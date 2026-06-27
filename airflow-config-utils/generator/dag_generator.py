import yaml
from pathlib import Path


def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    config_dir = Path("../airflow-configs/configs")

    for file in config_dir.rglob("*.yaml"):
        print(load_yaml(file))