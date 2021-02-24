"""Summary
Modules to parse json and returns configuration in format
"""
import json
from .constants import *


def parse_json(file_path):
    """Summary
        Load and parse json file
    Args:
        file_path (str): path of config file
    """
    with open(file_path) as file_obj:
        return json.load(file_obj)


def verify_config(config_dict):
    """Summary
        Verification of configuration received
    Args:
        config_dict (dict): config_dictionary parsed from json
    """
    must_present_configs = [lag, data_col_names, data_file_path, max_patt_len,
                            min_patt_len, supp_threshold, crossK_threshold,
                            num_of_bins, nw_window_len, nw_target_column,
                            nw_target_strategy, nw_target_threshold]

    if all(param in config_dict for param in must_present_configs):
        return

    raise NameError('All Configuration not present.')


def run(file_path):
    """Summary
    Parses and returns configuration from json
    Args:
        file_path (str): path of config file
    """
    config_dict = parse_json(file_path)
    verify_config(config_dict)

    return config_dict
