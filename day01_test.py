# https://adventofcode.com/2021/day/1

with open("day01.input.txt", "r") as f:
    input = f.read().splitlines()

exampleInput = """199
200
208
210
200
207
240
269
260
263""".splitlines()


def map_depth_increases(measurements):
    return [
        measurements[i] > measurements[i - 1] for i in range(len(measurements)) if i > 0
    ]


def count_depth_increases(measurements):
    return len(map_depth_increases(measurements))


def test_check_depth_increases():
    assert map_depth_increases(exampleInput) == [
        # (N/A - no previous measurement)
        True,  # 200 (increased)
        True,  # 208 (increased)
        True,  # 210 (increased)
        False,  # 200 (decreased)
        True,  # 207 (increased)
        True,  # 240 (increased)
        True,  # 269 (increased)
        False,  # 260 (decreased)
        True,  # 263 (increased)
    ]


def test_count_depth_increases():
    assert count_depth_increases(exampleInput) == 7
