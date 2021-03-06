# https://adventofcode.com/2021/day/2

with open("day02.input.txt", "r") as f:
    input = f.read().splitlines()

example_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()


def parse_line(line):
    instruction, raw_number = line.split(" ")
    return (instruction, int(raw_number))


def parse_commands(input):
    return list(map(parse_line, input))


def calculate_planned_course(commands):
    horizontal_position = sum(
        value for (instruction, value) in commands if instruction == "forward"
    )

    acc_up = sum(value for (instruction, value) in commands if instruction == "up")
    acc_down = sum(value for (instruction, value) in commands if instruction == "down")
    depth = acc_down - acc_up

    return (
        horizontal_position,
        depth,
    )


def calculate_planned_course_byproduct(commands):
    horizontal_position, depth = calculate_planned_course(commands)
    return horizontal_position * depth


def test_parse_commands():
    assert parse_commands(example_input) == [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]


def test_calculate_planned_course():
    assert calculate_planned_course(parse_commands("")) == (0, 0)
    assert calculate_planned_course(parse_commands(example_input)) == (15, 10)


def test_planned_course_byproduct():
    assert calculate_planned_course_byproduct(parse_commands(example_input)) == 150

    # Solve AoC 2 part 1
    assert calculate_planned_course_byproduct(parse_commands(input)) == 2091984


def calculate_planned_course_corrected(commands):
    horizontal_position = 0
    depth = 0
    aim = 0

    for (instruction, value) in commands:
        if instruction == "down":
            aim = aim + value
        elif instruction == "up":
            aim = aim - value
        elif instruction == "forward":
            horizontal_position = horizontal_position + value
            depth = depth + aim * value

    return (
        horizontal_position,
        depth,
    )


def calculate_planned_course_byproduct_corrected(commands):
    horizontal_position, depth = calculate_planned_course_corrected(commands)
    return horizontal_position * depth


def test_calculate_planned_course_corrected():
    assert calculate_planned_course_corrected(parse_commands("")) == (0, 0)
    assert calculate_planned_course_corrected(parse_commands(example_input)) == (15, 60)


def test_planned_course_byproduct_corrected():
    assert (
        calculate_planned_course_byproduct_corrected(parse_commands(example_input))
        == 900
    )

    # Solve AoC 2 part 2
    assert (
        calculate_planned_course_byproduct_corrected(parse_commands(input))
        == 2086261056
    )
