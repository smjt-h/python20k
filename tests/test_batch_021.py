import pytest


@pytest.mark.parametrize('n', range(1000))
def test_fast_batch_021(n):
    assert n * 2 == n + n
