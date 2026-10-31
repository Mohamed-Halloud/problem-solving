class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

    # Maintain a max heap
        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            # Find the largest among root, left child, right child
            if left < n and nums[left] > nums[largest]:
                largest = left

            if right < n and nums[right] > nums[largest]:
                largest = right

            # If a child is larger, swap and continue heapifying
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        # Step 1: Build a max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # Step 2: Move the maximum to the end
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)

        return nums


    




        