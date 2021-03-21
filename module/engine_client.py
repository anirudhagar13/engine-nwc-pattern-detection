# Runs entire flow to preprocess engine data to NWC pattern generic format
# Then it uses NWC pattern package to generate sequential patterns

import os
import argparse
import pandas as pd

from .constants import data_file_path, pass_col_name, iter_col_name
from .constants import nc_window_column_name, feature_col_names, num_of_bins
from .constants import formatted_engine_data_file, default_config_file
from .constants import nc_window_len, nc_window_threshold, seq_idx_name

from .config_parser import parse_config
from .preprocess import InvalidIndexPreprocessor
from .nc_window import MeanThresholdBinarizer
from .discretize import DenoiseDiscretizer
from .engine_data import EngineData

# Present working directory
dir_path = os.path.dirname(os.path.realpath(__file__))


def init_preprocess_strategy():
    '''
    Create instance of preprocessing strategy for the data
    '''
    # list of columns that signify same trip
    split_cols = [pass_col_name]

    # list of columns that signify continuity of taking readings
    index_cols = [iter_col_name]

    return InvalidIndexPreprocessor(split_cols, index_cols)


def init_binarize_strategy(config_dict: dict):
    '''
    Create instance of binarization strategy for anomalous window
    '''
    return MeanThresholdBinarizer(config_dict[nc_window_threshold],
                                  config_dict[nc_window_len])


def init_discretize_strategy(config_dict: dict):
    '''
    Create instance of discretization strategy for attributes
    '''
    return DenoiseDiscretizer(config_dict[num_of_bins])


def prepare_engine_data(engine_data: pd.DataFrame, config_dict: dict):
    '''
    Prepares engine data in format required by generic NWC pattern
    '''
    # Instantiating Engine data
    preprocess_strategy = init_preprocess_strategy()
    binarize_strategy = init_binarize_strategy(config_dict)
    discretize_strategy = init_discretize_strategy(config_dict)

    engine_data_inst = EngineData(
        engine_data, preprocess_strategy, discretize_strategy, binarize_strategy)

    return engine_data_inst.prepare_data(config_dict[nc_window_column_name],
                                         config_dict[feature_col_names])


def main(config_path: str):
    # parse configuration file to a hashmap
    config_dict = parse_config(dir_path + config_path)

    # reading input data file
    engine_data = pd.read_csv(
        dir_path + config_dict[data_file_path])

    print('\n', '*' * 20, ' | ',
          'Engine Data Preperation', ' | ', '*' * 20, '\n')

    # returning invalid indexes and formatted data
    invalid_seq_indexes, formatted_engine_data = prepare_engine_data(
        engine_data, config_dict)

    # Giving name to index as crucial to locating sequences
    formatted_engine_data.index.name = seq_idx_name

    # Saving intermediate data
    formatted_engine_data.to_csv(
        dir_path + formatted_engine_data_file, header=True)
    print('\n', '*' * 20, ' | ',
          'Engine Data Formatted and Saved', ' | ', '*' * 20, '\n')


if __name__ == '__main__':
    # Define the parser, to read the configuration file
    parser = argparse.ArgumentParser(
        description='Finding sequential patterns in Engine Time Series data')

    parser.add_argument('--configpath', action="store",
                        dest='configpath', default=default_config_file)
    args = parser.parse_args()

    main(args.configpath)
