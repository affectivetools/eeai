import operator
import dask.dataframe as dd
import multiprocessing as mp
from multiprocessing import Pool
from sklearn.model_selection import train_test_split


def df_parallel_column_apply(df, func, column_name):
    """ TODO make it work with grouped objects as df."""
    n_partitions = mp.cpu_count() * 4
    d_data = dd.from_pandas(df, npartitions=n_partitions)

    res =\
    d_data.map_partitions(lambda df: df.apply((lambda row: func(row[column_name])), axis=1))\
    .compute(scheduler='processes')

    return res


def iterate_in_chunks(l, n):
    """Yield successive 'n'-sized chunks from iterable 'l'.
    Note: last chunk will be smaller than l if n doesn't divide l perfectly.
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]


def parallel_apply(iterable, func, n_processes=None):
    """ Apply func in parallel to chunks of the iterable based on multiple processes.
    :param iterable:
    :param func: simple function that does not change the state of global variables.
    :param n_processes: (int) how many processes to split the data over
    :return:
    """
    n_items = len(iterable)
    if n_processes is None:
        n_processes = min(4 * mp.cpu_count(), n_items)
    pool = Pool(n_processes)
    chunks = int(n_items / n_processes)
    res = []
    for data in pool.imap(func, iterable, chunksize=chunks):
        res.append(data)
    pool.close()
    pool.join()
    return res


def sort_dict_by_val(in_dict, reverse=False):
    return sorted(list(in_dict.items()), key=operator.itemgetter(1), reverse=reverse)


def sort_dict_by_key(in_dict, reverse=False):
    return sorted(list(in_dict.items()), key=operator.itemgetter(0), reverse=reverse)


def make_train_test_val_splits(df, loads, random_seed, split_column='target', verbose=True):
    """ Split the data into train/val/test.
    :param df: pandas Dataframe, contains the dataframe that will be split into train/test/val
    :param split_column: (string, corresponding to one column of the df)
        elements that have the same value over these columns will be in DIFFERENT splits.
    :param loads: list with the three floats summing to one for train/val/test, e.g., [0.8, 0.1, 0.1]
    :param random_seed: int
    :return: changes the df in-place to include a column indicating the "split" of each row
    """
    if sum(loads) < 10e-5:
        raise ValueError('Split loads must sum to 1.')

    train_size, val_size, test_size = loads
    if verbose:
        print("Using a {},{},{} for train/val/test purposes".format(train_size, val_size, test_size))

    ## unique id
    unique_id = df[split_column]
    unique_ids = unique_id.unique()
    unique_ids.sort()

    train, rest = train_test_split(unique_ids, test_size=val_size+test_size, random_state=random_seed)
    train = set(train)

    if val_size != 0:
        val, test = train_test_split(rest, test_size=round(test_size*len(unique_ids)), random_state=random_seed)
    else:
        test = rest
    test = set(test)
    assert len(test.intersection(train)) == 0

    def mark_example(x):
        if x in train:
            return 'train'
        elif x in test:
            return 'test'
        else:
            return 'val'

    df['split'] = unique_id.apply(mark_example)
    return df


class TerminalTextColor:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'