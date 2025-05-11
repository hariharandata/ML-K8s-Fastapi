import subprocess
import sys
from pathlib import Path

import joblib
import pytest

# Determine the root directory of the project (ML-K8s-Fastapi)
# This assumes tests are run from the project root or that the project root is in PYTHONPATH
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_SCRIPT_PATH = PROJECT_ROOT / "src" / "model.py"
MODEL_OUTPUT_PATH = PROJECT_ROOT / "src" / "iris_model.pkl"


def test_model_script_runs_and_saves_model():
    """Test that the model.py script runs, creates iris_model.pkl, and the model can be loaded."""
    # Ensure the model file doesn't exist before running the script to ensure the script creates it
    if MODEL_OUTPUT_PATH.exists():
        MODEL_OUTPUT_PATH.unlink()

    # Run the model.py script
    # Using sys.executable ensures we use the same Python interpreter that's running pytest
    process = subprocess.run(
        [sys.executable, str(MODEL_SCRIPT_PATH)], capture_output=True, text=True
    )

    # Check that the script ran successfully
    assert process.returncode == 0, f"Model script failed with error: {process.stderr}"

    # Check that the model file was created
    assert MODEL_OUTPUT_PATH.exists(), f"Model file {MODEL_OUTPUT_PATH} was not created."

    # Try to load the model to ensure it's valid
    try:
        model = joblib.load(MODEL_OUTPUT_PATH)
        print("Model loaded successfully.")
        assert model is not None, "Loaded model is None."
        # You could add more specific assertions about the loaded model if needed
        # e.g., assert hasattr(model, 'predict')
    except Exception as e:
        pytest.fail(f"Failed to load the saved model: {e}")
    finally:
        # Clean up: remove the created model file
        if MODEL_OUTPUT_PATH.exists():
            MODEL_OUTPUT_PATH.unlink()


if __name__ == "__main__":
    test_model_script_runs_and_saves_model()
