import pandas as pd
import yaml
import os

def data_processing(data_path):
    data = pd.read_csv(data_path)
    processed_data = data.dropna()
    return processed_data

if __name__ == "__main__":
    param_yaml_path = "params.yaml"

    with open(param_yaml_path) as yaml_file:
        param_yaml = yaml.safe_load(yaml_file)

    # Process Training Data
    train_data_path = os.path.join(param_yaml["split"]["dir"], param_yaml["split"]["train_file"])
    final_train_data = data_processing(data_path=train_data_path)

    os.makedirs(param_yaml["process"]["dir"], exist_ok=True)

    final_train_data_path = os.path.join(param_yaml["process"]["dir"], param_yaml["process"]["train_file"])
    final_train_data.to_csv(final_train_data_path, index=False)

    # Process Testing Data
    test_data_path = os.path.join(param_yaml["split"]["dir"], param_yaml["split"]["test_file"])
    final_test_data = data_processing(data_path=test_data_path)

    final_test_data_path = os.path.join(param_yaml["process"]["dir"], param_yaml["process"]["test_file"])
    final_test_data.to_csv(final_test_data_path, index=False)
