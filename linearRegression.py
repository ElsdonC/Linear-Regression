def calculate_error(initial_b, initial_m, points):
    error = 0
    for i in range(len(points)):
        x, y = points[i, 0], points[i, 1]
        error += (y - (initial_m * x) + initial_b)**2
    error /= len(points)
    return error