import sklearn.model_selection import train_test_split

def train_dev_test_split(*arrays, **options):

    dev_size = options.pop('dev_size', 'default')
    test_size = options.pop('test_size', 'default')

    if dev_size == 'default':
        dev_size = 0.25

    if test_size == 'default':
        test_size = 0.25

    train_set, test_dev_set = train_test_split(*arrays, **dict(**options, test_size = dev_size + test_size))
    test_set, dev_set = train_test_split(*arrays, **dict(**options, test_size = dev_size / (dev_size + test_size)))

    return [train_set, test_set, dev_set]