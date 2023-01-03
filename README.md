# BandAligmentPlotter
Package to plot band gap alignment

## Installing

Install BAPlotter by using `pip`:
```bash
pip install baplotter
```

    
## Usage


```python
from BAPlotter import Plotter

plotter = Plotter(materials,vbm_energies,cbm_energies)
plotter.save('path/to/file')
```

## Examples: 

### Example 1
The basic example with default confugration is shown below:
```python
from BAPlotter import Plotter

materials = ['DBT', 'TS6', '2TS6']
vbm_energies = [-6.937817558 ,-5.61561582	,-5.05016300]
cbm_energies = [-2.661274542,	-1.603567574,	-2.060446915]

plotter = Plotter(materials,vbm_energies,cbm_energies)
plotter.save('path/to/file')

```

![Band Gap Alignment Figure](https://github.com/SaraTolba/BandAligmentPlotter/blob/main/examples/Figures/BandAligment_1.png)

## Contributing
Please feel free to contribute to the BAPlotter repo!

You can checkout [Matplotlib's documentation](https://matplotlib.org/stable/index.html) for more information on plotting settings.

