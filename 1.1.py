import sys
from itertools import islice

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    data_iterator = iter(input_data)

    try:
        # The first integer is N (number of test cases)
        num_test_cases = int(next(data_iterator))
    except StopIteration:
        return

    def process_case(_):
        try:
            count = int(next(data_iterator))
            
            numbers = map(int, islice(data_iterator, count))
            
            return sum(map(lambda x: x*x, filter(lambda x: x >= 0, numbers)))
        except StopIteration:
            return 0

    results = map(process_case, range(num_test_cases))

    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve()
