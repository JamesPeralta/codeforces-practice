"""
We place a king and queen and we have to fork them

"""

def iterate_pos(row, col, a, b):
    attacks = [
        # attack forward
        (row - a, col + b),
        (row - a, col - b),
        # attack right
        (row - b, col + a),
        (row + b, col + a),
        # Attack down
        (row + a, col + b),
        (row + a, col - b),
        # Attack left
        (row - b, col - a),
        (row + b, col - a),
    ]
    return attacks

tests = int(input())

for _ in range(tests):
    first = input().split()
    second = input().split()
    third = input().split()

    a, b = int(first[0]), int(first[1])
    k_x, k_y = int(second[0]), int(second[1])
    q_x, q_y = int(third[0]), int(third[1])

    result = set()
    for x, y in iterate_pos(k_x, k_y, a, b):
        for cand_x, cand_y in iterate_pos(x, y, a, b):
            if cand_x == q_x and cand_y == q_y:
                result.add((x, y))
                break

    print(len(result))