# Constants across package (Due to sharing b/w modules)

# configuration related constants
lag = "lag"
feature_col_names = "attribute_names"
data_file_path = "data_file_path"
max_patt_len = "max_pattern_length"
min_patt_len = "min_pattern_length"
supp_threshold = "support_threshold"
crossK_threshold = "crossK_threshold"
num_of_bins = "number_of_discretizer_bins"
nc_window_len = "anomalous_window_length"
nc_window_column_name = "anomalous_target_column"
nc_window_strategy = "anomalous_window_strategy"
nc_window_threshold = "anomalous_window_threshold"

# Data related constants
pass_col_name = 'pass'
iter_col_name = 'Iteration'
target_col_name = 'NCWindow'
seq_idx_name = 'SeqIndex'

# File IO related constants
default_config_file = '/data/default_config.json'
formatted_engine_data_file = '/data/formatted_engine_data.csv'
