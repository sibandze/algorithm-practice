import random
class Solution:
    def count_inversions(self, arr: list[int]) -> tuple[int, list[int]]:
        """
        Calculates the number of inversions in an array and returns the sorted array.

        An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].
        This method uses a modified merge sort algorithm to count inversions efficiently.

        Args:
            arr: The input list of integers.

        Returns:
            A tuple containing:
            - The total count of inversions.
            - The sorted version of the input array.
        """
        array_length = len(arr)

        # --- Helper function to count split inversions during merge ---
        def merge_and_count_split_inversions(left_half: list[int], right_half: list[int]) -> tuple[int, list[int]]:
            """
            Merges two sorted subarrays and counts the inversions between them.

            Inversions are counted when an element from the right_half is placed
            before an element from the left_half during the merge process.

            Args:
                left_half: The sorted left subarray.
                right_half: The sorted right subarray.

            Returns:
                A tuple containing:
                - The count of split inversions.
                - The merged and sorted array.
            """
            # Initialize pointers for the left and right subarrays
            left_ptr, right_ptr = 0, 0
            # Initialize count of split inversions
            split_inversions_count = 0
            # Initialize the merged array
            merged_array = []
            # Get lengths of subarrays for easier boundary checks
            len_left = len(left_half)
            len_right = len(right_half)

            # Merge the two halves while counting inversions
            while left_ptr < len_left and right_ptr < len_right:
                if left_half[left_ptr] <= right_half[right_ptr]:
                    # If element from left is smaller or equal, it's in correct order relative to right elements
                    merged_array.append(left_half[left_ptr])
                    left_ptr += 1
                else:
                    # If element from right is smaller, it forms inversions with all remaining elements in the left_half
                    merged_array.append(right_half[right_ptr])
                    right_ptr += 1
                    # The number of remaining elements in left_half is (len_left - left_ptr)
                    split_inversions_count += (len_left - left_ptr)

            # Append any remaining elements from the left half
            while left_ptr < len_left:
                merged_array.append(left_half[left_ptr])
                left_ptr += 1

            # Append any remaining elements from the right half
            while right_ptr < len_right:
                merged_array.append(right_half[right_ptr])
                right_ptr += 1

            return split_inversions_count, merged_array

        # --- Main recursive function call ---
        # Base case: An array with 0 or 1 element has no inversions and is already sorted.
        if array_length <= 1:
            return 0, arr

        # Divide the array into two halves
        mid_point = array_length // 2
        left_half_original = arr[:mid_point]
        right_half_original = arr[mid_point:]

        # Recursively count inversions in the left and right halves
        # and get the sorted versions of these halves.
        left_inversions, sorted_left_half = self.count_inversions(left_half_original)
        right_inversions, sorted_right_half = self.count_inversions(right_half_original)

        # Count inversions that span across the two halves (split inversions)
        # and get the fully merged and sorted array.
        split_inversions, merged_sorted_array = merge_and_count_split_inversions(
            sorted_left_half, sorted_right_half
        )

        # The total number of inversions is the sum of inversions within the left half,
        # within the right half, and those that span across both halves.
        total_inversions = left_inversions + right_inversions + split_inversions

        return total_inversions, merged_sorted_array

# Example Usage:
if __name__ == "__main__":
    solver = Solution()

    # Test case 1: Basic example
    test_arr1 = [2, 4, 1, 3, 5]
    print(f"Original array: {test_arr1}")
    inversions1, sorted_arr1 = solver.count_inversions(test_arr1.copy()) # Use copy to keep original intact
    print(f"Inversions: {inversions1}")
    print(f"Sorted array: {sorted_arr1}")
    # Expected inversions: (2,1), (4,1), (4,3) -> 3 inversions

    print("-" * 20)

    # Test case 2: Array with no inversions
    test_arr2 = [1, 2, 3, 4, 5]
    print(f"Original array: {test_arr2}")
    inversions2, sorted_arr2 = solver.count_inversions(test_arr2.copy())
    print(f"Inversions: {inversions2}")
    print(f"Sorted array: {sorted_arr2}")
    # Expected inversions: 0

    print("-" * 20)

    # Test case 3: Array with maximum inversions (reverse sorted)
    test_arr3 = [5, 4, 3, 2, 1]
    print(f"Original array: {test_arr3}")
    inversions3, sorted_arr3 = solver.count_inversions(test_arr3.copy())
    print(f"Inversions: {inversions3}")
    print(f"Sorted array: {sorted_arr3}")
    # Expected inversions: (5,4), (5,3), (5,2), (5,1), (4,3), (4,2), (4,1), (3,2), (3,1), (2,1) -> 10 inversions

    print("-" * 20)

    # Test case 4: Empty array
    test_arr4 = []
    print(f"Original array: {test_arr4}")
    inversions4, sorted_arr4 = solver.count_inversions(test_arr4.copy())
    print(f"Inversions: {inversions4}")
    print(f"Sorted array: {sorted_arr4}")
    # Expected inversions: 0

    print("-" * 20)

    # Test case 5: Array with one element
    test_arr5 = [42]
    print(f"Original array: {test_arr5}")
    inversions5, sorted_arr5 = solver.count_inversions(test_arr5.copy())
    print(f"Inversions: {inversions5}")
    print(f"Sorted array: {sorted_arr5}")
    # Expected inversions: 0

    print("-" * 20)

    # Test case 6: Random long array
    # Generate a random array with a length between 104 and 1015
    # and elements ranging from -105 to 105.
    random_array_length = random.randint(10**3, 10**5)
    print(f"Generating random array of len {random_array_length}...")
    test_arr6 = [random.randint(-10**5, 10**5) for _ in range(random_array_length)]
    print(f"Original array length: {len(test_arr6)}")
    inversions6, sorted_arr6 = solver.count_inversions(test_arr6.copy()) # Use copy
    print(f"Inversions: {inversions6}")
    # Verify sorting by comparing with Python's built-in sorted()
    print(f"Array sorted correctly: {sorted_arr6 == sorted(test_arr6)}")
