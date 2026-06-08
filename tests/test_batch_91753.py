import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_91753(n):
    assert n * 2 == n + n
