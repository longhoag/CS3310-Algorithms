#Name: Long Hoang
import sys

def main():
    # Read a single line of input from stdin, which is a list of integers separated by commas
    # Example input: -2,1,-3,4,-1,2,1,-5,4
    line = sys.stdin.readline().strip()
    A = list(map(int, line.split(',')))
    
    # Initialize variables for bottom-up dp 
    current_sum = A[0]
    max_sum = A[0]
    start = 0
    end = 0
    temp_start = 0
    
    # Iterate through the array to find the max subarray
    for i in range(1, len(A)):
        # Check if starting fresh from A[i] is better
        if A[i] > current_sum + A[i]:
            current_sum = A[i]
            temp_start = i
        else:
            current_sum += A[i]
        
        # Update the global max if needed
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    # Print the maximum subarray
    print(','.join(map(str, A[start:end+1])))

if __name__ == "__main__":
    main()