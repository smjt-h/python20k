import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_50456(n):
    assert n * 2 == n + n
