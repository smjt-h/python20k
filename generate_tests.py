"""
Generates 30,000 pytest test cases across multiple files.
- 20 slow tests (~10 seconds each via time.sleep)
- 29,980 fast tests (simple assertions, spread across 30 files)
"""

import os
import shutil

TESTS_DIR = os.path.join(os.path.dirname(__file__), "tests")
TOTAL_TESTS = 30_000
NUM_FILES = 30
TESTS_PER_FILE = TOTAL_TESTS // NUM_FILES  # 1000
SLOW_TEST_COUNT = 20
SLOW_TEST_DURATION = 10  # seconds


def generate():
    if os.path.exists(TESTS_DIR):
        shutil.rmtree(TESTS_DIR)
    os.makedirs(TESTS_DIR)

    # __init__.py for the tests package
    with open(os.path.join(TESTS_DIR, "__init__.py"), "w") as f:
        pass

    # conftest.py at the root
    with open(os.path.join(TESTS_DIR, "conftest.py"), "w") as f:
        f.write("import pytest\n")

    # File 0: 20 slow tests + 980 parametrized fast tests
    with open(os.path.join(TESTS_DIR, "test_batch_000.py"), "w") as f:
        f.write("import time\nimport pytest\n\n\n")
        for i in range(SLOW_TEST_COUNT):
            f.write(f"def test_slow_{i:03d}():\n")
            f.write(f"    time.sleep({SLOW_TEST_DURATION})\n")
            f.write(f"    assert True\n\n\n")

        fast_count = TESTS_PER_FILE - SLOW_TEST_COUNT
        f.write(f"@pytest.mark.parametrize('n', range({fast_count}))\n")
        f.write("def test_fast_batch_000(n):\n")
        f.write("    assert n * 2 == n + n\n")

    # Files 1-29: 1000 parametrized fast tests each
    for file_idx in range(1, NUM_FILES):
        with open(os.path.join(TESTS_DIR, f"test_batch_{file_idx:03d}.py"), "w") as f:
            f.write("import pytest\n\n\n")
            f.write(f"@pytest.mark.parametrize('n', range({TESTS_PER_FILE}))\n")
            f.write(f"def test_fast_batch_{file_idx:03d}(n):\n")
            f.write(f"    assert n * 2 == n + n\n")

    print(f"Generated {TOTAL_TESTS} tests across {NUM_FILES} files in {TESTS_DIR}/")
    print(f"  - {SLOW_TEST_COUNT} slow tests (~{SLOW_TEST_DURATION}s each)")
    print(f"  - {TOTAL_TESTS - SLOW_TEST_COUNT} fast tests")


if __name__ == "__main__":
    generate()
