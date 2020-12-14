pyminiCLI
=====

the quickest and simplest way to specify command-line interfaces for python scripts and apps.

how it works
------------

simply call minicli.command on a function in your script, and its positional
arguments will be interpereted as command-line positionals, its keywords as
command-line options, and its docstring used to supplement the usage in
--help

in example.py:
```
    from minicli import command


    def a_function(positional1, positional2, kwarg='blarg'):
        """
        a docstring
        :param positional1:
        :param positional2:
        :param kwarg:
        :return:
        """
        print("Hello!")
        print('my positionals are: ', positional1, positional2)
        print('my options are: ', kwarg)
        return

    command(a_function)
```
the result:

```
   $ python3 example.py an_argument another_argument --kwarg optional_argument
   ['positional1', 'positional2']
   ['kwarg']
   Hello!
   my positionals are:  an_argument another_argument
   my options are:  optional_argument
   
   $ python3 example.py --help
   usage:  positional1  positional2  [--kwarg <value>] 

   a docstring
   :param positional1:
   :param positional2:
   :param kwarg:
   :return:
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
 - one-letter flags
 - multiple named commands in the same python app
 - include type hints in --help
 - cast arguments to type hint types
 - *args
 - **kwargs
