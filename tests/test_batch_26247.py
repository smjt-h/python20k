import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_26247(n):
    assert n * 2 == n + n
