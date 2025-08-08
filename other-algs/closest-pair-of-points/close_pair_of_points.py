import random
import math
import sys

# --- Point Class Definition ---
class Point:
    """
    Represents a point in a 2D plane with an identifier.
    """
    def __init__(self, point_id: int, x_coord: float, y_coord: float):
        """
        Initializes a Point object.

        Args:
            point_id: A unique identifier for the point.
            x_coord: The x-coordinate of the point.
            y_coord: The y-coordinate of the point.
        """
        self.id = point_id
        self.x = x_coord
        self.y = y_coord

    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the point.
        """
        return f"({self.x:.2f},{self.y:.2f})"

    def __repr__(self) -> str:
        """
        Returns a developer-friendly string representation of the point,
        suitable for debugging.
        """
        return f"Point(id={self.id}, x={self.x}, y={self.y})"

# --- Solution Class for Closest Pair of Points ---
class Solution:
    def find_closest_pairs(self, points_data: list[tuple[float, float]]) -> tuple[Point, Point] | None:
        """
        Finds the closest pair of points in a given list of 2D points.

        This is the main entry point. It converts input tuples into Point objects,
        sorts them by X and Y coordinates ONCE, and then calls the recursive helper.

        Args:
            points_data: A list of tuples, where each tuple is (x_coordinate, y_coordinate).

        Returns:
            A tuple containing the two closest Point objects, or None if there are
            fewer than two points.
        """
        if len(points_data) < 2:
            return None

        # Convert input data into Point objects.
        point_objects = [Point(idx, x, y) for idx, (x, y) in enumerate(points_data)]

        # --- Crucial Step: Sort points by X and Y coordinates ONCE ---
        # This is done upfront to enable the efficient divide-and-conquer strategy.
        points_sorted_by_x = sorted(point_objects, key=lambda p: p.x)
        points_sorted_by_y = sorted(point_objects, key=lambda p: p.y)

        # Call the recursive helper function.
        return self._find_closest_pairs_recursive(points_sorted_by_x, points_sorted_by_y)

    def _find_closest_pairs_recursive(self, points_sorted_by_x: list[Point], points_sorted_by_y: list[Point]) -> tuple[Point, Point] | None:
        """
        Recursively finds the closest pair of points using a divide-and-conquer approach.

        This function implements the core logic, efficiently utilizing pre-sorted X and Y lists.

        Args:
            points_sorted_by_x: A list of Point objects, sorted by their x-coordinate.
            points_sorted_by_y: A list of Point objects, sorted by their y-coordinate.

        Returns:
            A tuple containing the two closest Point objects, or None if fewer than two points.
        """
        num_points = len(points_sorted_by_x)

        # --- Base Case: Brute Force for Small Subproblems ---
        if num_points <= 3:
            return self._brute_force_closest_pair(points_sorted_by_x)

        # --- Divide Step ---
        mid_index = num_points // 2
        median_point = points_sorted_by_x[mid_index] # The point at the median x-coordinate

        # Partition the Y-sorted list into two lists: left_half_y and right_half_y.
        # This is done efficiently by iterating through points_sorted_by_y once
        # and checking if each point belongs to the left or right half based on its ID
        # or by comparing its x-coordinate to the median_point's x-coordinate.
        # Using a set of IDs from the left half is a common way to do this.
        left_half_x_sorted = points_sorted_by_x[:mid_index]
        right_half_x_sorted = points_sorted_by_x[mid_index:]

        # Efficiently create Y-sorted lists for the left and right halves.
        left_half_y = []
        right_half_y = []
        # Store IDs of points in the left half for quick lookups.
        left_half_ids = {p.id for p in left_half_x_sorted}

        for p in points_sorted_by_y:
            if p.id in left_half_ids:
                left_half_y.append(p)
            else:
                right_half_y.append(p)

        # --- Conquer Step ---
        # Recursively find the closest pairs in the left and right halves.
        closest_pair_left = self._find_closest_pairs_recursive(left_half_x_sorted, left_half_y)
        closest_pair_right = self._find_closest_pairs_recursive(right_half_x_sorted, right_half_y)

        # Determine the minimum distance and best pair found so far.
        min_distance_so_far = float('inf')
        current_best_pair = None

        if closest_pair_left:
            dist_left = self._calculate_distance(closest_pair_left[0], closest_pair_left[1])
            min_distance_so_far = dist_left
            current_best_pair = closest_pair_left

        if closest_pair_right:
            dist_right = self._calculate_distance(closest_pair_right[0], closest_pair_right[1])
            if dist_right < min_distance_so_far:
                min_distance_so_far = dist_right
                current_best_pair = closest_pair_right

        # If no pair found yet (e.g., if one half had < 2 points), ensure we start with inf.
        if current_best_pair is None and num_points >= 2:
             min_distance_so_far = float('inf')


        # --- Combine Step: Check for closer pairs across the dividing line ---
        # Create a strip of points that are within 'min_distance_so_far' of the median line.
        # These points are already sorted by Y because they are filtered from points_sorted_by_y.
        points_in_strip_y_sorted = []
        for p in points_sorted_by_y:
            if abs(p.x - median_point.x) < min_distance_so_far:
                points_in_strip_y_sorted.append(p)

        # Check for closer pairs within the strip.
        closest_pair_in_strip = self._find_closest_pair_in_strip(points_in_strip_y_sorted, min_distance_so_far)

        # Update the best pair if a closer pair was found in the strip.
        if closest_pair_in_strip:
            dist_strip = self._calculate_distance(closest_pair_in_strip[0], closest_pair_in_strip[1])
            if dist_strip < min_distance_so_far:
                current_best_pair = closest_pair_in_strip

        return current_best_pair

    def _brute_force_closest_pair(self, points: list[Point]) -> tuple[Point, Point] | None:
        """
        Finds the closest pair of points using brute force.
        Suitable for small lists of points (typically <= 3).

        Args:
            points: A list of Point objects.

        Returns:
            A tuple containing the two closest Point objects, or None if fewer than two points.
        """
        min_dist_sq = float('inf') # Use squared distance to avoid sqrt until the end
        closest_pair = None
        num_points = len(points)

        if num_points < 2:
            return None

        for i in range(num_points):
            for j in range(i + 1, num_points):
                p1 = points[i]
                p2 = points[j]
                dist_sq = (p2.x - p1.x)**2 + (p2.y - p1.y)**2 # Squared distance
                if dist_sq < min_dist_sq:
                    min_dist_sq = dist_sq
                    closest_pair = (p1, p2)
        return closest_pair

    def _find_closest_pair_in_strip(self, strip_points: list[Point], current_min_distance: float) -> tuple[Point, Point] | None:
        """
        Finds the closest pair of points within a vertical strip, given that
        they are already sorted by their y-coordinates.

        Args:
            strip_points: A list of Point objects within the strip, sorted by y-coordinate.
            current_min_distance: The minimum distance found so far in the halves.

        Returns:
            A tuple containing the two closest Point objects within the strip that are
            closer than current_min_distance, or None if no such pair exists.
        """
        min_dist_sq = current_min_distance ** 2
        closest_pair = None
        strip_len = len(strip_points)

        for i in range(strip_len):
            # Check against next points within the 'current_min_distance' vertical range.
            # The inner loop limit (i + 8) ensures we check at most 7 points ahead,
            # based on the geometric proof that at most 7 points can be in the relevant box.
            for j in range(i + 1, min(i + 8, strip_len)):
                p1 = strip_points[i]
                p2 = strip_points[j]

                # Optimization: If the Y-distance alone is >= current_min_distance,
                # then the actual distance will also be greater. Break inner loop.
                if (p2.y - p1.y) ** 2 >= min_dist_sq:
                    break # Points further down in y will also be too far.

                dist_sq = (p2.x - p1.x)**2 + (p2.y - p1.y)**2
                if dist_sq < min_dist_sq:
                    min_dist_sq = dist_sq
                    closest_pair = (p1, p2)
        return closest_pair

    def _calculate_distance(self, p1: Point, p2: Point) -> float:
        """
        Calculates the Euclidean distance between two Point objects.
        """
        return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

# --- Example Usage ---
if __name__ == "__main__":
    solver = Solution()

    # Example 1: Basic test
    points_data1 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print("--- Test Case 1 ---")
    print(f"Input points: {points_data1}")
    closest_pair1 = solver.find_closest_pairs(points_data1)
    if closest_pair1:
        print(f"Closest pair: {closest_pair1[0]} and {closest_pair1[1]}")
        print(f"Distance: {solver._calculate_distance(closest_pair1[0], closest_pair1[1]):.4f}")
    else:
        print("Could not find a closest pair (need at least 2 points).")
    print("-" * 30)

    # Example 2: Points with negative coordinates and closer distance
    points_data2 = [(0, 0), (1, 1), (-1, -1), (0.5, 0.5), (2, 2)]
    print("--- Test Case 2 ---")
    print(f"Input points: {points_data2}")
    closest_pair2 = solver.find_closest_pairs(points_data2)
    if closest_pair2:
        print(f"Closest pair: {closest_pair2[0]} and {closest_pair2[1]}")
        print(f"Distance: {solver._calculate_distance(closest_pair2[0], closest_pair2[1]):.4f}")
    else:
        print("Could not find a closest pair (need at least 2 points).")
    print("-" * 30)

    # Example 3: Only two points
    points_data3 = [(1, 1), (5, 5)]
    print("--- Test Case 3 ---")
    print(f"Input points: {points_data3}")
    closest_pair3 = solver.find_closest_pairs(points_data3)
    if closest_pair3:
        print(f"Closest pair: {closest_pair3[0]} and {closest_pair3[1]}")
        print(f"Distance: {solver._calculate_distance(closest_pair3[0], closest_pair3[1]):.4f}")
    else:
        print("Could not find a closest pair (need at least 2 points).")
    print("-" * 30)

    # Example 4: Single point
    points_data4 = [(10, 10)]
    print("--- Test Case 4 ---")
    print(f"Input points: {points_data4}")
    closest_pair4 = solver.find_closest_pairs(points_data4)
    if closest_pair4:
        print(f"Closest pair: {closest_pair4[0]} and {closest_pair4[1]}")
        print(f"Distance: {solver._calculate_distance(closest_pair4[0], closest_pair4[1]):.4f}")
    else:
        print("Could not find a closest pair (need at least 2 points).")
    print("-" * 30)

    # Example 5: Empty list
    points_data5 = []
    print("--- Test Case 5 ---")
    print(f"Input points: {points_data5}")
    closest_pair5 = solver.find_closest_pairs(points_data5)
    if closest_pair5:
        print(f"Closest pair: {closest_pair5[0]} and {closest_pair5[1]}")
        print(f"Distance: {solver._calculate_distance(closest_pair5[0], closest_pair5[1]):.4f}")
    else:
        print("Could not find a closest pair (need at least 2 points).")
    print("-" * 30)

    # Example 6: Points that are on the dividing line and need strip check
    points_data6 = [(0, 0), (10, 10), (5, 4), (5, 6), (4, 5), (6, 5)]
    print("--- Test Case 6 ---")
    print(f"Input points: {points_data6}")
    closest_pair6 = solver.find_closest_pairs(points_data6)
    if closest_pair6:
        print(f"Closest pair: {closest_pair6[0]} and {closest_pair6[1]}")
        print(f"Distance: {solver._calculate_distance(closest_pair6[0], closest_pair6[1]):.4f}")
    else:
        print("Could not find a closest pair (need at least 2 points).")
    print("-" * 30)

    # Example 7: Random points (for larger scale testing)
    print("--- Test Case 7: Random Points ---")
    num_random_points = random.randint(10, 10**5)
    print(f"\r\033[KGenerating {num_random_points} random points...", end = "")
    random_points_data = [(random.uniform(-10**3, 10**3), random.uniform(-10**3, 10**3)) for _ in range(num_random_points)]
    print(f"\r\033[KGenerated {num_random_points} random points.")
    closest_pair7 = solver.find_closest_pairs(random_points_data)
    if closest_pair7:
        print(f"Closest pair found: {closest_pair7[0]} and {closest_pair7[1]}")
        print(f"Distance: {solver._calculate_distance(closest_pair7[0], closest_pair7[1]):.4f}")
    else:
        print("Could not find a closest pair (need at least 2 points).")
    print("-" * 30)
