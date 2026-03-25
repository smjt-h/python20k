import time
import pytest


def test_slow_000():
    time.sleep(10)
    assert True


def test_slow_001():
    time.sleep(10)
    assert True


def test_slow_002():
    time.sleep(10)
    assert True


def test_slow_003():
    time.sleep(10)
    assert True


def test_slow_004():
    time.sleep(10)
    assert True


def test_slow_005():
    time.sleep(10)
    assert True


def test_slow_006():
    time.sleep(10)
    assert True


def test_slow_007():
    time.sleep(10)
    assert True


def test_slow_008():
    time.sleep(10)
    assert True


def test_slow_009():
    time.sleep(10)
    assert True


def test_slow_010():
    time.sleep(10)
    assert True


def test_slow_011():
    time.sleep(10)
    assert True


def test_slow_012():
    time.sleep(10)
    assert True


def test_slow_013():
    time.sleep(10)
    assert True


def test_slow_014():
    time.sleep(10)
    assert True


def test_slow_015():
    time.sleep(10)
    assert True


def test_slow_016():
    time.sleep(10)
    assert True


def test_slow_017():
    time.sleep(10)
    assert True


def test_slow_018():
    time.sleep(10)
    assert True


def test_slow_019():
    time.sleep(10)
    assert True


@pytest.mark.parametrize('n', range(980))
def test_fast_batch_000(n):
    assert n * 2 == n + n
