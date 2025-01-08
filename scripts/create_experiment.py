import os
import re
import json
import toml

# Define the base project name as a constant
BASE_PROJECT_NAME = "langchain_experiments"

def is_valid_experiment_name(name):
    """Ensure the experiment name is a valid Python module name."""
    return bool(re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name))

def update_pyproject_toml(experiment_name):
    """Add the Poe task to pyproject.toml."""
    pyproject_path = "pyproject.toml"
    if not os.path.exists(pyproject_path):
        print("No pyproject.toml found in the current directory.")
        return

    # Read existing pyproject.toml
    with open(pyproject_path, "r") as f:
        pyproject_data = toml.load(f)

    # Ensure necessary sections exist
    if "tool" not in pyproject_data:
        pyproject_data["tool"] = {}
    if "poe" not in pyproject_data["tool"]:
        pyproject_data["tool"]["poe"] = {}
    if "tasks" not in pyproject_data["tool"]["poe"]:
        pyproject_data["tool"]["poe"]["tasks"] = {}

    # Add the new task
    task_name = f"{experiment_name}_run"
    task_command = f"python {BASE_PROJECT_NAME}/{experiment_name}/{experiment_name}_script.py"
    pyproject_data["tool"]["poe"]["tasks"][task_name] = task_command

    # Write updated pyproject.toml
    with open(pyproject_path, "w") as f:
        toml.dump(pyproject_data, f)

    print(f"Poe task '{task_name}' added to pyproject.toml!")

def create_experiment():
    """Automates the creation of a new experiment folder structure."""
    experiment_name = input("Enter the name of the new experiment: ").strip()

    if not experiment_name or not is_valid_experiment_name(experiment_name):
        print("Invalid experiment name. Please use letters, numbers, and underscores.")
        return

    base_dir = os.path.join(BASE_PROJECT_NAME, experiment_name)
    if os.path.exists(base_dir):
        print(f"Experiment '{experiment_name}' already exists.")
        return

    # Create experiment directories and boilerplate files
    os.makedirs(base_dir)
    os.makedirs(os.path.join("tests", experiment_name))

    open(os.path.join(base_dir, "__init__.py"), "w").close()

    # Generate the experiment Python script
    script_file = f"{experiment_name}_script.py"
    with open(os.path.join(base_dir, script_file), "w") as f:
        f.write(f"""# Experiment: {experiment_name}
# Instructions:
# To run this experiment:
# 1. Using Poetry:
#    poetry run python {BASE_PROJECT_NAME}/{experiment_name}/{script_file}
# 2. Or with Poe the Poet:
#    poe {experiment_name}_run

def run_experiment():
    print("Running experiment '{experiment_name}'")

if __name__ == "__main__":
    run_experiment()
""")

    # Generate the Jupyter notebook
    notebook_path = os.path.join(base_dir, f"{experiment_name}_notebook.ipynb")
    notebook_content = {
        "cells": [
            {"cell_type": "markdown", "source": [f"# Experiment: {experiment_name}"], "metadata": {}},
            {
                "cell_type": "code",
                "source": [f"""# Import the experiment logic
from {BASE_PROJECT_NAME}.{experiment_name}.{experiment_name}_script import run_experiment

# Run the experiment
run_experiment()"""],
                "metadata": {}
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python (langchain-experiments)",
                "language": "python",
                "name": "langchain-experiments"
            },
            "language_info": {
                "name": "python",
                "version": "3.11"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    with open(notebook_path, "w") as f:
        json.dump(notebook_content, f)

    # Generate the test file
    with open(os.path.join("tests", experiment_name, f"test_{experiment_name}_script.py"), "w") as f:
        f.write(f"""# Unit test for {experiment_name}_script
from {BASE_PROJECT_NAME}.{experiment_name}.{experiment_name}_script import run_experiment

def test_run_experiment():
    # Ensure the experiment runs without errors
    assert run_experiment() is None
""")

    print(f"Experiment '{experiment_name}' created successfully!")

    # Automatically update pyproject.toml with the new task
    update_pyproject_toml(experiment_name)

if __name__ == "__main__":
    create_experiment()
