# https://adventofcode.com/2021/day/5

with open("day05.input.txt", "r") as f:
    input = f.read().splitlines()

example_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".splitlines()


def determine_number_of_overlapping_points(lines_of_vents):
    return 0


def test_determine_number_of_overlapping_points():
    assert determine_number_of_overlapping_points(example_input) == 5