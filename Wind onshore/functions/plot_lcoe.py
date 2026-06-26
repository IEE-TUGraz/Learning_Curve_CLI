#!/usr/bin/env python
"""
This module provides a function to plot the Levelized Cost of Electricity (LCOE) for a wind power plant.
"""

import pandas as pd
import matplotlib.pyplot as plt

__author__ = "Christoph Ertl"
__copyright__ = "Copyright 2025, Christoph Ertl"
__credits__ = ["Christoph Ertl"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Christoph Ertl"
__email__ = "christoph.ertl@student.tugraz.at"
__status__ = "Development"


def plot_lcoe(df: pd.DataFrame) -> None:
    """
    Plot the Levelized Cost of Electricity (LCOE) over time.

    :param df: DataFrame containing the columns 'year' and 'LCOE in €/kWh'
    :type df: pandas.DataFrame

    :return: None
    :rtype: None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df["year"], df["LCOE in €/kWh"]*1000, linewidth=2)
    plt.xlabel("Year", fontsize=16)
    plt.ylabel("LCOE [€/MWh]", fontsize=16)
    plt.title(f"Wind onshore LCOE projection ({df['year'].min()}–{df['year'].max()})", fontsize=18, pad=20)
    plt.tick_params(axis='both', labelsize=14)
    plt.grid(True)
    plt.tight_layout()
    plt.show()