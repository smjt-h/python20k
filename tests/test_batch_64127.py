import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_64127(n):
    assert n * 2 == n + n
