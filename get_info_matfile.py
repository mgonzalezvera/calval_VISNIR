
from scipy.io import loadmat
path = '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP/'
files = [
    'EOM/Spectral/B01/dark/dark_20231206120042.431.mat',
    'EOM/Spectral/B01/dark/dark_20231206113207.168.mat',
    'EOM/Spectral/B01/dark/dark_20231206113049.174.mat',
    'EOM/Spectral/B01/dark/dark_20231206101502.716.mat',
    'EOM/Spectral/B07/dark/dark_20231205080925.465.mat',
    'EOM/Spectral/B07/dark/dark_20231205093822.648.mat',
    'EOM/Spectral/B02/dark/dark_20231205132214.732.mat',
    'EOM/Spectral/B02/dark/dark_20231205135952.473.mat',
    'EOM/Spectral/B02/dark/dark_20231205132923.423.mat',
    'EOM/Spectral/B02/dark/dark_20231205120545.214.mat',
    'EOM/Spectral/B04/dark/dark_20231205141749.492.mat',
    'EOM/Spectral/B04/dark/dark_20231205161427.463.mat',
    'EOM/Spectral/B04/dark/dark_20231205144931.476.mat',
    'EOM/Spectral/B04/dark/dark_20231205144658.957.mat',
    'EOM/Spectral/B03/dark/dark_20231206095410.628.mat',
    'EOM/Spectral/B03/dark/dark_20231205163336.435.mat',
    'EOM/Spectral/B03/dark/dark_20231205170427.419.mat',
    'EOM/Spectral/B03/dark/dark_20231206083947.497.mat',
    'EOM/Spectral/B06/dark/dark_20231205114314.468.mat',
    'EOM/Spectral/B06/dark/dark_20231205102610.798.mat',
    'EOM/Spectral/B06/dark/dark_20231205095610.548.mat',
    'EOM/Spectral/B06/dark/dark_20231205102625.549.mat'
]
dt = loadmat(path+files[0])

import mat73
ref_file = '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP/EOM/Spectral/B05/dark/dark_20231130151018.631.mat'
ref_data = mat73.loadmat(ref_file)

test = mat73.loadmat(path+files[0])


extras = [
    '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP/EOM/Spectral/20230712_correcciones/B03/dark_ib/dark_20231207103128.571.mat',
    '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP/EOM/Spectral/20230712_correcciones/B03/dark_ib/dark_20231207103136.239.mat',
    '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP/EOM/Spectral/20230712_correcciones/B04/dark_ib/dark_20231207103312.537.mat',
    '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP/EOM/Spectral/20230712_correcciones/B04/dark_ib/dark_20231207103320.032.mat'
]

new_darks = mat73.loadmat(extras [0])

import numpy as np
import h5py
f = h5py.File(path+files[0],'r')
data = f.get('data/variable1')
data = np.array(data) # For converting to a NumPy array