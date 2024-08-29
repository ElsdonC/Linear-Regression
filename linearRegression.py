class LinearRegression:
    def __init__(self, learning_rate, points, num_iterations):
        self.learning_rate = learning_rate
        self.points = points
        self.num_iterations = num_iterations

    def calculate_error(self, initial_b, initial_m):
        error = 0
        for i in range(len(self.points)):
            x, y = self.points[i][0], self.points[i][1]
            error += (y - (initial_m * x) + initial_b)**2
        error /= len(self.points)
        return error

    def gradient_descent(self, b, m):
        b, m = b, m
        for i in range(self.num_iterations):
            b, m = self.gradient_descent_step(b, m)
        return [b, m]

    def gradient_descent_step(self, b, m):
        gradient_b, gradient_m = 0, 0
        num_points = len(self.points)
        for i in range(num_points):
            x, y = self.points[i][0], self.points[i][1]
            error = (y - (m * x + b))
            gradient_b += -(2/num_points) * error
            gradient_m += -(2/num_points) * x * error
        new_b = b - (self.learning_rate * gradient_b)
        new_m = m - (self.learning_rate * gradient_m)
        return [new_b, new_m]