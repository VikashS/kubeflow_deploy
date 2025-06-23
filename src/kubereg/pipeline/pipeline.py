from kfp import dsl
from kubereg.pipeline.components.etl_component import etl_component
from kubereg.pipeline.components.train_component import train_component

@dsl.pipeline(
    name="Model Training Pipeline",
    description="Pipeline for ETL and model training with Iris dataset"
)
def model_training_pipeline(
    processed_path: str = "/data/processed_data.csv",
    model_path: str = "/data/model.pkl"
):
    etl_task = etl_component(output_path=processed_path)
    train_task = train_component(input_path=processed_path, model_path=model_path)
    train_task.after(etl_task)

if __name__ == "__main__":
    from kfp.compiler import Compiler
    Compiler().compile(model_training_pipeline, "pipeline.yaml")