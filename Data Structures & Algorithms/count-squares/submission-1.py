from collections import defaultdict

class CountSquares:

    def __init__(self):
        
        self.pts_count = defaultdict(int)
        
        self.x_to_ys = defaultdict(set)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.pts_count[(x, y)] += 1
        self.x_to_ys[x].add(y) 

    def count(self, point: list[int]) -> int:
        res = 0
        px, py = point

        
        for y in self.x_to_ys[px]:
            if y == py:
                continue
            
            side_len = abs(py - y)
            
            
            for x in (px + side_len, px - side_len):
                if (x, py) in self.pts_count and (x, y) in self.pts_count:
                    res += (
                        self.pts_count[(px, y)] *
                        self.pts_count[(x, py)] *
                        self.pts_count[(x, y)]
                    )

        return res