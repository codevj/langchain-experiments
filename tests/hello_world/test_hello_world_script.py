# Unit test for hello_world_script
from langchain_experiments.hello_world.hello_world_script import run_experiment

def test_run_experiment():
    # Ensure the experiment runs without errors
    assert run_experiment() is None
