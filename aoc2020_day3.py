def get_tree_count(hillside, down_slope, cross_slope):
    tree_count = 0
    h_pos = 0
    hill_width = len(hillside[0])

    for v_pos in range(down_slope, len(hillside), down_slope) :
        hill_contour = hillside[v_pos]
        h_pos = (h_pos+cross_slope)%hill_width
        hill_pos = hill_contour[h_pos]
        if hill_pos == '#':
            tree_count += 1

    return tree_count


def solve(part):
    hillside = []
    data = open('data/day3-input.txt', 'r').read().split('\n') # read the file
    for line in data:
        hillside.append(line)

    if part == 1:
        slopes = [(1,3)]
        tree_count = 0
        for (down_slope, cross_slope) in slopes:
            tree_count = tree_count + get_tree_count(hillside, down_slope, cross_slope)
        
        print("Number of trees = ", tree_count)

    if part == 2:
        slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
        tree_product = 1

        for (down_slope, cross_slope) in slopes:
            tree_count = get_tree_count(hillside, down_slope, cross_slope)
            tree_product = tree_product * tree_count
        
        print("Product of trees = ", tree_product)

