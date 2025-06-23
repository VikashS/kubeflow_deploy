from kfp import dsl

@dsl.component
def etl_component(output_path: str) -> str:
    return dsl.ContainerOp(
        name="ETL",
        image="etl-image:latest",
        command=["python", "-m", "myapp.etl.etl"],
        arguments=[],
        container_kwargs={
            "env": [
                {"name": "OUTPUT_PATH", "value": output_path},
            ]
        },
    ).output