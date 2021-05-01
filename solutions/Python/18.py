def collapse_tree_bottom_up(tree) -> int:
    tree_copy = tree.copy()
    for row_idx, row in reversed(list(enumerate(tree[:-1]))):
        for col_idx, node in enumerate(row):
            next_row = tree[row_idx + 1]
            tree_copy[row_idx][col_idx] = node + \
                max(next_row[col_idx], next_row[col_idx + 1])

    return tree_copy[0][0]


def parse_tree() -> list:
    with open('./inputs/18.txt', 'r') as f:
        return [list(map(int, row.split(' '))) for row in f.read().split('\n')]


if __name__ == "__main__":
    tree = parse_tree()
    max_total = collapse_tree_bottom_up(tree)
    print(max_total)
