import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Handle empty or invalid input
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])

        # Min-heap to store cells on the current "boundary" or "water level".
        # Stores tuples: (height, row, col)
        min_heap = []

        # Visited set to keep track of cells that have been processed.
        visited = set()

        # Initialize the heap with all cells on the outer border of the heightMap.
        # These cells form the initial "walls" or boundary that can contain water.
        for r in range(m):
            # Left border
            heapq.heappush(min_heap, (heightMap[r][0], r, 0))
            visited.add((r, 0))
            # Right border
            heapq.heappush(min_heap, (heightMap[r][n-1], r, n-1))
            visited.add((r, n-1))

        for c in range(n):
            # Top border (avoid double-adding corners)
            if (0, c) not in visited:
                heapq.heappush(min_heap, (heightMap[0][c], 0, c))
                visited.add((0, c))
            # Bottom border (avoid double-adding corners)
            if (m-1, c) not in visited:
                heapq.heappush(min_heap, (heightMap[m-1][c], m-1, c))
                visited.add((m-1, c))

        # Variables to track the total trapped water volume.
        trapped_water = 0

        # Directions for BFS/neighbor exploration
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # The core logic: Process cells from the heap, expanding inwards.
        # The heap ensures we always process the lowest boundary cell first.
        while min_heap:
            # Pop the cell with the minimum height from the current "boundary".
            # This height represents the current maximum water level that can be contained
            # by the walls encountered so far.
            height, r, c = heapq.heappop(min_heap)

            # Explore neighbors of this cell.
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check if the neighbor is within bounds and has not been visited yet.
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # Mark the neighbor as visited.
                    visited.add((nr, nc))

                    # Calculate how much water this neighbor cell can trap.
                    # If the neighbor's height is less than the current boundary height ('height'),
                    # it means water can be trapped. The amount is the difference.
                    # 'height' is the water level determined by the lowest surrounding wall.
                    trapped_water += max(0, height - heightMap[nr][nc])

                    # Add the neighbor to the heap. Its "effective height" for future boundary
                    # considerations is the maximum of its own height and the current water level.
                    # This ensures that if water flows into this cell, it does so up to 'height',
                    # and this cell then acts as a new boundary at its effective height.
                    heapq.heappush(min_heap, (max(height, heightMap[nr][nc]), nr, nc))

        return trapped_water
