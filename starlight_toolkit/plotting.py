'''

Tools for plotting Starlight output.

ariel@ufsc
Created on 05/30/2017

'''

import numpy as np
import matplotlib.pyplot as plt
from starlight_toolkit.tables import read_output_table

def plot_spec(ax, out_file, plot_obs=True, plot_error=False, plot_labels=False
, obs_color='k', syn_color='b', w0_color='y', syn_label='Fitted Spectrum'):
    '''
    TODO: Add marks for clipped wavelengths, documentation.

    '''

    out = read_output_table(out_file)

    l_obs, f_obs, f_syn, f_wei = out['spectra']['l_obs'], \
    out['spectra']['f_obs'], out['spectra']['f_syn'], out['spectra']['f_wei']

    w0 = out['spectra']['f_wei'] <= 0

    error = 1/(f_wei[~w0]**2)

    if plot_obs==True:

        f_obs_masked = np.ma.masked_array(data = f_obs, mask = w0)
        f_w0         = np.ma.masked_array(data = f_obs, mask = ~w0)

        ax.plot(l_obs, f_obs, color=obs_color, lw=0.5, label='Observed Spectrum')
        ax.plot(l_obs, f_w0, color=w0_color, lw=0.5, label=r'$w_\lambda=0$')

    if plot_error==True:
        ax.plot(l_obs[~w0], error, '--r')

    if plot_labels==True:
        ax.set_ylabel(r'$F_\lambda/F_{\lambda0}$', fontsize=15)
        ax.set_xlabel(r'$\lambda\mathrm{[\AA]}$', fontsize=15)

    ax.plot(l_obs, f_syn, color=syn_color, lw=0.5, label=syn_label)

    ax.set_ylim(0, 1.2 * np.max(f_syn))
    ax.set_xlim(out['keywords']['l_ini'],out['keywords']['l_fin'])
