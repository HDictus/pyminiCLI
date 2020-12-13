import sys
import argparse
from inspect import signature, Parameter


class ArgumentParser(argparse.ArgumentParser):
    """ArgumentParser, but with custom --help"""

    def __init__(self, *args, **kwargs):
        super(ArgumentParser, self).__init__(*args, **kwargs)
        self.help_string = "usage: "

    def print_usage(self, *args):
        self._print_message(self.help_string)

    def print_help(self, *args):
        self._print_message(self.help_string)


def command(function, args=None):
    """
    run this function as a command-line command, automatically converting
    the positional and keyword arguments to command line arguments and
    options as needed


    :param function: the function to run
    :param args: (for testing purposes), arguments to run on.
        uses sys.argv by default
    :return: None
    """
    if args is None:
        args = sys.argv[1:]
    parameters = signature(function).parameters
    parser = ArgumentParser()
    positionals = []
    kwargs = []
    for name, param in parameters.items():
        if param.default != Parameter.empty:
            option_string = '--' + name
            parser.add_argument(option_string, default=param.default)
            parser.help_string += f" [{option_string} <value>] "
            kwargs.append(name)
        else:
            parser.add_argument(name)
            parser.help_string += f" {name} "
            positionals.append(name)

    if function.__doc__:
        parser.help_string += '\n' + function.__doc__
    parser.help_string += '\n'
    results = parser.parse_args(args)
    print(positionals)
    print(kwargs)
    posn = (getattr(results, positional) for positional in positionals)
    kwarg = {key: getattr(results, key) for key in kwargs}
    return function(*posn, **kwarg)