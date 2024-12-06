#Name: Long Hoang
import sys

def findMaxCrossingSubarray(A, low, mid, high):
    # Find the maximum subarray sum that ends at or before 'mid', scanning towards the left.
    left_sum = float('-inf')
    sum_ = 0
    max_left = mid
    for i in range(mid, low-1, -1):
        sum_ += A[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i

    # Find the maximum subarray sum that starts at or after 'mid+1', scanning towards the right.
    right_sum = float('-inf')
    sum_ = 0
    max_right = mid + 1
    for j in range(mid+1, high+1):
        sum_ += A[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j

    # The combined max crossing subarray sum is the sum of these two maxima.
    return (max_left, max_right, left_sum + right_sum)

def findMaximumSubarray(A, low, high):
    # Base case: If the array considered has only one element, that's the max subarray.
    if low == high:
        return (low, high, A[low])

    # Find the midpoint to divide the array into two halves.
    mid = (low + high) // 2

    # Recursively find the maximum subarray in the left half (A[low..mid]).
    left_low, left_high, left_sum = findMaximumSubarray(A, low, mid)
    # Recursively find the maximum subarray in the right half (A[mid+1..high]).
    right_low, right_high, right_sum = findMaximumSubarray(A, mid+1, high)
    # Find the maximum subarray that crosses the midpoint.
    cross_low, cross_high, cross_sum = findMaxCrossingSubarray(A, low, mid, high)

    # Compare the three results: left, right, and crossing subarrays.
    # Return the one with the largest sum.
    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)


def main():
    # Read a single line of input from stdin.
    line = sys.stdin.readline().strip()
    # Convert the comma-separated string into a list of integers.
    A = list(map(int, line.split(',')))

    # Compute the maximum subarray for the entire array A.
    low, high, max_sum = findMaximumSubarray(A, 0, len(A)-1)

    # Print the maximum subarray (from A[low] to A[high]) as comma-separated values.
    # Example output: "4,-1,2,1"
    print(','.join(map(str, A[low:high+1])))

if __name__ == "__main__":
    main()