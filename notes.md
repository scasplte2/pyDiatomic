### Setup virtual environment first using
```
python -m virtualenv env0
```

### Activate virtaul environment with
```
source env0/bin/activate
```

### Installed pyDiatomic with
```
pip install -e . (instead of python setup.py develop --user as suggested)
```

### Installed the following packages as well
```
pip install numpy
pip install scipy
pip install periodictable
pip install matplotlib
pip install jupyterlab
```

### Adding your own potential curves
Strontium potential energy curves are given as two column data sets in `./examples/potentials`. The ground state X^1\Sigma_g^+ potential is given in two variants (srGS.dat and srGS_halo.data) with the latter being a higher resolution potential for trying to get the theoretical energy of the least bound state in 86. 

The documentation for pydiatomic (https://pydiatomic.readthedocs.io/en/latest/index.html) describes a way to define curves with angular momentum coupling ebtween them but I was not able to get this to work. My attempts are the excited state potential file srVA, srVB, srVF for one basis and srX, srY, and srZ for the other basis described in the '15 Nicholson paper on OFR.

### Example notebooks
There are Jupyter notebooks with examples avialable in `examples/Notebooks/` these can be accessed by starting Jupyter notebook from a python shell using
```
jupyter lab
```

### NOTE: Your local version of python may be `python3` and `pip3` instead of `python` and `pip`
