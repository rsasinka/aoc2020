def load(file):
    with open(file, "r") as f:
        return [x.strip() for x in f.readlines()]


def check_slope(trees, x_path, y_path):
    max_len_x = len(trees[0])
    tree_count = 0
    x_current = 0
    for y in range(y_path, len(trees), y_path):
        x_current = (x_current + x_path) % max_len_x
        y_current = y
        if trees[y_current][x_current] == "#":
            tree_count += 1
    return tree_count


def main():
    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.

    trees = load("inpoot.txt")
    print(check_slope(trees, 1, 1) *
          check_slope(trees, 3, 1) *
          check_slope(trees, 5, 1) *
          check_slope(trees, 7, 1) *
          check_slope(trees, 1, 2))


if __name__ == '__main__':
    main()