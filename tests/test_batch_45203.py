import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_45203(n):
    assert n * 2 == n + n
