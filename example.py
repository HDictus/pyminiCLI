from minicli import command

def a_function(positional1: int, *args: str, keyword_only: float, kwarg='blarg'):
    """
    a docstring
    :param positional1 (integer): the first positional argument
    :param: *args: any number of other arguments
    :param keyword_only: non-optional -- argument (a number)
    :param kwarg: an option
    """
    print("Hello!")
    print('I recieved positional: ', positional1)
    print('required keyword: ', keyword_only)
    print('other positionals: ', *args)
    print('my options are: ', kwarg)
    return

command(a_function)
# should have usage, followed by docstring as help
# all positionals should be passed in order
# all options as keywords
