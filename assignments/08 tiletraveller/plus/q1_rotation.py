def find_width(lines):
    """Finds the minimum width required to fit all the lines."""

    max_length = 0
    for line in lines:
        if len(line) > max_length:
            max_length = len(line)

    return max_length


def rotate_text_clockwise(text):
    """Rotates text 90 degrees clockwise, adding spaces as needed for multi-line strings."""

    lines = text.splitlines()
    width = find_width(lines)

    rotated_text = ""
    for character_index in range(width):
        for line in reversed(lines):
            if len(line) > character_index:
                character_to_add = line[character_index]
            else:
                character_to_add = " "

            rotated_text += character_to_add

        rotated_text += "\n"

    return rotated_text.rstrip("\n")
