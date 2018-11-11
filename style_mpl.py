"""
LHCb-like style for matplotlib
"""


__all__ = [
    'style_mpl',
]

def style_mpl():

    STYLE = {}

    STYLE['lines.linewidth'] = 1.5

    # font
    STYLE['text.usetex'] = True
    STYLE['font.family'] = 'serif'
    STYLE['mathtext.fontset'] = 'stix'
   # STYLE['mathtext.default'] = 'rm'
    # helvetica usually not present on linux
    STYLE['font.serif'] ='Times New Roman'
    # figure layout
    STYLE['figure.figsize'] =6,7
    #   lhcbStyle->SetPaperSize(20,26); # in cm
    # STYLE['figure.figsize'] =  10.2362205, 7.874015 # in inc, not working
    STYLE['figure.facecolor'] = 'white'
    STYLE['figure.subplot.bottom'] = 0.14
    STYLE['figure.subplot.top'] = 0.95
    STYLE['figure.subplot.left'] = 0.14
    STYLE['figure.subplot.right'] = 0.95
    STYLE['savefig.facecolor']= 'ff000000'
    # axes
    STYLE['axes.xmargin']= 0
    STYLE['axes.ymargin']= 0.05
    STYLE['axes.labelsize'] = 22
    STYLE['xtick.labelsize'] =12
    STYLE['xtick.major.size'] = 7.5
    STYLE['xtick.minor.size'] = 3.75
    STYLE['ytick.labelsize'] = 12
    STYLE['ytick.major.size'] = 7.5
    STYLE['ytick.minor.size'] = 3.75
    STYLE['lines.markersize'] = 5
    STYLE['xtick.minor.bottom'] =True
    STYLE['xtick.top'] =True
    STYLE['ytick.right'] =True
    # STYLE['lines.markeredgewidth'] = 0. # not working, it changes other stuff

    # legend
    STYLE['legend.numpoints'] = 1
    STYLE['legend.fontsize'] = 13
    STYLE['legend.labelspacing'] = 0.3
    STYLE['legend.frameon'] = False

    # what cannot be set with rcParams:
    # * markeredgewidth
    # * axis-label alignment
    # * axis-label offset
    # * axis-ticks

    return STYLE
