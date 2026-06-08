import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_76720(n):
    assert n * 2 == n + n
