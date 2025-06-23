import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import os

def train_model(input_path, model_path):
    # Load processed data
    df = pd.read_csv(input_path)
    X = df.drop("target", axis=1)
    y = df["target"]

    # Split and train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(multi_class='ovr', max_iter=200)
    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, model_path)
    print(f"Model trained and saved to {model_path}")

if __name__ == "__main__":
    input_path = os.getenv("INPUT_PATH", "/data/processed_data.csv")
    model_path = os.getenv("MODEL_PATH", "/data/model.pkl")
    train_model(input_path, model_path)