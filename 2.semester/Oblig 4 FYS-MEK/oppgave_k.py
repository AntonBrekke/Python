from oppgave_h import *

code = input('M for midpoint, E for own:')

if code =='E' or code =='ME':
    # Egen implementert metode
    h = 1
    v_0 = 8
    tol = 1e-14

    method = EulerCromer(U0=150, x0=2, alpha=39.48, m=23, T=10, N=50000)
    method.set_initial_condition(v_0=v_0, x_0=-5)
    a, v, x, t = method.solve()

    while abs(method.x0 - np.max(x)) >= tol:
        method.set_initial_condition(v_0=v_0, x_0=-5)
        a, v, x, t = method.solve()
        if np.max(x) < method.x0:
            v_0 += h
        elif np.max(x) > method.x0:
            v_0 -= h
            h *= 0.1
            v_0 += h
        print(v_0)

    print(np.max(x))
    method.set_initial_condition(v_0=v_0, x_0=-5)
    a, v, x, t = method.solve()
    plt.plot(t, x, label= f'v_0 = {method.v_0}' )
    plt.xlabel(r'$t\;[-]$'); plt.ylabel(r'$x\;[-]$')
    plt.title('Atom gjennom felt', weight='bold')
    plt.legend()
    # plt.savefig('oppgave_i.png')
    plt.show()

    E = v_0

if code == 'M' or code == 'ME':
    # Midtpunktmetoden
    method = EulerCromer(U0=150, x0=2, alpha=39.48, m=23, T=10, N=50000)

    min = 8; max = 10
    dif = max - min
    mid = (max + min)/2
    tol = 1e-14
    x0 = method.x0

    while dif > tol:
        print(f'min = {min}, max = {max}, mid = {mid}')
        method.set_initial_condition(v_0=mid, x_0=-5)
        a, v, x, t = method.solve()
        if np.max(x) < x0:
            min = mid
        else:
            max = mid
        mid = (max + min)/2
        dif = max - min

    v_0 = mid
    print(np.max(x))
    method.set_initial_condition(v_0=v_0, x_0=-5)
    a, v, x, t = method.solve()
    plt.plot(t, x, label= f'v_0 = {method.v_0}' )
    plt.xlabel(r'$t\;[-]$'); plt.ylabel(r'$x\;[-]$')
    plt.title('Atom gjennom felt', weight='bold')
    plt.legend()
    # plt.savefig('oppgave_i.png')
    plt.show()
    if code == 'ME':
        print(abs(v_0 - E))
