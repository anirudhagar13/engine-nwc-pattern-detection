"""Summary
Modules to parse json and returns configuration in format
"""
import json
from .constants import *


def parse_json(file_path: str) -> dict:
    """Summary
        Load and parse json file
    Args:
        file_path (str): path of config file
    """
    with open(file_path) as file_obj:
        return json.load(file_obj)


def verify_config(config_dict: dict) -> None:
    """Summary
        Verification of configuration received
    Args:
        config_dict (dict): config_dictionary parsed from json
    """
    must_present_configs = [lag, feature_col_names, data_file_path,
                            output_file_path, patt_len,
                            supp_threshold, crossK_threshold,
                            nc_window_len, nc_window_column_name,
                            nc_window_threshold]

    if all(param in config_dict for param in must_present_configs):
        return

    raise NameError('All Configuration not present.')


def parse_config(file_path: str) -> dict:
    """Summary
    Parses and returns configuration from json
    Args:
        file_path (str): path of config file
    """
    config_dict = parse_json(file_path)
    verify_config(config_dict)

    return config_dict
