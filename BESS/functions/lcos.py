#!/usr/bin/env python
"""
This module provides a function to calculate the Levelized Cost of Storage (LCOS) for a utility scale battery system with financial and
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


def lcos(capex: float, opex_share: float, wacc_nominal: float, wacc_real: float, lifetime: int, cycles_pa: int, electricity_price: float, round_trip_eff: float, time_degradation: float, DoD: float, res_value: float) -> float:
    """
    Calculates the Levelized Cost of Storage (LCOS).

    :param capex: Capital expenditure in €/kWh
    :type capex: float

    :param opex_share: Annual operational expenditure as a share of CAPEX in %
    :type opex_share: float

    :param wacc_nominal: Nominal Weighted Average Cost of Capital
    :type wacc_nominal: float

    :param wacc_real: Real Weighted Average Cost of Capital
    :type wacc_real: float

    :param lifetime: Lifetime of the battery system in years
    :type lifetime: int

    :param cycles_pa: Number of cycles per year
    :type cycles_pa: int

    :param electricity_price: Electricity price in €/kWh
    :type electricity_price: float

    :param round_trip_eff: Round trip efficiency of the system in %
    :type round_trip_eff: float

    :param time_degradation: Degradation rate of the system in % per year
    :type time_degradation: float

    :param DoD: Depth of Discharge (DoD) in %
    :type DoD: float

    :param res_value: Residual value of the system at the end of its lifetime in €/kWh
    :type res_value: float

    :return: Levelized Cost of Storage in €/kWh
    :rtype: float
    """

    t = np.arange(1, lifetime + 1)

    opex = capex * opex_share 
    opex_total = np.sum(opex / (1 + wacc_nominal)**t)

    charging_cost = np.sum((1 * electricity_price * cycles_pa * DoD * (1 - time_degradation)**t) / (1 + wacc_nominal)**t)

    res_value_discounted = res_value / (1 + wacc_nominal)**lifetime


    lcos = (capex + opex_total + charging_cost - res_value_discounted) / (np.sum((1 * cycles_pa * DoD * (1 - time_degradation)**t * round_trip_eff) / (1 + wacc_real)**t))

    return float(lcos)