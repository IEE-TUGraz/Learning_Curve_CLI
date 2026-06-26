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


def lcoe(capex: float, opex_share: float, capacity_factor: float, wacc_nominal: float, wacc_real: float, lifetime: int, res_value: float) -> float:
    """
    Calculates the Levelized Cost of Electricity (LCOE).

    :param capex: Capital expenditure in €/kWp
    :type capex: float

    :param opex_share: Annual operational expenditure as a share of CAPEX in %
    :type opex_share: float

    :param capacity_factor: Capacity factor in %
    :type capacity_factor: float

    :param wacc_nominal: Nominal Weighted Average Cost of Capital
    :type wacc_nominal: float

    :param wacc_real: Real Weighted Average Cost of Capital
    :type wacc_real: float

    :param lifetime: Lifetime of the wind power plant in years
    :type lifetime: int

    :param res_value: Residual value of the system at the end of its lifetime in €/kWp
    :type res_value: float

    :return: Levelized Cost of Electricity in €/kWh
    :rtype: float
    """

    t = np.arange(1, lifetime + 1)

    opex = capex * opex_share 
    opex_total = np.sum(opex / (1 + wacc_nominal)**t)
    res_value_discounted = res_value / (1 + wacc_nominal)**lifetime
    annual_yield = capacity_factor * 8760  # kWh/kW per year
    
    yield_total = np.sum((annual_yield) / (1 + wacc_real)**t)

    lcoe = (capex + opex_total - res_value_discounted) / (yield_total)

    return float(lcoe)