# Given a value of x, find f(x). Formula: f(x) = (2x)^3 + f(x-1) + f(x-3) . (When x < 10, f(x) = 1)


# test_cases: input, output

test_cases = [
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
    (8, 1),
    (9, 1),
    (10, 8002), # f(10) = (2*10)^3 + f(9) + f(7)  = 8000 + 1 + 1 = 8002
    (11, 18651), # f(11) = (2*11)^3 + f(10) + f(8) = 10648 + 8002 + 1 = 18651
    (12, 32476), # f(12) = (2*12)^3 + f(11) + f(9) = 13824 + 18651 + 1 = 32476
    (13, 58054), #  f(13) = (2*13)^3 + f(12) + f(10) =  17576 + 32476 +8002 = 58054
    (14, 98657), # f(14) = (2*14)^3 + f(13) + f(11) = 21952 + 58054 + 18651 = 98657
    (15, 158133), # f(15) = (2*15)^3 + f(14) + f(12) = 27000 + 98657 + 32476 = 158133
]


def calculate(x:int):
    if x<10:
        return 1
    return  (2*x)**3 + int(calculate(x-1)) + int(calculate(x-3))


def code_runner(test_cases:list):
    count = 0
    for test_in, test_out in test_cases:
        count +=1
        result = calculate(test_in)
        if result == test_out:
            print(f"Test Case {count}: Passed")
        else:
            print(f"Test Case {count}: Failed")
    return

code_runner(test_cases)