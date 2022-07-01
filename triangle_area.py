
def triangle_area(vertices):
    v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
    vertices = [v1,v2,v3]
    v = vertices
    A = 1/2*abs(v[1][0]*v[2][1] - v[2][0]*v[1][1] - v[0][0]*v[2][1] + v[2][0]*v[0][1] + v[0][0]*v[1][1] - v[1][0]*v[0][1])
    return A

def test_triangle_area():
    v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg
test_triangle_area()


# Kjøretest fra terminalen:
"""
PS C:\Desktop\Python> python triangle_area.py
PS C:\Desktop\Python>
"""
