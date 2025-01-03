import os
import json
from pathlib import Path

def create_experiment():
    """Automates the creation of a new experiment folder structure with a Jupyter notebook."""
    experiment_name = input("Enter the name of the new experiment: ").strip()

    if not experiment_name:
        print("Experiment name cannot be empty.")
        return

    # Automatically detect the parent directory of `scripts` folder
    scripts_dir = Path(__file__).parent
    parent_dir = scripts_dir.parent  # The root project directory
    experiments_dir = parent_dir / "langchain_experiments"

    base_dir = experiments_dir / experiment_name
    if base_dir.exists():
        print(f"Experiment '{experiment_name}' already exists.")
        return

    # Create experiment directories and files
    os.makedirs(base_dir)
    os.makedirs(parent_dir / "tests" / experiment_name)

    (base_dir / "__init__.py").touch()
    with open(base_dir / "experiment.py", "w") as f:
        f.write(f"""# Experiment: {experiment_name}

def run_experiment():
    print("Running experiment '{experiment_name}'")

if __name__ == "__main__":
    run_experiment()
""")

    with open(parent_dir / "tests" / experiment_name / "test_experiment.py", "w") as f:
        f.write(f"""# Unit test for {experiment_name}

from langchain_experiments.{experiment_name}.experiment import run_experiment

def test_run_experiment():
    assert run_experiment() is None  # Check for successful execution
""")

    # Create Jupyter notebook
    notebook_path = base_dir / "experiment.ipynb"
    notebook_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# Experiment: {experiment_name}\n\nThis notebook contains notes, results, and code for the experiment."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["# Import necessary libraries\nfrom langchain.llms import OpenAI\n\n# Placeholder function\nprint('Hello from the Jupyter notebook')"]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    with open(notebook_path, "w") as f:
        json.dump(notebook_content, f)

    print(f"Experiment '{experiment_name}' created successfully with a Jupyter notebook at '{base_dir}'!")
