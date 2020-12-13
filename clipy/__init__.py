"""quick and easy """
import sys
import argparse
from inspect import signature, Parameter


class ArgumentParser(argparse.ArgumentParser):
    """ArgumentParser, but with custom --help"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.help_string = "usage: "

    # pylint: disable=signature-differs
    def print_usage(self, file):
        self._print_message(self.help_string)

    # pylint: disable=signature-differs
    def print_help(self, file):
        self._print_message(self.help_string)


def _add_arguments(parser, parameters):
    """
    add all Parameters in parameters to the ArgumentParser parser
    and return lists of positional and keyword argument names

    :param parser: (ArgumentParser)
    :param parameters: (dict) parameter_name : Parameter
    :return: positionals (list<str>), keywords (list<str>)
    """
    positionals = []
    keywords = []
    for name, param in parameters.items():
        if param.default != Parameter.empty:
            option_string = '--' + name
            parser.add_argument(option_string, default=param.default)
            parser.help_string += f" [{option_string} <value>] "
            keywords.append(name)
        else:
            parser.add_argument(name)
            parser.help_string += f" {name} "
            positionals.append(name)
    return positionals, keywords


def command(function, argv=None):
    """
    run this function as a command-line command, automatically converting
    the positional and keyword arguments to command line arguments and
    options as needed


    :param function: the function to run
    :param args: (for testing purposes), arguments to run on.
        uses sys.argv by default
    :return: None
    """
    if argv is None:
        argv = sys.argv[1:]

    arguments = signature(function).parameters
    parser = ArgumentParser()
    positionals, keywords = _add_arguments(
        parser, arguments
    )

    if function.__doc__:
        parser.help_string += '\n' + function.__doc__
    parser.help_string += '\n'

    results = parser.parse_args(argv)
    args = (getattr(results, positional) for positional in positionals)
    kwargs = {key: getattr(results, key) for key in keywords}
    return function(*args, **kwargs)
