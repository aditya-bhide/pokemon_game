import pickle


def pickler(file_, path, mode='wb'):
    dbfile_paths = open(path, mode)
    # source, destination
    pickle.dump(file_, dbfile_paths)
    dbfile_paths.close()


def read_pickle(path):
    """Returns file at path"""

    with open(path, 'rb') as f:
        obj = pickle.load(f)
    return obj