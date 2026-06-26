# Experience Curve Cost Projection Tool

An open-source Python framework for projecting future technology costs of renewable energy technologies using **experience curves**. The tool provides transparent and parameterizable models for calculating the **Levelized Cost of Electricity (LCOE)** and **Levelized Cost of Storage (LCOS)** of different technologies and enables long-term cost projections for use in **Energy System Optimization Models (ESOMs)**.

---

## Overview

Planning future energy systems requires reliable assumptions about the costs of emerging technologies. While many energy system models include techno-economic parameters, transparent and reproducible methods for projecting future technology costs are often lacking.

This project addresses this challenge by providing an open-source framework that

- projects future technology costs using experience curves,
- calculates technology-specific LCOE and LCOS,
- allows easy modification of technical and economic assumptions,
- enables scenario and sensitivity analyses, and
- provides transparent and reproducible cost projections.

Although originally developed using Austria-specific data, the framework is fully parameterizable and can easily be adapted to other countries or regions.

---

## Supported Technologies

Currently, the tool supports:

- ☀️ Photovoltaic (Utility-scale)
- 🏠 Photovoltaic (Residential)
- 🌬️ Onshore Wind Power
- 🔋 Lithium-Ion Battery Energy Storage Systems (BESS)
- ⚡ Vanadium Redox Flow Battery (VRFB)

Additional technologies can easily be integrated.

---

## Features

- Experience curve based cost projections
- One-factor, two-factor and multi-factor learning models
- Technology-specific LCOE and LCOS calculations
- Modular and parameterizable architecture
- Support for scenario analysis
- Sensitivity analysis of technical and economic parameters
- Transparent input data structure
- Publication-quality plots
- Export of results for further analysis

---

## Cost Models

The framework implements technology-specific cost models for:

### Photovoltaics

- Module costs
- Inverter costs
- Balance of System (BoS)
- Performance degradation
- Inverter replacement
- Operating costs

### Wind Power

- CAPEX
- OPEX
- Capacity factor
- Lifetime
- Discount rate

### Battery Energy Storage Systems

- Investment costs
- Charging costs
- Round-trip efficiency
- Cycle degradation
- Operating costs
- Residual value

---

## Methodology

Future technology costs are estimated using **experience curves**, which describe the reduction in costs as cumulative installed capacity increases.

The framework supports

- One-Factor Experience Curves (OFEC)
- Two-Factor Experience Curves (TFEC)
- Multi-Factor Experience Curves (MFEC)

allowing additional explanatory variables (e.g. material prices or innovation indicators) to improve projection accuracy.

---

## Typical Workflow

1. Import technology-specific input data.
2. Define technical and economic assumptions.
3. Configure experience curve parameters.
4. Calculate current LCOE/LCOS.
5. Project future costs.
6. Perform sensitivity analyses.
7. Export tables and figures.

---

## Project Structure

```text
├── data/               # Input data
├── models/             # LCOE / LCOS models
├── experience_curves/  # Experience curve implementations
├── scenarios/          # Scenario definitions
├── results/            # Generated figures and tables
├── notebooks/          # Example Jupyter notebooks
├── plots/              # Plotting utilities
└── main.py
```

---

## Example Applications

The tool can be used for

- Energy system optimization
- Capacity expansion planning
- Renewable investment analysis
- Long-term technology assessments
- Academic research
- Scenario analysis
- Teaching

---

## Requirements

- Python 3.10+
- NumPy
- Pandas
- SciPy
- Matplotlib
- Plotly (optional)

Install dependencies using

```bash
pip install -r requirements.txt
```

---

## Citation

If you use this tool in academic work, please cite:

> Ertl, C. (2025). *A model of technological learning for low-carbon energy technologies in the Austrian power sector*. Master's Thesis, Graz University of Technology.

---

## License

This project is released under the MIT License.

---

## Contributing

Contributions are welcome!

Feel free to

- report bugs,
- suggest new features,
- improve documentation,
- add new technologies, or
- submit pull requests.

---

## Contact

Institute of Electricity Economics and Energy Innovation (IEE)

Graz University of Technology

For questions or suggestions, please open an issue on GitHub.
