from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
from pathlib import Path

# Load the iris dataset
iris = load_iris()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model in the same directory as the script
model_path = Path(__file__).parent / "iris_model.pkl"
joblib.dump(model, model_path)

