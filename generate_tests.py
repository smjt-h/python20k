"""
Generates ~500,000 pytest test cases across 100,000 files.
- 20 slow tests (~10 seconds each via time.sleep), all in test_batch_00000.py
- ~500,000 fast tests (simple assertions) spread across 100,000 files,
  5 parametrized fast tests per file.
"""

import os
import shutil

TESTS_DIR = os.path.join(os.path.dirname(__file__), "tests")
NUM_FILES = 100_000
TESTS_PER_FILE = 5
SLOW_TEST_COUNT = 20
SLOW_TEST_DURATION = 10  # seconds
FILENAME_WIDTH = 5  # test_batch_00000.py .. test_batch_99999.py


def generate():
    if os.path.exists(TESTS_DIR):
        shutil.rmtree(TESTS_DIR)
    os.makedirs(TESTS_DIR)

    # __init__.py for the tests package
    open(os.path.join(TESTS_DIR, "__init__.py"), "w").close()

    # conftest.py at the root
    with open(os.path.join(TESTS_DIR, "conftest.py"), "w") as f:
        f.write("import pytest\n")

    # File 0: 20 slow tests + TESTS_PER_FILE parametrized fast tests
    slow_lines = ["import time\n", "import pytest\n", "\n\n"]
    for i in range(SLOW_TEST_COUNT):
        slow_lines.append(
            f"def test_slow_{i:03d}():\n"
            f"    time.sleep({SLOW_TEST_DURATION})\n"
            f"    assert True\n\n\n"
        )
    slow_lines.append(
        f"@pytest.mark.parametrize('n', range({TESTS_PER_FILE}))\n"
        f"def test_fast_batch_{0:0{FILENAME_WIDTH}d}(n):\n"
        f"    assert n * 2 == n + n\n"
    )
    with open(
        os.path.join(TESTS_DIR, f"test_batch_{0:0{FILENAME_WIDTH}d}.py"), "w"
    ) as f:
        f.writelines(slow_lines)

    # Files 1 .. NUM_FILES-1: TESTS_PER_FILE parametrized fast tests each
    # Pre-build the body once and only swap the function name per file.
    template = (
        "import pytest\n\n\n"
        f"@pytest.mark.parametrize('n', range({TESTS_PER_FILE}))\n"
        "def test_fast_batch_{idx}(n):\n"
        "    assert n * 2 == n + n\n"
    )
    for file_idx in range(1, NUM_FILES):
        idx_str = f"{file_idx:0{FILENAME_WIDTH}d}"
        with open(
            os.path.join(TESTS_DIR, f"test_batch_{idx_str}.py"), "w"
        ) as f:
            f.write(template.format(idx=idx_str))

    total = SLOW_TEST_COUNT + NUM_FILES * TESTS_PER_FILE
    print(f"Generated {total} tests across {NUM_FILES} files in {TESTS_DIR}/")
    print(f"  - {SLOW_TEST_COUNT} slow tests (~{SLOW_TEST_DURATION}s each)")
    print(f"  - {total - SLOW_TEST_COUNT} fast tests")


if __name__ == "__main__":
    generate()
