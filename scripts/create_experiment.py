import os

def create_experiment():
    """Create a new experiment folder structure."""
    experiment_name = input("Enter the name of the new experiment: ").strip()

    if not experiment_name:
        print("Experiment name cannot be empty.")
        return

    base_dir = os.path.join("langchain_experiments", experiment_name)

    if os.path.exists(base_dir):
        print(f"Experiment '{experiment_name}' already exists.")
        return

    # Create experiment directories
    os.makedirs(base_dir)
    os.makedirs(os.path.join("tests", experiment_name))

    # Create __init__.py files
    open(os.path.join(base_dir, "__init__.py"), "w").close()
    open(os.path.join("tests", experiment_name, "__init__.py"), "w").close()

    # Create default experiment.py file
    experiment_file = os.path.join(base_dir, "experiment.py")
    with open(experiment_file, "w") as f:
        f.write(f"""# Experiment: {experiment_name}

def run_experiment():
    print("Running experiment '{experiment_name}'")

if __name__ == "__main__":
    run_experiment()
""")

    # Create default test file
    test_file = os.path.join("tests", experiment_name, "test_experiment.py")
    with open(test_file, "w") as f:
        f.write(f"""# Unit test for {experiment_name}

from langchain_experiments.{experiment_name}.experiment import run_experiment

def test_run_experiment():
    assert run_experiment() is None  # Check for successful execution
""")

    print(f"Experiment '{experiment_name}' created successfully at '{base_dir}'.")

