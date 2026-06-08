import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_87556(n):
    assert n * 2 == n + n
