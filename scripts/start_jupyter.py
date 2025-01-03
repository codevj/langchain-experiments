import os
import subprocess

def register_kernel():
    """Registers the Poetry environment as a Jupyter kernel."""
    print("Registering Jupyter kernel for langchain-experiments...")
    try:
        subprocess.run([
            "python",
            "-m",
            "ipykernel",
            "install",
            "--user",
            "--name=langchain-experiments",
            "--display-name",
            "Python (langchain-experiments)"
        ], check=True)
        print("Jupyter kernel registered successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to register Jupyter kernel: {e}")

def start_jupyter():
    """Start Jupyter notebook in the langchain_experiments directory."""
    # Step 1: Register kernel
    register_kernel()

    # Step 2: Change directory and launch Jupyter Notebook
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../langchain_experiments")
    os.chdir(base_dir)  # Change to langchain_experiments directory
    print(f"Starting Jupyter Notebook in: {base_dir}")
    subprocess.run(["jupyter", "notebook"], check=True)
