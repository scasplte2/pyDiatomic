import numpy as np
import cse
import matplotlib.pyplot as plt
from scipy.special import hermite

######################################################
#
# Harmonic oscillator example
#
# Stephen.Gibson@anu.edu.au
#  24 Aug 2017
######################################################


def phi(v, R, alpha):
    y = R*np.sqrt(alpha)
    Nv = ((alpha/np.pi)**0.25)/np.sqrt(2**v*np.math.factorial(v))
    Hv = hermite(v)
    sum = 0.0
    for i, h in enumerate(Hv.coeffs[::-1]):
        sum += h*(y**i)
    return (-1)**v*sum*Nv*np.exp(-y**2/2)

μ = 2
ω = 1/3
R = np.linspace(-2, 2, 2001)
# quadratic PEC
V = (1/2)*μ*(ω*R)**2

X = cse.Cse(μ, VT=[(R, V)])

fig, ax = plt.subplots()

print(" v   E(v) [cm-1] | [eV]")
for en in [0.01, 0.1, 0.16]:  # guess energies in eV
    X.solve(en)
    wf = X.wavefunction[:, 0, 0]
    if X.vib % 2:
        wf = -wf
    print(f'{X.vib:2d}      {X.cm:8.2f} |{X.cm/8065.541:8.4f}')
    ax.plot(R, wf*300 + X.cm, label=fr'$v={X.vib:d}$')
    ax.plot(R, phi(X.vib, R, μ*ω)*300 + X.cm, 'k--')

ax.plot(np.NaN, np.NaN, 'k--', label=r'analytical')
ax.plot(R, V*8065.541)
ax.axis(xmin=-2, xmax=2, ymin=-10, ymax=2000)
ax.legend()
ax.set_title(r'Harmonic oscillator potential:'
             r' $\psi_v(x) = N_v H_v(x) e^{-x^2/2}$')
ax.set_ylabel(r'potential energy (cm$^{-1}$) / wavefunction $\times 400$')
ax.set_xlabel(r'$x$')

plt.savefig('output/example_HO.png', dpi=75)
plt.show()
