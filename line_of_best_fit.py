import numpy as np

def best_fit_line(data):
    
    x = np.array(list(data.keys()))
    y = np.array(list(data.values()))

    
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    
    m = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
    c = y_mean - m * x_mean

    
    return f"y = {m:.2f}x + {c:.2f}"


data = {}


equation = best_fit_line(data)
print("Equation of the line of best fit:", equation)
