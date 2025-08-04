class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return str(self)
class Solution:
    def closest_pairs(self, points):
        points_ = []
        for idx, p in enumerate(points):
            points_.append(Point(idx, p[0], p[1]))
        return self._closest_pairs(points_)
    def _closest_pairs(self, points):
        def distance(p1, p2):
            return ((p2.x-p1.x)**2+(p2.y-p1.y)**2)**0.5
        def closest_pair_split(p_x, p_y, d):
            n = len(p_x)
            x_ = p_x[n//2].x
            s_y = []
            min_max = (x_-d, x_+d)
            for i in range(n):
                p = p_y[i]
                if min_max[0] <= p.x <= min_max[1]:
                    s_y.append(p)
            best_d, best_pair = d, None
            #print(len(s_y))
            for i in range(len(s_y)):
                for j in range(i+1, min(7+i, len(s_y))):
                    p, q = s_y[i], s_y[j]
                    d_pq = distance(p, q)
                    if d_pq < best_d:
                        best_d = d_pq
                        best_pair = (p, q)
            return best_pair
        def closest_pairs(p_x, p_y):
            n = len(p_x)
            if n <= 3:
                min_d = float("inf")
                pair = None
                for i in range(n):
                    for j in range(i+1, n):
                        d = distance(p_x[i], p_x[j])
                        if d < min_d:
                            min_d = d
                            pair = (p_x[i], p_x[j])
                return pair
            half_n = n//2
            left_x = []
            left_ids = set()
            right_x = []
            for i in range(n):
                p = p_x[i]
                if i < half_n:
                    left_x.append(p)
                    left_ids.add(p.id)
                else:
                    right_x.append(p)
            left_y = []
            right_y = []
            for i in range(n):
                p = p_y[i]
                if p.id in left_ids:
                    left_y.append(p)
                else:
                    right_y.append(p)
                
            pair1 = closest_pairs(left_x, left_y)
            d1 = float("inf")
            if pair1 != None:
                d1 = distance(pair1[0], pair1[1])
            pair2 = closest_pairs(right_x, right_y)
            d2 = float("inf")
            if pair2 != None:
                d2 = distance(pair2[0], pair2[1])
            if d1 <= d2:
                d = d1
                best_pair = pair1
            else:
                d = d2
                best_pair = pair2
            split_pair = closest_pair_split(p_x, p_y, d)
            
            return best_pair if split_pair == None else split_pair

        p_x = sorted(points, key = lambda point: point.x)
        p_y = sorted(points, key = lambda point: point.y)

        return closest_pairs(p_x, p_y)
