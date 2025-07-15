'''
Leetcode 2379 minimum recolors to get k consecutive black blocks
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.
In one operation, you can recolor a white block such that it becomes a black block.
Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
'''

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        i, j = 0, 0
        black_blocks_in_range = 0
        while j < k:
            black_blocks_in_range += blocks[j] == 'B'
            j+=1
        max_black_blocks_in_range = black_blocks_in_range
        
        while j < n:
            black_blocks_in_range += blocks[j] == 'B'
            black_blocks_in_range -= blocks[i] == 'B'
            i+=1
            j+=1
            if max_black_blocks_in_range < black_blocks_in_range:
                max_black_blocks_in_range = black_blocks_in_range

        return k-max_black_blocks_in_range
