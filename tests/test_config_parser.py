import unittest
from module.config_parser import *

class TestConfigParser(unittest.TestCase):

    def test_parse_json(self):
        file_path = "tests/data/test_config.json"

        exp_dict = {"support_threshold": 0.004,
                    "crossK_threshold": 1,
                    "attribute_names": ["*"],
                    "lag": 1}

        self.assertDictEqual(parse_json(file_path), exp_dict)

    def test_verify_config(self):
        test_dict = {"support_threshold": 0.004,
                     "crossK_threshold": 1,
                     "attribute_names": ["*"],
                     "lag": 1}

        with self.assertRaises(NameError):
            verify_config(test_dict)


if __name__ == '__main__':
    unittest.main()
