from sklearn.datasets import load_iris
import pandas as pd
import os


def etl_process(output_path):
    # Load Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target

    # Simple ETL: Remove rows with any values < 0 (if any)
    df = df[df >= 0].dropna()

    # Save processed data
    df.to_csv(output_path, index=False)
    print(f"ETL completed. Output saved to {output_path}")


if __name__ == "__main__":
    output_path = os.getenv("OUTPUT_PATH", "/data/processed_data.csv")
    etl_process(output_path)