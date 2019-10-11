import textwrap


def wrap(string, max_width):
    # return "\n".join(textwrap.wrap(string, max_width))
    return textwrap.fill(string, width=max_width)

string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 4

print(wrap(string, max_width))
