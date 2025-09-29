'''
812 Largest Triangle Area
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

'''
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Function to calculate the cross product
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        # Sort the points
        points = sorted(points)

        # Calculate the convex hull
        hull = []
        for p in points:
            while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)

        t = len(hull) + 1
        for p in reversed(points):
            while len(hull) >= t and cross(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        hull.pop()  # Remove the duplicate point

        # Function to calculate the area of a triangle
        def area(a, b, c):
            return abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2.0

        # Find the maximum area triangle
        n = len(hull)
        max_area = 0
        for i in range(n):
            k = i + 2
            for j in range(i + 1, n):
                while k < n and area(hull[i], hull[j], hull[k % n]) < area(hull[i], hull[j], hull[(k + 1) % n]):
                    k += 1
                max_area = max(max_area, area(hull[i], hull[j], hull[k % n]))

        return max_area
