# Runs entire flow to preprocess engine data to NWC pattern generic format
# Then it uses NWC pattern package to generate sequential patterns

import os
import argparse
import pandas as pd

from .constants import *

from nwc_pattern_miner import mine_sequence_patterns

from .config_parser import parse_config
from .preprocess import InvalidIndexPreprocessor
from .nc_window import MeanThresholdBinarizer
from .discretize import ManualDiscretizer, DenoiseDiscretizer
from .engine_data import EngineData

# Present working directory
dir_path = os.path.dirname(os.path.realpath(__file__))


def init_preprocess_strategy(config_dict: dict):
    '''
    Create instance of preprocessing strategy for the data
    '''
    # list of columns that signify same trip
    split_cols = config_dict[split_columns]

    # list of columns that signify continuity of taking readings
    index_cols = config_dict[index_columns]

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
    if config_dict[discretization_type] == manual_discrete_strategy:
        return ManualDiscretizer(config_dict[feature_col_names],
                                 config_dict[feature_min_values],
                                 config_dict[feature_bin_intervals])
    else:
        # auto-denoising
        return DenoiseDiscretizer(config_dict[n_bins])


def prepare_engine_data(engine_data: pd.DataFrame, config_dict: dict):
    '''
    Prepares engine data in format required by generic NWC pattern
    '''
    # Instantiating Engine data
    preprocess_strategy = init_preprocess_strategy(config_dict)
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

    # Mining NWC Patterns
    column_names = config_dict[feature_col_names] + [target_col_name]
    output_df = mine_sequence_patterns(formatted_engine_data[column_names],
                                       target_col_name,
                                       config_dict[supp_threshold],
                                       config_dict[crossK_threshold],
                                       config_dict[patt_len],
                                       lag=config_dict[lag],
                                       invalid_seq_indexes=invalid_seq_indexes,
                                       output_type=config_dict[output_type],
                                       topk=config_dict[topk],
                                       pruning_type=config_dict[pruning_type])
    output_df.to_csv(
        dir_path + config_dict[output_file_path], header=True, index=False)
    print('\n', '*' * 20, ' | ',
          'Engine Patterns Mined and Saved', ' | ', '*' * 20, '\n')


if __name__ == '__main__':
    # Define the parser, to read the configuration file
    parser = argparse.ArgumentParser(
        description='Finding sequential patterns in Engine Time Series data')

    parser.add_argument('--configpath', action="store",
                        dest='configpath', default=default_config_file)
    args = parser.parse_args()

    main(args.configpath)
