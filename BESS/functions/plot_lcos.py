#!/usr/bin/env python
"""
This module provides a function to plot the Levelized Cost of Storage (LCOS) for a utility scale battery system.
"""

import pandas as pd
import matplotlib.pyplot as plt

__author__ = "Christoph Ertl"
__copyright__ = "Copyright 2025, Christoph Ertl"
__credits__ = ["Christoph Ertl"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Christoph Ertl"
__email__ = "christoph.ertl@student.tugraz.at"
__status__ = "Development"


def plot_lcos(df: pd.DataFrame) -> None:
    """
    Plot the Levelized Cost of Storage (LCOS) over time.

    :param df: DataFrame containing the columns 'year' and 'LCOS in €/kWh'
    :type df: pandas.DataFrame

    :return: None
    :rtype: None
    """
    plt.figure()
    plt.plot(df["year"], df["LCOS in €/kWh"]*1000, linewidth=2)
    plt.xlabel("Year", fontsize=16)
    plt.ylabel("LCOS [€/MWh]", fontsize=16)
    plt.title(f"BESS LCOS projection ({df['year'].min()}–{df['year'].max()})", fontsize=18, pad=20)
    plt.tick_params(axis='both', labelsize=14)
    plt.grid(True)
    plt.tight_layout()
    plt.show()