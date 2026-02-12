#  For Tests
from utils.colors import Colors
# python3 -m dir.file

def test(xyz):
    pass

#  For Tests

test_cases = [
    ("test_in", "test_out")
]


def code_runner():
    count = 0
    for test_in, test_out in test_cases:
        count+=1
        result = test(test_in)
        print(f"Test Case {count}:", f"{Colors.GREEN}PASSED" if result == test_out else f"{Colors.RED}FAILED")