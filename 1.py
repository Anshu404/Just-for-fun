def main():
    import sys
    # Increase recursion depth just in case inputs are large
    sys.setrecursionlimit(2000)
    
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        return

    # Recursively collect 'count' number of integers starting at 'start'
    def grab_values(data, start, count):
        if count == 0:
            return []
        return [data[start]] + grab_values(data, start + 1, count - 1)

    def sum_squares(arr, i=0):
        if i == len(arr):
            return 0
        
        num = int(arr[i])
        
        val = (num * num) if num >= 0 else 0
        
        return val + sum_squares(arr, i + 1)

    # Recursively solve all test cases
    def solve_case(index, remaining):
        if remaining == 0:
            return []
        
        # Basic bounds check
        if index >= len(tokens):
            return []

        try:
            count = int(tokens[index])
        except:
            return []

        # Logic to extract array and calculate
        arr = grab_values(tokens, index + 1, count)
        
        # Call the fixed function here
        total = sum_squares(arr)
        
        # Process the rest of the cases
        rest = solve_case(index + 1 + count, remaining - 1)
        
        return [str(total)] + rest

    if tokens:
        total_cases = int(tokens[0])
        results = solve_case(1, total_cases)
        print('\n'.join(results))

if __name__ == "__main__":
    main()
