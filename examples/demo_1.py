from BAPlotter import Plotter

materials = ['DBT', 'TS6', '2TS6']
vbm_energies = [-6.937817558 ,-5.61561582	,-5.05016300]
cbm_energies = [-2.661274542,	-1.603567574,	-2.060446915]


plotter = Plotter(materials,vbm_energies,cbm_energies)
# plotter.show()
# Note: Image will not be saved until you close the image figure window
plotter.save('path/to/file')
