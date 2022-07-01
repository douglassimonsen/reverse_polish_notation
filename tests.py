import main
import pytest
import lark

@pytest.mark.parametrize(
    'inp,out',
    [
        ('- 1 2', -1),
        ('* 1 2', 2),
        ('+ 1 2', 3),
        ('/ 1 2', 0.5),
    ]
)
def test_int_vals(inp, out):
    assert main.main(inp) == out


@pytest.mark.parametrize(
    'inp,out',
    [
        ('- -1 2', -3),
        ('* -1 2', -2),
        ('+ 1 -2', -1),
        ('/ 1 -2', -0.5),
    ]
)
def test_negative_vals(inp, out):
    assert main.main(inp) == out


@pytest.mark.parametrize(
    'inp,out',
    [
        ('- -1.1 2', -3.1),
        ('* -1.1 2', -2.2),
        ('+ 1 -2.1', -1.1),
        ('/ 4.2 -2.1', -2.0),
    ]
)
def test_float_vals(inp, out):
    assert main.main(inp) == out


@pytest.mark.parametrize(
    'inp,out',
    [
        ('* * + 3 2 - 5 1 - 6 2', 80),
        ('* * + 3.0 2 - 5 1 - 6 2', 80),
        ('* + 3 2 - 5 1', 20),
    ]
)
def test_multi_step(inp, out):
    assert main.main(inp) == out


@pytest.mark.parametrize(
    'inp,exc',
    [
        ('* * +', lark.exceptions.UnexpectedToken),
        ('* 3 2 1', lark.exceptions.UnexpectedToken),
        ('* 3', lark.exceptions.UnexpectedToken),
        ('+ a 2', lark.exceptions.UnexpectedCharacters),
    ]
)
def test_bad_cases(inp, exc):
    with pytest.raises(exc):
        main.main(inp)