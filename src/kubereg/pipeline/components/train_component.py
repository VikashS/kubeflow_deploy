from kfp import dsl

@dsl.component
def train_component(input_path: str, model_path: str) -> str:
    return dsl.ContainerOp(
        name="Train",
        image="train-image:latest",
        command=["python", "-m", "myapp.training.train"],
        arguments=[],
        container_kwargs={
            "env": [
                {"name": "INPUT_PATH", "value": input_path},
                {"name": "MODEL_PATH", "value": model_path},
            ]
        },
    ).output