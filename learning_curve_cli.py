"""
CLI script to run different learning curve models with specified configuration files.
The available models are:
- Wind onshore 
- PV (utility scale and household)
- BESS (lithium ion and VRF)

Each model is located in its own subdirectory and is executed with a specific configuration file.
The configuration files are stored in the respective "config_files" subdirectory of each model.
The configuration files are YAML files that contain paths to CSV files with the necessary data for the models.
The script uses the Typer library to create a command-line interface (CLI) for easy execution of the models.

To start a model, use the following command:
python learning_curve_cli.py --type <model_type> --config <config_file>
"""

import typer
import subprocess
from pathlib import Path

__author__ = "Christoph Ertl"
__copyright__ = "Copyright 2025, Christoph Ertl"
__credits__ = ["Christoph Ertl"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Christoph Ertl"
__email__ = "christoph.ertl@student.tugraz.at"
__status__ = "Development"

app = typer.Typer()

MODELS = {
    "PV": "PV/main.py",
    "wind": "Wind onshore/main.py",
    "BESS": "BESS/main.py"
}

@app.command()
def run(
    type: str = typer.Option(..., "--type", help="model type (wind, PV or BESS)"),
    config: str = typer.Option(..., "--config", help="name of the config file (.yaml file)")
):

    if type not in MODELS:
        typer.echo(f"unknown type: {type}")
        raise typer.Exit(code=1)
    
    script_path = Path(MODELS[type])

    if not script_path.exists():
        typer.echo(f"script not found: {script_path}")
        raise typer.Exit(code=1)

    config_path = script_path.parent / "config_files" / config

    if not config_path.exists():
        typer.echo(f"config file not found: {config_path}")
        raise typer.Exit(code=1)
    
    # Start of the model
    subprocess.run(["python", str(script_path), "--config", str(config_path)])

if __name__ == "__main__":
    app()