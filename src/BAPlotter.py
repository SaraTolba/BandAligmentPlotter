#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib as mpl
import os

"""
__author__ = "Sara A. Tolba"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0.0"

"""


"""
Configuration class which you can specify or edit any propery you want!
"""
class Config: 
    # Define the colors for the colormap
    __DARK_ORANGE = (247/255., 148/255., 51/255.)
    __LIGHT_ORANGE = (251/255., 216/255., 181/255.) 
    
    __DARK_BLUE = (23/255., 71/255., 158/255.)
    __LIGHT_BLUE = (174/255., 198/255., 242/255.)
    
    _cb_colors = [__LIGHT_ORANGE, __DARK_ORANGE]
    _vb_colors = [__LIGHT_BLUE, __DARK_BLUE]

    fig_size = (100,100)
    bar_width = 5

    fontFamily = 'Arial'
    fontSize = 12
    
    axesLabelSize = fontSize
    axesLineWidth = 1
    
    xtickLabelSize = 12
    ytickLabelSize = 8
    
    linesLineWidth = 1
    legendMarkerScale = 1
    
    

class Plotter:
    
    def __init__(self, materials, vbm_energies, cbm_energies, config=Config()) -> None:
        """Plotter class constructor, specify that it should take in data for plotting the band alignment

        Args:
            materials (list): List of materials names as strings
            vbm_energies (list): List of Valence Band maximum energies in eV. 
            cbm_energies (list): List of Conduction Band minimum energies in eV. 
            config (Config Object, optional): Config class to change the proprties of the figure such as font family,font size or colors! Defaults to Config().
        """
        self.materials = materials
        self.vbm_energies = vbm_energies
        self.cbm_energies = cbm_energies
        self.config = config

        # ---------Matlibplot configuration defaults
        mpl.rcParams['font.family'] = config.fontFamily
        mpl.rcParams['font.size'] = config.fontSize
        mpl.rcParams['axes.labelsize'] = config.axesLabelSize
        mpl.rcParams['axes.linewidth'] = config.axesLineWidth
        mpl.rcParams['xtick.labelsize'] = config.xtickLabelSize
        mpl.rcParams['ytick.labelsize'] = config.ytickLabelSize
        mpl.rcParams['lines.linewidth'] = config.linesLineWidth
        mpl.rcParams["legend.markerscale"] = config.legendMarkerScale

    def __plot(self):
        """This code appears to be creating a plot of band alignment for a list of materials. 
        It does this by creating a LinearSegmentedColormap object from a list of colors for the valence band (vb) and conduction band (cb), and creating a new figure and axis. 
        It then loops through the materials, creating a rectangle patch for the valence band minimum (vbm) and conduction band maximum (cbm) for each material using the colormap and alpha values to create a gradient effect. 
        The materials' names are also added to the plot.
        Finally, labels for the valance band and conduction band are added at the bottom and top of the x-axis, respectively.

        Returns:
            figure: reutrn matplotlib figure to save or show
        """
        positions = [x * 5 for x in range(len(self.materials))]

        # Create a LinearSegmentedColormap object from the colors
        cb_map = colors.LinearSegmentedColormap.from_list(
            "", self.config._cb_colors)
        vb_map = colors.LinearSegmentedColormap.from_list(
            "", self.config._vb_colors)

        # Create a new figure and axis
        fig, ax = plt.subplots()

        # Loop through the materials
        for i in range(len(self.materials)):
            # Convert the colormap to a tuple of RGBA values
            left = positions[i]
            right = left + 5  # left + bar_width
            vb_bottom = min(self.vbm_energies)-3
            vb_top = self.vbm_energies[i]
            cb_bottom = self.cbm_energies[i]
            cb_top = max(self.cbm_energies)+3

            ax.annotate(str(self.materials[i]), (positions[i]+2.5, self.vbm_energies[i]-0.9), color='white',
                        weight='normal', fontsize=self.config.fontSize - len(self.materials), ha='center', va='center', zorder=7)  # <------- edit

            # Create a Rectangle patch for the VBM
            vbm = matplotlib.patches.Rectangle((positions[i], vb_bottom), 5, (
                self.vbm_energies[i]-vb_bottom), alpha=0, facecolor='w', clip_on=True, zorder=5)
            vbm_box = matplotlib.patches.Rectangle((positions[i], vb_bottom), 5, (
                self.vbm_energies[i]-vb_bottom), alpha=1, fill=None, clip_on=True, zorder=6, lw=0.5)

            # Set the alpha values of the patch to create a gradient from the top to the bottom
            X = [[.7, .7], [0.6, 0.6]]
            ax.imshow(X, interpolation='bicubic', cmap=vb_map,
                      extent=(left, right, vb_bottom, vb_top), alpha=1)

            # # Add the patch to the axis
            ax.add_patch(vbm)
            ax.add_patch(vbm_box)
            ax.set_gid(self.materials[i])

            cbm = matplotlib.patches.Rectangle((positions[i], self.cbm_energies[i]), 5, (
                cb_top-self.cbm_energies[i]), alpha=0, facecolor='w', clip_on=False, zorder=5)

            cbm_box = matplotlib.patches.Rectangle((positions[i], self.cbm_energies[i]), 5, (
                cb_top-self.cbm_energies[i]), alpha=1, fill=None, clip_on=True, zorder=6, lw=0.5)

            ax.imshow(X, interpolation='bicubic', cmap=cb_map,
                      extent=(left, right, cb_top, cb_bottom), alpha=1)
            # # cbm.set_label(materials[i])
            ax.add_patch(cbm)
            ax.add_patch(cbm_box)

            # print(str(materials[i]))

        # Add the Valance Band label at the bottom of the x-axis
        # ax.text(0.5, -0.08, 'Valance Band', transform=ax.transAxes, ha='center', fontsize=12)
        ax.text(0.5, -0.1, 'Valance Band',
                transform=ax.transAxes, ha='center')

        # Add the Conduction Band label at the top of the x-axis
        # ax.text(0.5, 1.05, 'Conduction Band', transform=ax.transAxes, ha='center', fontsize=12)
        ax.text(0.5, 1.05, 'Conduction Band',
                transform=ax.transAxes, ha='center')

        ax.set_ylabel("Energy (eV)")

        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            labelbottom=False)  # labels along the bottom edge are off

        plt.xlim([0, max(positions)+5])
        plt.ylim([min(self.vbm_energies)-3, max(self.cbm_energies)+3])

        return fig

    
    
    def show(self):
        import tkinter as Tk
        fig = self.__plot()
        fig.show()
        Tk.mainloop()

        
    def save(self, __path=None):
        # Show the plot
        fig = self.__plot()
        iamge_name = 'BandAligment.png'
        if __path is None:
            fig.savefig(iamge_name, dpi=1000)
            print(f'Image Saved at {os.path.join(os.getcwd(),iamge_name)}')
        else:
            fig.savefig(os.path.join(__path, iamge_name), dpi=1000)
            print(f'Image Saved at {os.path.join(__path,iamge_name)}')

