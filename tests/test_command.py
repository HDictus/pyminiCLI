import pytest
from minicli import command


def test_no_args(capfd):
    check = dict(ok=False)

    def no_args():
        """docstring"""
        check['ok'] = True
        return

    command(no_args, argv=[])
    assert check['ok']
    with pytest.raises(SystemExit) as se:
        command(no_args, argv=['an arg'])


def test_positionals_and_kwargs(capfd):
    check = dict(called=False)

    def with_args(arg1, arg2, kwarg1='yes', kwarg2='no'):
        """docstring"""
        check['called'] = (arg1, arg2, kwarg1, kwarg2)
        return

    with pytest.raises(SystemExit) as se:
        command(with_args, argv=[])

    command(with_args, argv=['avalue', 'another'])
    assert check['called'] == ('avalue', 'another', 'yes', 'no')
    command(with_args, argv=['avalue', 'another', '--kwarg1', 'indeed'])
    assert check['called'] == ('avalue', 'another', 'indeed', 'no')


def test_help(capfd):

    def test_fun():
        """just some help"""
        return
    with pytest.raises(SystemExit):
        command(test_fun, argv=["--help"])

def test_var_args():
    called_with = []

    def test_fun(*args):
        for a in args:
            called_with.append(a)
        return

    command(test_fun, argv=['a', 'bunch', 'of', 'args'])
    assert called_with == ['a', 'bunch', 'of', 'args']


def test_var_args_not_at_end():
    a_val = []
    b_val = []
    args_val = []

    def test_fun(a, *args, b):
        a_val.append(a)
        b_val.append(b)
        for arg in args:
            args_val.append(arg)
        return

    command(test_fun, argv=['A', 'args', 'more-args', '--b', 'B'])
    assert a_val == ['A']
    assert b_val == ['B']
    assert args_val == ['args', 'more-args']
    with pytest.raises(SystemExit):
        command(test_fun, argv=['A', 'args', 'more-args', 'B'])