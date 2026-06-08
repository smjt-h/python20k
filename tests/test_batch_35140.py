import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_35140(n):
    assert n * 2 == n + n
