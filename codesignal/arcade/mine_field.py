from collections import namedtuple, defaultdict
from scipy.spatial import distance

Mine = namedtuple("Mine", ["name", "x", "y", "blast_radius"])


def get_dist(x1, y1, x2, y2):
    return distance.euclidean([x1, y1], [x2, y2])


def longest_chain(mines):
    conn = defaultdict(set)

    for mine in mines:
        for otherMine in mines:
            if mine == otherMine:
                continue
            else:
                dist = get_dist(mine.x, mine.y, otherMine.x, otherMine.y)
                if dist <= mine.blast_radius:
                    conn[mine.name].add(otherMine.name)

    # Incorrect
    items = []
    mine = ""
    for k, v in conn.items():
        for i in v:
            if i not in items:
                items.append(i)
            if k not in items:
                mine = k

    return mine, len(items) + 1


# Diagram: https://i.imgur.com/xEZZQKP.png
mines = [
    Mine("A", 7, 13, 3),
    Mine("B", 6.5, 17, 5),
    Mine("C", 12, 10, 4.5),
    Mine("D", 14.5, 7, 3.5),
    Mine("E", 17, 9, 2),
    Mine("F", 7, 11, 2.5),
    Mine("G", 8.5, 11.5, 3),
]

print(longest_chain(mines))
# print(longest_chain(mines) == ('C', 6))
