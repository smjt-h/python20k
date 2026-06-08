import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_70694(n):
    assert n * 2 == n + n
