Linear Regression from Scratch in Python

## Formulas Utilized
Mean Squared Error: 
### $\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$
Gradient with respect to parameter b:
### $\frac{\partial J}{\partial b} = -\frac{2}{n} \sum_{i=1}^{n} \left( y_i - (m \cdot x_i + b) \right)$
Gradient with respect to parameter m:
### $\frac{\partial J}{\partial m} = -\frac{2}{n} \sum_{i=1}^{n} x_i \cdot \left( y_i - (m \cdot x_i + b) \right)$
#
## Execution
To run this program, run the `linearRegression.py` file using Python:
```
python linearRegression.py
```
The output should look like this:
```
Before gradient descent, b = 0, m = 0, MSE = 3537.6041666666665
After 1500 iterations, b = 1.5682323364405246, m = 9.947097998639563, MSE = 21.73348156771939
enter study hours: 
```