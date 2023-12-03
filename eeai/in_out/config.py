"""
See: https://jonnyjxn.medium.com/how-to-config-your-machine-learning-experiments-without-the-headaches-bb379de1b957
"""
import yaml


def _collect_all_items(in_dict, prefix=""):
        all_found = []
        for key, val in in_dict.items():
            if type(val) is dict:
                all_found.extend(_collect_all_items(in_dict[key], prefix + key + '/' ))
            else:
                all_found.append(prefix + key)

        return all_found


class Config(object):
    """Simple dict wrapper that adds a thin API allowing for slash-based (/) retrieval of
    nested elements, e.g. cfg.get_config("meta/dataset_name")
    """
    def __init__(self, config_path=None):

        if config_path is not None:
            with open(config_path) as cf_file:
                cfg = yaml.safe_load(cf_file.read())
        else:
            cfg = dict()

        self._data = cfg

    def get(self, path=None, default=None):
        """
        E.g.,   n_hidden_layers = cfg.get('experiment/model/n_layers', 36)

        Args:
            path: specify the nested dictionary with each nested dictionary given by /
            default: if the path does not lead to an existing value, return the default
        Returns:
            the stored value or the default
        """

        # we need to deep-copy self._data to avoid over-writing its data
        recursive_dict = dict(self._data)

        if path is None:
            return recursive_dict

        path_items = path.split("/")[:-1]
        data_item = path.split("/")[-1]

        try:
            for path_item in path_items:  # try to reach the final dictionary from which you will get the value.
                recursive_dict = recursive_dict.get(path_item)

            value = recursive_dict.get(data_item, default)

            return value
        except (TypeError, AttributeError):
            return default

    def list_all_items(self):
        return _collect_all_items(self._data)

    def __str__(self):
        final_str = ""
        for item in self.list_all_items():
            final_str += item + "\n"
        return final_str

    def __getitem__(self, item):
        return self.get(item)