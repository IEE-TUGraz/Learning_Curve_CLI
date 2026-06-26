#!/usr/bin/env python
"""
Main script for calculating and plotting the Levelized Cost of Electricity (LCOE)
based on a master configuration input file (YAML file). The YAML file contains paths 
to CSV files which contain the data.

This script loads parameters and cumulative installation data, calculates
nominal and real WACC, projects CAPEX via learning rates, computes LCOE and
visualizes the result as a time series plot.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yaml
import typer

from pathlib import Path

from functions.wacc_nom import wacc_nom
from functions.wacc_real import wacc_real
from functions.lcoe import lcoe
from functions.plot_lcoe import plot_lcoe

__author__ = "Christoph Ertl"
__copyright__ = "Copyright 2025, Christoph Ertl"
__credits__ = ["Christoph Ertl"]
__license__ = "MIT"
__version__ = "8.0.0"
__maintainer__ = "Christoph Ertl"
__email__ = "christoph.ertl@student.tugraz.at"
__status__ = "Development"


def main(config: str = typer.Option(..., help="path to config.yaml")):

    print(f"BUsed configuration: {config}")
    
    config_path = Path(config)
    
    base_path = config_path.parent

    with open(config_path, "r") as file:
        try:
            config_file = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)

    # Get paths
    paths = config_file["paths"]

    # Read CSVs
    baseline_values_df = pd.read_csv(base_path / paths["baseline_values"])
    baseline_values = dict(zip(baseline_values_df["parameter"], baseline_values_df["value"]))

    learning_rates_df = pd.read_csv(base_path / paths["learning_rates"])
    learning_rates = dict(zip(learning_rates_df["parameter"], learning_rates_df["value"]))

    financial_parameters_df = pd.read_csv(base_path / paths["financial_parameters"])
    financial_parameters = dict(zip(financial_parameters_df["parameter"], financial_parameters_df["value"]))

    technical_parameters_df = pd.read_csv(base_path / paths["technical_parameters"])
    technical_parameters = dict(zip(technical_parameters_df["parameter"], technical_parameters_df["value"]))

    cum_installations_df = pd.read_csv(base_path / paths["cumulative_installations"])

    # Extract data from dataframes
    capex_module_base   = baseline_values["capex_module_base"] # CAPEX of module in the start year €/kWp
    capex_inverter_base   = baseline_values["capex_inverter_base"] # CAPEX of inverter in the start year €/kWp
    capex_BOS_base   = baseline_values["capex_BOS_base"] # CAPEX of BoS in the start year €/kWp
    opex_share    = baseline_values["opex_share"] # annual OPEX as a share of the total CAPEX in %
    yield_base   = baseline_values["yield_base"] # specific yield in kWh/kWp

    capex_module_LR     = learning_rates["capex_module_LR"] # Module learning rate in %
    capex_inverter_LR     = learning_rates["capex_inverter_LR"] # Inverter learning rate in %
    capex_BOS_LR     = learning_rates["capex_BOS_LR"] # BoS learning rate in %

    D            = financial_parameters["debt_ratio"] # share of debt financing (e.g. 70% means 70% debt financing and 30%  equity financing)
    CT           = financial_parameters["corporate_tax"] # corporate tax rate in %
    k_d          = financial_parameters["interest_debt"] # interest rate on debt in %
    k_e          = financial_parameters["interest_equity"] # interest rate on equity in %
    inflation    = financial_parameters["inflation_rate"] # average inflation rate in %

    degradation  = technical_parameters["degradation_rate"] # 0.25% annual degradation rate for PV modules
    lifetime     = technical_parameters["system_lifetime"] # lifetime of the plant in years
    res_value    = technical_parameters["res_value"] # residual value of the system at the end of its lifetime in €/kWp


    # WACC calculation
    wacc_r = wacc_real(D, CT, k_d, k_e, inflation)
    wacc_n = wacc_nom(D, CT, k_d, k_e)

    print("Wacc_nom =", wacc_n)
    print("Wacc_real =", wacc_r)

    # CAPEX projections
    df = cum_installations_df
    b1 = -np.log2(1 - capex_module_LR) # learning exponent
    b2 = -np.log2(1 - capex_inverter_LR)
    b3 = -np.log2(1 - capex_BOS_LR)

    x0 = df["capacity_GWp"].iloc[0] # installed capacity in year 0

    df["CAPEX from module in €/kWp"] = capex_module_base * (df["capacity_GWp"] / x0) ** (-b1)
    df["CAPEX from inverter in €/kW"] = capex_inverter_base * (df["capacity_GWp"] / x0) ** (-b2)
    df["CAPEX from BoS in €/kW"] = capex_BOS_base * (df["capacity_GWp"] / x0) ** (-b3)

    # Calculating LCOE
    lcoe_values = []

    for i in range(len(df)):
        capex_module = df["CAPEX from module in €/kWp"].iloc[i]
        capex_inverter = df["CAPEX from inverter in €/kW"].iloc[i]
        capex_BOS = df["CAPEX from BoS in €/kW"].iloc[i]

        lcoe_i = lcoe(capex_module, capex_inverter, capex_BOS, opex_share, yield_base, wacc_n, wacc_r, degradation, lifetime, res_value)
        lcoe_values.append(lcoe_i)

    df["LCOE in €/kWh"] = lcoe_values
    print(df)

    #Optional: export CSV file
    #df[["year", "LCOE in €/kWh"]].to_csv(base_path / "PV_household.csv", index=False)

    # plot
    plot_lcoe(df)


if __name__ == "__main__":
    typer.run(main)