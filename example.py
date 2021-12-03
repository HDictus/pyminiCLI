from minicli import command

def a_function(positional1, a_float: float, *args, keyword_only, kwarg='blarg'):
    """
    a docstring
    :param positional1 (integer): the first positional argument
    :param: *args: any number of other arguments
    :param keyword_only: non-optional -- argument (a number)
    :param kwarg: an option
    """
    print("Hello!")
    print('I recieved positional: ', positional1)
    print("I converted this for you:", a_float, type(a_float))
    print('required keyword: ', keyword_only)
    print('other positionals: ', *args)
    print('my options are: ', kwarg)
    return

command(a_function)
# should have usage, followed by docstring as help
# all positionals should be passed in order
# all options as keywords
