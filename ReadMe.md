# **LangChain Experiments**

This project is meant to experiment with Langchain. 

## **Table of Contents**
1. [Introduction](#introduction)
2. [Pre-requisites](#pre-requisites)
3. [Installation](#installation)
4. [Available Scripts](#available-scripts)
   - [1. Create a New Experiment](#1-create-a-new-experiment)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

---

## **Introduction**

`langchain-experiments` is a Python project that uses Poetry for package and dependency management. This repository contains helpful scripts automate the creation of new experiments with corresponding test templates.

---

## **Pre-requisites**

Before installing and running the project, ensure you have the following dependencies installed:

1. **Python 3.11.8** or higher: The project is tested with this version of Python.
   - Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. **Poetry**: A dependency and package manager for Python.
   - Installation:
     ```bash
     curl -sSL https://install.python-poetry.org | python3 -
     ```
     After installation, ensure that Poetry is added to your PATH:
     ```bash
     poetry --version
     ```

Ensure these prerequisites are set up before proceeding with the installation.

---

## **Installation**

Once the pre-requisites are installed, clone the repository and run the following command:
```bash
poetry install
```

This installs all dependencies and registers the scripts as Poetry commands.

---

## **Available Scripts**

### **1. Create a New Experiment**

**Script:** `scripts/create_experiment.py`

**Purpose:** Automates the creation of a new experiment folder structure and corresponding test folder.

**Command:**
```bash
poetry run create-experiment
```

**Behavior:**
1. Prompts for the experiment name.
2. Creates the following folder structure:
    ```plaintext
    langchain_experiments/
    └── [experiment_name]/
        ├── __init__.py
        └── experiment.py  # Main experiment script
    tests/
    └── [experiment_name]/
        ├── __init__.py
        └── test_experiment.py  # Corresponding test script
    ```
3. Adds boilerplate content for the `experiment.py` and `test_experiment.py` files.

**Example:**
```bash
Enter the name of the new experiment: experiment_3
```
Result:
```plaintext
Experiment 'experiment_3' created successfully at 'langchain_experiments/experiment_3'.
```

---

## **Usage**

### Running Commands

- **Create a New Experiment:**
  ```bash
  poetry run create-experiment
  ```

### Listing All Available Poetry Commands
To list all available scripts:
```bash
poetry run --help
```

---

## **Contributing**

If you want to add new scripts or enhance existing ones:
1. Add your script in the `scripts/` folder.
2. Register the script in `pyproject.toml` under `[tool.poetry.scripts]`.
3. Run `poetry install` to apply changes.
4. Add corresponding unit tests in the `tests/` directory.

---

## **License**

This is an open-source project released under the MIT license. Thus, as long you distribute the LICENSE and acknowledge the work, you can safely clone or fork this project and use it as a source of inspiration for whatever you want.

