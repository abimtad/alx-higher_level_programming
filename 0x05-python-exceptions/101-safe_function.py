#!/usr/bin/python3

def safe_function(fct, *args):
    """Excutes a functions safely

    Args:
        fct (function): the function to excute
        args (key word arg): argument for fct

    Returns:
        the result of the function or None
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
