# Funksjon som skal finne a[0] + a[k] + a[2k]...
def finn_sum(a,k):
    res = sum([a[i] for i in range(0, len(a),k)])
    return res

# Vi lager en testfunkjson:
def test_finn_sum():
    """Testfunksjon for finn sum"""
    a = [0, 1, 2, 3, 4, 5]  # Eksempel for inputverdi for a
    k = 3                   # Eksempel på inputverdi for k
    expected = 3            # Hva output forventes å bli
    computed = finn_sum(a, k)   # Hva output faktisk er
    success = (computed == expected)       # Fikk vi riktg svar?
    message = 'computed %s, expected %s' % (computed, expected)
    assert success, message

# Vi kaller på testfunksjonen
test_finn_sum()
# Et tomt progamkjør i terminalen betyr at det stemmer
