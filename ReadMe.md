# **LangChain Experiments**

This project is meant to experiment with LangChain.

## **Table of Contents**
1. [Introduction](#introduction)
2. [Pre-requisites](#pre-requisites)
3. [Installation](#installation)
4. [Available Scripts](#available-scripts)
   - [1. Create a New Experiment](#1-create-a-new-experiment)
   - [2. Start Jupyter Notebook](#2-start-jupyter-notebook)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

---

## **Introduction**

`langchain-experiments` is a Python project that uses Poetry for package and dependency management. This repository contains helpful scripts to automate the creation of new experiments with corresponding test templates.

---

## **Pre-requisites**

Before installing and running the project, ensure you have the following dependencies installed:
1. **Poetry**: A dependency and package manager for Python.
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

**Purpose:** Automates the creation of a new experiment folder structure, a corresponding test folder, and a Jupyter notebook.

**Command:**
```bash
poetry run create-experiment
```

**Behavior:**
1. Prompts for the experiment name.
2. Creates the following folder structure:
    ```plaintext
    langchain_experiments/
    └── experiment_1/
        ├── __init__.py
        ├── experiment.py  # Main experiment script
        └── experiment.ipynb  # Jupyter notebook for interactive experimentation
    tests/
    └── experiment_1/
        ├── __init__.py
        └── test_experiment.py  # Corresponding test script
    ```
3. Adds boilerplate content for the `experiment.py`, `experiment.ipynb`, and `test_experiment.py` files.

**Example:**
```bash
Enter the name of the new experiment: experiment_1
```
Result:
```plaintext
Experiment 'experiment_1' created successfully at 'langchain_experiments/experiment_1'.
```

---

### **2. Start Jupyter Notebook**

**Script:** `scripts/start_jupyter.py`

**Purpose:** Launches the Jupyter notebook interface in the `langchain_experiments` folder and registers the Poetry environment as a Jupyter kernel.

**Command:**
```bash
poetry run start-notebook
```

**Behavior:**
1. Registers the Poetry virtual environment as a Jupyter kernel named `"Python (langchain-experiments)"`.
2. Opens Jupyter Notebook in the `langchain_experiments/` directory.

---

## **Usage**

### **1. Running Tests**

To run tests for all experiments:
```bash
poetry run pytest
```

To run tests for a specific experiment:
```bash
poetry run pytest tests/experiment_1/
```

This command runs the unit tests and reports the results, ensuring that your experiments work as expected.

### **2. Launching Jupyter Notebooks**

Each experiment includes a **Jupyter notebook** (`experiment.ipynb`) for interactive experimentation. To open the notebook, run:
```bash
poetry run start-notebook
```

This will:
1. Register the virtual environment as a Jupyter kernel.
2. Open Jupyter Notebook in your browser with the working directory set to `langchain_experiments/`.

Navigate to the appropriate experiment folder and open `experiment.ipynb` to start interactive experimentation.

---

## **Contributing**

If you want to add new scripts or enhance existing ones:
1. Add your script in the `scripts/` folder.
2. Register the script in `pyproject.toml` under `[tool.poetry.scripts]`.
3. Run `poetry install` to apply changes.
4. Add corresponding unit tests in the `tests/` directory.

---

## **License**

This is an open-source project released under the MIT license. Thus, as long as you distribute the LICENSE and acknowledge the work, you can safely clone or fork this project and use it as a source of inspiration for whatever you want.
