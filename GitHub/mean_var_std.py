import numpy as np
def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    number = np.array(list).reshape([3,3])
    calculations = {
        "mean": [number.mean(0).tolist(), number.mean(1).tolist(), number.mean()],
        "variance": [number.var(0).tolist(), number.var(1).tolist(), number.var()],
        "standard deviation": [number.std(0).tolist(), number.std(1).tolist(), number.std()],
        "max": [number.max(0).tolist(), number.max(1).tolist(), number.max()],
        "min": [number.min(0).tolist(), number.min(1).tolist(), number.min()],
        "sum": [number.sum(0).tolist(), number.sum(1).tolist(), number.sum()],
    }

    return calculations
