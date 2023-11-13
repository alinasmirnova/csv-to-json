import importlib
import importlib.resources


def get_test_data_path(package_name, file_name):
    return str(importlib.resources.files(package_name).joinpath(f'test_data/{file_name}'))
