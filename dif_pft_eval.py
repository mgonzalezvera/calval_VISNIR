import mat73
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import scienceplots
import numpy as np

# GENERAL PARAMETERS
sns.light_palette("seagreen", as_cmap=True)
plt.style.use(['science'])
plt.rcParams['text.usetex'] = True

# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
MAIN_FOLDER = '/home/usuario/Documentos/MISION/CalVal/VisNir/20231127_VisNir_INVAP_rev1.0/'

path_dark = 'EOM/Rad/dark/'
dark_folders = [
    'dark_ptf30/',
    'dark_pft150/'
]
path_ltyp = 'EOM/Rad/Ltyp/L1/'
dirs_l1 = {
    'A100': [
        'A100_ptf30/',
        'A100_ptf150/'
    ],
'A46': [
        'A46_ptf30/',
        'A46_ptf150/'
    ],
'A62': [
        'A62_ptf30/',
        'A62_ptf150/'
    ],
'A78': [
        'A78_ptf30/',
        'A78_ptf150/'
    ]
}
def plot_bands_by_att(att):
    dic = {
        'at_30':{'band_' + str(i): [] for i in range(12) if i != 10},
        'at_150': {'band_' + str(i): [] for i in range(12) if i != 10}
    }
    for folder in dirs_l1[att]:
        path_file = MAIN_FOLDER + path_ltyp + folder + '*.mat'
        files = sorted(glob.glob(path_file))
        time_int = []
        for file in files:
            df = mat73.loadmat(file)['salida']
            time_int.append(df['tiemposInt'])
            df = np.mean(df['imagen'], axis=2)
            for i,line in enumerate(df):
                if i == 10:
                    i =11
                dic['band_{}'.format(i)].append(np.mean(line))

    for band in dic.keys():


