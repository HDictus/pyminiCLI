pyminiCLI
=====

the quickest and simplest way to specify command-line interfaces for python scripts and apps.

how it works
------------

simply call minicli.command on a function in your script, and its positional
arguments will be interpereted as command-line positionals, its keywords as
command-line options, and its docstring used to supplement the usage in
--help

If you provide type-hints for any of the arguments, the command-line inputs will
be converted to this type for you.

in example.py:
```
from minicli import command

def a_function(positional1, a_float: float, *args, keyword_only, kwarg='blarg'):
    """
    A description of the command

    Arguments:
      positional1 (integer): the first positional argument
      a_float (float): e.g. 1.5
      *args: any number of other arguments
      keyword_only: non-optional -- argument (a number)
      kwarg: an option
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
```
the result:

```
$ python example.py a 1.43 b c d e --keyword_only b --kwarg z
Hello!
I recieved positional:  a
I converted this for you: 1.43 <class 'float'>
required keyword:  b
other positionals:  b c d e
my options are:  z
$ python example.py --help
usage:  positional1  a_float <args... > [--keyword_only <value> (required)]  [--kwarg <value>] 

    A description of the command

    Arguments:
      positional1 (integer): the first positional argument
      a_float (float): e.g. 1.5
      *args: any number of other arguments
      keyword_only: non-optional -- argument (a number)
      kwarg: an option


```


Contributing
------------
If you would like to add to pyminiCLI:
 1. make an issue explaining what improvment you would like to make
 2. create a pull request

see below for ideas for what to improve

To do
-----

 - boolean options
 - error incorrectly lists varargs as required
 - one-letter flags
 - multiple named commands in the same python app
 - include type hints in --help
 - automatically include defaults in doc
 - still work if options provided before positionals

