import numpy as np
def mean(x_list):
    s = 0
    for i in range(len(x_list)):
        s += x_list[i]/len(x_list)
    return s

x_test_values = [0.699, 0.703, 0.698, 0.688, 0.701]
def test_mean():
    expected = np.mean(x_test_values)
    computed = mean(x_test_values)
    tol = 1e-12
    success = abs(expected - computed) < tol
    msg = 'Something is wrong!'
    assert success, msg

test_mean()
