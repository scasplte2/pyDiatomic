import numpy as np
import cse
import matplotlib.pyplot as plt
from scipy.special import hermite

######################################################
#
# Absolute value example
#
# jim.aman@rice.edu
#  16 March 2019
######################################################


def phi(v, R, alpha):
    y = R*np.sqrt(alpha)
    Nv = (alpha/np.pi)**0.25/np.sqrt(2**v*np.math.factorial(v))
    Hv = hermite(v)
    sum = 0.0
    for i, h in enumerate(Hv.coeffs[::-1]):
        sum += h*(y**i)
    return (-1)**v*sum*Nv*np.exp(-y**2/2)


R = np.linspace(-2, 2, 401)
# linear PEC
V = abs(R)/10

X = cse.Cse(2, VT=[(R, V)])

fig, ax = plt.subplots()

print(" v    E(v) in cm-1")
for en in [0.01, 0.03, 0.04, 0.06, 0.09]:  # guess energies in eV
    X.solve(en)
    wf = X.wavefunction[:, 0, 0]
    if X.vib % 2:
        wf = -wf
    print(f'{X.vib:2d}  {X.cm:8.2f}')
    ax.plot(R, wf*400 + X.cm, label=fr'$v={X.vib:d}$')
    ax.plot(R, phi(X.vib, R, 10)*400 + X.cm, 'k--')

ax.plot(np.NaN, np.NaN, 'k--', label=r'analytical')
ax.plot(R, V*8065.541)
ax.axis(xmin=-1.5, xmax=1.5, ymin=-800, ymax=1600)
ax.legend()
ax.set_title(r'Absolute value potential:'
             r' $\psi_v(x) = N_v H_v(x) e^{-x^2/2}$')
ax.set_ylabel(r'potential energy (cm$^{-1}$) / wavefunction $\times 400$')
ax.set_xlabel(r'$x$')

plt.savefig('output/example_abs.png', dpi=75)
plt.show()
