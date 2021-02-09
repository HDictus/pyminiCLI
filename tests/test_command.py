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
