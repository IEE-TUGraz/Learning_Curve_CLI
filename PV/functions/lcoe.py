#!/usr/bin/env python
"""
This module provides a function to calculate the Levelized Cost of Electricity (LCOE) for a PV system using financial and
technical input parameters.
"""

import numpy as np

__author__ = "Christoph Ertl"
__copyright__ = "Copyright 2025, Christoph Ertl"
__credits__ = ["Christoph Ertl"]
__license__ = "MIT"
__version__ = "2.0.0"
__maintainer__ = "Christoph Ertl"
__email__ = "christoph.ertl@student.tugraz.at"
__status__ = "Development"


def lcoe(capex_module: float, capex_inverter: float, capex_BOS: float, opex_share: float, annual_yield: float, wacc_nominal: float, 
         wacc_real: float, degradation_rate: float, lifetime: int, res_value: float) -> float:
    """
    Calculates the Levelized Cost of Electricity (LCOE).

    :param capex_module: Capital expenditure of module in €/kWp
    :type capex_module: float

    :param capex_inverter: Capital expenditure of inverter in €/kWp
    :type capex_inverter: float

    :param capex_BOS: Capital expenditure of BoS in €/kWp
    :type capex_BOS: float

    :param opex_share: Annual operational expenditure as a share of total CAPEX in %
    :type opex_share: float

    :param annual_yield: Specific annual energy yield in kWh/kWp
    :type annual_yield: float

    :param wacc_nominal: Nominal Weighted Average Cost of Capital
    :type wacc_nominal: float

    :param wacc_real: Real Weighted Average Cost of Capital
    :type wacc_real: float

    :param degradation_rate: Annual degradation rate of PV panels (e.g. 0.0025 for 0.25%)
    :type degradation_rate: float

    :param lifetime: Lifetime of the PV system in years
    :type lifetime: int

    :param res_value: Residual value of the system at the end of its lifetime in €/kWp
    :type res_value: float

    :return: Levelized Cost of Electricity in €/kWh
    :rtype: float
    """

    t = np.arange(1, lifetime + 1)
        
    capex_total = capex_module + capex_inverter + capex_BOS

    opex = capex_total * opex_share
    opex_total = np.sum(opex / (1 + wacc_nominal)**t)
    
    inv_repl = capex_inverter / (1 + wacc_nominal)**(lifetime/2)

    res_value_discounted = res_value / (1 + wacc_nominal)**lifetime

    yield_total = np.sum((annual_yield * (1 - degradation_rate)**t) / (1 + wacc_real)**t)

    lcoe = (capex_total + opex_total + inv_repl - res_value_discounted) / (yield_total)

    return float(lcoe)