#!/usr/bin/env python
"""
This module provides a function to calculate the real Weighted Average Cost of Capital (WACC) by using 
different financial input parameters.
"""

__author__ = "Christoph Ertl"
__copyright__ = "Copyright 2025, Christoph Ertl"
__credits__ = ["Christoph Ertl"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Christoph Ertl"
__email__ = "christoph.ertl@student.tugraz.at"
__status__ = "Development"


def wacc_real(D: float, CT: float, k_d: float, k_e: float, inflation: float) -> float:
    """
    Calculates the real Weighted Average Cost of Capital (WACC).

    :param D: Debt ratio (e.g. 0.8 for 80% debt financing)
    :type D: float

    :param CT: Corporate tax rate in %
    :type CT: float

    :param k_d: Interest rate on debt in %
    :type k_d: float

    :param k_e: Interest rate on equity in %
    :type k_e: float

    :param inflation: Expected inflation rate in %
    :type inflation: float

    :return: Real WACC value
    :rtype: float
    """
    E = 1 - D 
    wacc_nom = (D * k_d * (1 - CT) + E * k_e) / (D + E)
    wacc_real = ((1 + wacc_nom) / (1 + inflation)) - 1

    return wacc_real
