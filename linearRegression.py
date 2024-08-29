import csv

class LinearRegression:
    def __init__(self, learning_rate, points, num_iterations):
        self.learning_rate = learning_rate
        self.points = points
        self.num_iterations = num_iterations

    def calculate_error(self, b, m):
        error = 0
        for i in range(len(self.points)):
            x, y = self.points[i][0], self.points[i][1]
            error += (y - (m * x) + b)**2
        error /= len(self.points)
        return error

    def gradient_descent(self, b, m):
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

if __name__ == "__main__":
    # process data
    data = None
    with open('data.csv', newline='') as csvfile:
        lines = csvfile.readlines()[1:]
        data = list(csv.reader(lines))
    for row in data:
        row[0], row[1] = float(row[0]), float(row[1])
    
    lr = LinearRegression(0.0001, data, 1500)
    initial_b, initial_m = 0, 0
    initial_error = lr.calculate_error(initial_b, initial_m)
    print(f"Before gradient descent, b = {initial_b}, m = {initial_m}, MSE = {initial_error}")
    [final_b, final_m] = lr.gradient_descent(initial_b, initial_m)
    final_error = lr.calculate_error(final_b, final_m)
    print(f"After {lr.num_iterations} iterations, b = {final_b}, m = {final_m}, MSE = {final_error}")

    studyHours = float(input("enter study hours: "))
    predictedScore = final_m * studyHours + final_b
    if predictedScore > 100:
        predictedScore = 100.00
    print(f"predicted score for studying {studyHours} hours is {predictedScore}%")