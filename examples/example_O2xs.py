# -*- coding: utf-8 -*-
"""
  CSE  - solve the coupled-channel time-independent Schrödinger equation
         using recipe of B.R. Johnson J Chem Phys 69, 4678 (1977).

  Stephen.Gibson@anu.edu.au
  2016
"""

import numpy as np
import matplotlib.pylab as plt
import time

import cse

evcm = 8065.541   # conversion factor eV -> cm-1

d = 'potentials/'  # directory name

wavelength = np.arange(110, 174.1, 0.1)  # nm

# initialize CSE problem - any missing essential parameters are requested
# mu - reduced mass
# eni - initial state guess energy
# VTI - initial state(s)
# VTf - final coupled states
# coupf - homogeneous coupling
# dipolemoment - transition moments 

X = cse.Xs(mu='O2', VTi=[d+'X3S-1.dat'], eni=800,
                    VTf=[d+'B3S-1.dat', d+'3P1.dat', d+'E3S-1.dat',
                         d+'3PR1.dat'],
                    coupf=[40, 4000, 0, 0, 7000, 0],
                    dipolemoment=[1, 0, 0, 0.3])
                    #, transition_energy=wavelength)  # <--- alternative direct call

print("CSE: calculating cross section speeded by Python multiprocessing",
      " Pool.map")
print("     from {:.2f} to {:.2f} in {:.2f} nm steps ... ".
      format(wavelength[0], wavelength[-1], wavelength[1]-wavelength[0]))

t0 = time.time()
X.calculate_xs(transition_energy=wavelength)
print("CSE: ...  in {:.2g} seconds".format(time.time()-t0))

print('CSE: E(v"={:d}) = {:.2f} cm-1, {:.3g} eV'.format(X.gs.node_count(), 
                                                   X.gs.cm, X.gs.energy))
