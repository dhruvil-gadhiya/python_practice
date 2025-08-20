# A function with recursion or loops is provided...

# Dry Run Toolkit: one recursive function + one loop-based function
# Toggle TRACE to False if you want students to trace by hand without seeing the logs.
TRACE = True

def _indent(d): 
    return "  " * d

# --- Recursion example: sum_to_n(n) = n + (n-1) + ... + 1 ---
def sum_to_n(n, depth=0):
    if TRACE:
        print(f"{_indent(depth)}call sum_to_n({n})")
    if n <= 1:
        if TRACE:
            print(f"{_indent(depth)}base → return {n}")
        return n
    result = n + sum_to_n(n - 1, depth + 1)
    if TRACE:
        print(f"{_indent(depth)}combine → {n} + sum_to_n({n-1}) = {result}")
    return result

# --- Loop example: Euclidean GCD (greatest common divisor) ---
def gcd(a, b):
    step = 0
    if TRACE:
        print(f"call gcd({a}, {b})")
    while b != 0:
        if TRACE:
            print(f"  step {step}: a={a}, b={b} → set a,b = b, a%b = ({b}, {a % b})")
        a, b = b, a % b
        step += 1
    if TRACE:
        print(f"stop: b=0 → return a={a}")
    return a

# --- Loop example #2: binary search (on a sorted list) ---
def binary_search(arr, x):
    lo, hi = 0, len(arr) - 1
    step = 0
    if TRACE:
        print(f"call binary_search({arr}, {x})")
    while lo <= hi:
        mid = (lo + hi) // 2
        if TRACE:
            print(f"  step {step}: lo={lo}, hi={hi}, mid={mid}, arr[mid]={arr[mid]}")
        if arr[mid] == x:
            if TRACE:
                print(f"found at index {mid}")
            return mid
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
        step += 1
    if TRACE:
        print("not found → return -1")
    return -1

if __name__ == "__main__":
    print("=== Recursion Dry Run ===")
    res1 = sum_to_n(4)         # Trace this by hand, then compare
    print("Result:", res1, "\n")

    print("=== Loop Dry Run: GCD ===")
    res2 = gcd(1071, 462)      # Classic GCD example
    print("Result:", res2, "\n")

    print("=== Loop Dry Run: Binary Search ===")
    res3 = binary_search([2, 5, 9, 12, 17, 21, 24, 31], 17)
    print("Result index:", res3)

