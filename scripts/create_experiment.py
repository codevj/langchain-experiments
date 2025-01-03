import os
import re
import sys
import json

def is_valid_experiment_name(name):
    """Checks if the experiment name is a valid Python identifier."""
    return bool(re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name))


def create_experiment():
    """Automates the creation of a new experiment folder structure with a Jupyter notebook."""
    experiment_name = input("Enter the name of the new experiment: ").strip()

    if not experiment_name:
        print("Experiment name cannot be empty.")
        sys.exit(1)

    if not is_valid_experiment_name(experiment_name):
        print(f"Invalid experiment name '{experiment_name}'. It must be a valid Python identifier.")
        print("The name should:")
        print("  - Start with a letter or underscore.")
        print("  - Only contain letters, digits, and underscores.")
        sys.exit(1)

    base_dir = os.path.join("langchain_experiments", experiment_name)
    if os.path.exists(base_dir):
        print(f"Experiment '{experiment_name}' already exists.")
        sys.exit(1)

    # Create experiment directories and files
    os.makedirs(base_dir)
    os.makedirs(os.path.join("tests", experiment_name))

    open(os.path.join(base_dir, "__init__.py"), "w").close()
    with open(os.path.join(base_dir, "experiment.py"), "w") as f:
        f.write(f"""# Experiment: {experiment_name}

def run_experiment():
    print("Running experiment '{experiment_name}'")

if __name__ == "__main__":
    run_experiment()
""")

    with open(os.path.join("tests", experiment_name, "test_experiment.py"), "w") as f:
        f.write(f"""# Unit test for {experiment_name}

from langchain_experiments.{experiment_name}.experiment import run_experiment

def test_run_experiment():
    assert run_experiment() is None  # Check for successful execution
""")

    # Create Jupyter notebook
    notebook_path = os.path.join(base_dir, "experiment.ipynb")
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

    print(f"Experiment '{experiment_name}' created successfully with a Jupyter notebook!")
