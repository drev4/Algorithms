# Given an integer array and a window of size w
# Find the current maximum value in the window as it slides through the entire array.

# Space Complexity O(w) window size.
# Time complexity O(n) array length.
from collections import deque


def find_max_sliding_window(nums, window_size):
    result = []
    # If there is not any num return an empty array
    if not nums:
        return result

    # If window size is greater than nums arrays length then the window size is the full array
    if window_size > len(nums):
        window_size = len(nums)

    # Initializing doubly ended queue for storing indices
    window = deque()

    # Find out the first maximum value in the window
    for i in range(window_size):
        # For every element, remove the previous smaller elements from window
        while window and nums[i] >= nums[window[-1]]:
            window.pop()

        # Add current element at the back of the queue
        window.append(i)
    # Appending the largest element in the window to the result
    result.append(nums[window[0]])

    for i in range(window_size, len(nums)):
        # remove all numbers that are smaller than current number
        # from the tail of list
        while window and nums[i] >= nums[window[-1]]:
            window.pop()

        # Remove first index from the window deque if
        # it doesn't fall in the current window anymore
        if window and window[0] <= (i - window_size):
            window.popleft()

        # Add current element at the back of the queue
        window.append(i)
        result.append(nums[window[0]])

    return result


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    window = 3
    result = find_max_sliding_window(array, window)
    print(result)
