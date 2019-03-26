import pickle
import inspect


def pickle_dump(variable):
    with open('pickle/{}.pk'.format(_retrieve_name(variable)), 'wb') as f:
        pickle.dump(variable, f)


def pickle_load(var_name):
    with open('pickle/{}.pk'.format(var_name), 'rb') as f:
        return pickle.load(var_name, f)


def _retrieve_name(var):
    """
    Retrieves var name in string
    """
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var][0]

