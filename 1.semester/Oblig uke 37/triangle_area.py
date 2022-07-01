
def triangle_area(vertices):        # Funksjon for Arealet av en triangel basert på punkter
    v1 = [0,0]; v2 = [1,0]; v3 = [0,2]      # Definerte lister
    vertices = [v1,v2,v3]       # Nested list med verdier
    v = vertices
    A = 1/2*abs(v[1][0]*v[2][1] - v[2][0]*v[1][1] - v[0][0]*v[2][1] + v[2][0]*v[0][1] + v[0][0]*v[1][1] - v[1][0]*v[0][1])
    return A

def test_triangle_area():       # Testfunksjon som tester om verdien fra forrige def stemmer
    v1 = [0,0]; v2 = [1,0]; v3 = [0,2]      # Definerte lister
    vertices = [v1, v2, v3] # Nested list med verdier
    expected = 1            # Forventet resultat ( verdi fra oppgave )
    computed = triangle_area(vertices)      # Beregnet verdi fra triangle_area
    tol = 1E-14
    success = abs(expected - computed) < tol        # Toleranseverdi
    msg = f"computed area = {computed} != {expected}(expected)"
    assert success, msg     # Dersom succes er false returneres msg
test_triangle_area()


# Kjøretest fra terminalen:
"""
PS C:\Desktop\Python> python triangle_area.py
PS C:\Desktop\Python>
"""
