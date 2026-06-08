import pytest


@pytest.mark.parametrize('n', range(5))
def test_fast_batch_29333(n):
    assert n * 2 == n + n
