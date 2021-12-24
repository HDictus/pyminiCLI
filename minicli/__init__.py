"""quick and easy """
import sys
import argparse
from inspect import signature, Parameter


class ArgumentParser(argparse.ArgumentParser):
    """ArgumentParser, but with custom --help"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.help_string = "usage: "

    def print_usage(self, file=None):
        self._print_message(self.help_string, file)

    def print_help(self, file=None):
        self._print_message(self.help_string, file)


def _add_arguments(parser, parameters):
    """
    add all Parameters in parameters to the ArgumentParser parser
    and return lists of positional and keyword argument names

    :param parser: (ArgumentParser)
    :param parameters: (dict) parameter_name : Parameter
    :return: positionals (list<str>), keywords (list<str>)
    """
    positionals = []
    vararg = []
    keywords = []
    types = {}
    for name, param in parameters.items():
        if param.default != Parameter.empty:
            option_string = '--' + name
            parser.add_argument(option_string, default=param.default)
            parser.help_string += f" [{option_string} <value>] "
            keywords.append(name)
        elif param.kind == Parameter.KEYWORD_ONLY:
            option_string = '--' + name
            parser.add_argument(option_string, required=True)
            parser.help_string += f" [{option_string} <value> (required)] "
            keywords.append(name)
        elif param.kind == Parameter.VAR_POSITIONAL:
            parser.add_argument(name, nargs='*')
            parser.help_string += f"<{name}... >"
            vararg.append(name)
        else:
            parser.add_argument(name)
            parser.help_string += f" {name} "
            positionals.append(name)
        if param.annotation != param.empty:
            types[name] = param.annotation
        else:
            types[name] = str

    return positionals, vararg, keywords, types


def _get_argument(parsed_args, name, types, vararg=False):
    """Find the value of name in the parsed arguments
    casting to the annotated type if appropriate"""

    def _convert_type(typehint, value):
        try:
            return typehint(value)
        except ValueError as error:
            sys.stderr.write(str(error))
            sys.stderr.write('\n\n')
            sys.stderr.write(
                f"{value} does not represent a valid value of {name}"
                f" (could not cast to {typehint}), see above for error)")
            sys.stderr.write('\n')
            sys.exit(1)

    if vararg:
        return (_convert_type(types[name], value)
                for value in getattr(parsed_args, name))
    return _convert_type(types[name], (getattr(parsed_args, name)))


def _collect_positionals(results, positionals, types):
    return list(_get_argument(results, positional, types)
                for positional in positionals)


def _collect_varargs(results, vararg, types):
    return list(_get_argument(results, vararg[0], types, vararg=True))


def _collect_kwargs(results, keywords, types):
    return {key: _get_argument(results, key, types)for key in keywords}


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
    positionals, vararg, keywords, types = _add_arguments(
        parser, arguments
    )

    if function.__doc__:
        parser.help_string += '\n' + function.__doc__
    parser.help_string += '\n'

    results = parser.parse_args(argv)
    args = _collect_positionals(results, positionals, types)
    if vararg:
        args += _collect_varargs(results, vararg, types)
    kwargs = _collect_kwargs(results, keywords, types)

    return function(*args, **kwargs)
