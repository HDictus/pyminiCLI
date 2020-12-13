CLIpy
=====

the quickest and simplest way to run python as a command line app

how it works
------------

simply call clipy.command on a function in your script, and its positional
arguments will be interpereted as command-line positionals, its keywords as
command-line options, and its docstring used to supplement the usage in
--help

.. code:: python
    from clipy import command


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

.. code: bash

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



Contributing
------------
If you would like to add to clipy:
 1. make an issue explaining what improvment you would like to make
 2. create a pull request

see below for ideas for what to improve

To do
-----

 - boolean options
 - one-letter flags
 - include type hints in --help
 - cast arguments to type hint types
 - *args
 - **kwargs
