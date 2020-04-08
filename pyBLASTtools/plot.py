import matplotlib.pyplot as plt
import numpy as np

import pyBLASTtools.mapmaker as mp


def plot_map(map_value, projection, idxpixel, title=None, centroid=None, save=False, save_path=None):


    wcs_proj = mp.wcs_world(projection.wcs.ctype, projection.wcs.crpix, projection.wcs.cdelt, \
                            projection.wcs.crval, projection.wcs.radesys, projection.wcs.equinox)

    if list(projection.wcs.ctype) == ['RA---TAN', 'DEC--TAN']:
        string_x = 'RA (deg)'
        string_y = 'DEC (deg)'
    elif list(projection.wcs.ctype) == ['TLON-ARC', 'TLAT-ARC']:
        string_x = 'AZ (deg)'
        string_y = 'EL (deg)'
    elif list(projection.wcs.ctype) == ['TLON-CAR', 'TLAT-CAR']:
        string_x = 'xEL (deg)'
        string_y = 'EL (deg)'
    elif list(projection.wcs.ctype) == ['TLON-TAN', 'TLAT-TAN']:
        string_x = 'RA_proj (deg)'
        string_y = 'DEC_proj (deg)'

    proj_plot = wcs_proj.reproject(idxpixel)

    ax = plt.subplot(projection=proj_plot)

    im = ax.imshow(map_value, origin='lower')

    plt.colorbar(im)

    if centroid is not None:
        ax.plot(centroid[0]-np.floor(np.amin(idxpixel[:,0])), \
                centroid[1]-np.floor(np.amin(idxpixel[:,1])), 'x', c='red')

    c1 = ax.coords[0]           
    c2 = ax.coords[1]
    c1.set_axislabel(string_x)
    c2.set_axislabel(string_y)
    c1.set_major_formatter('d.ddd')
    c2.set_major_formatter('d.ddd')

    if title is not None:
        plt.title(title)  

    if save:        
        plt.savefig(save_path, dpi=120)
        plt.close()
    
