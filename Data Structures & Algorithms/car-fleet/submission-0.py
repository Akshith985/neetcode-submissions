class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l=[]
        cars = sorted(zip(position, speed), reverse=True)
        for p, s in cars:
            res = (target - p) / s
            if l:
                if res>l[-1]:
                    l.append(res)
                else:
                    continue
            else:
                l.append(res)
        return len(l)