def read_from_file(path):
    points = []
    with open(path, "r") as file:
        for line in file:
            row = line.strip().split()
            row = tuple([int(num) for num in row])
            points.append(row)
    return points
