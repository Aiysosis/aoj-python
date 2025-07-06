import math


Point = tuple[float, float]


def main():
    n = int(input())
    sq3 = math.sqrt(3)
    cos60 = 0.5
    sin60 = sq3 / 2

    def koch(p1: Point, p2: Point) -> list[Point]:
        x1, y1 = p1
        x2, y2 = p2
        sx = x1 * 2.0 / 3.0 + x2 / 3.0
        sy = y1 * 2.0 / 3.0 + y2 / 3.0
        tx = x1 / 3.0 + x2 * 2.0 / 3.0
        ty = y1 / 3.0 + y2 * 2.0 / 3.0
        ux = sx + (cos60 * (tx - sx) - sin60 * (ty - sy))
        uy = sy + (cos60 * (ty - sy) + sin60 * (tx - sx))

        return [(sx, sy), (ux, uy), (tx, ty)]

    def do_koch(n: int, points: list[Point]):
        res: list[Point] = [points[0]]
        for i in range(n - 1):
            res = [*res, *koch(points[i], points[i + 1])]
            res.append(points[i + 1])
        return res

    points: list[Point] = [(0.0, 0.0), (100.0, 0.0)]
    while n > 0:
        points = do_koch(len(points), points)
        n -= 1
    for x, y in points:
        print(f"{x:.8f} {y:.8f}")
