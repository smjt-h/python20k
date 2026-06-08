import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_03743(n):
    assert n * 2 == n + n
