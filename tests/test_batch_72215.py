import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_72215(n):
    assert n * 2 == n + n
