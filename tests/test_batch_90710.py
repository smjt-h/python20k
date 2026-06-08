import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_90710(n):
    assert n * 2 == n + n
