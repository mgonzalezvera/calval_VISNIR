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
    colores_espectro = ['violet', 'blue', 'cyan', 'green', 'yellow', 'orange', 'red', 'darkred', 'maroon',
                        'darkmagenta', 'darkblue']
    dic = {
        'at_30':{'band_' + str(i): [] for i in range(12) if i != 10},
        'at_150': {'band_' + str(i): [] for i in range(12) if i != 10}
    }
    timesint = {
        'at_30': [],
        'at_150': []
    }
    dic_keys = list(dic.keys())
    for j,folder in enumerate(dirs_l1[att]):
        path_file = MAIN_FOLDER + path_ltyp + folder + '*.mat'
        files = sorted(glob.glob(path_file))
        for file in files:
            df = mat73.loadmat(file)['salida']
            timesint[dic_keys[j]].append(df['tiemposInt'])
            df = np.mean(df['imagen'], axis=2)
            sd = np.std(df)
            for i,line in enumerate(df):
                if i == 10:
                    i =11
                dic[dic_keys[j]]['band_{}'.format(i)].append(np.mean(line))
                # dic[dic_keys[j]]['band_{}'.format(i)].append([np.mean(line),sd])

    fig, axs = plt.subplots()
    for pft in dic.keys():
        ls = '-'
        if pft[3:]=='150':
            ls = '--'
        for i_color,band in enumerate(dic[pft].keys()):

            mean_band = dic[pft][band]
            axs.plot(timesint[pft],mean_band,label=band+' pft= {} ms'.format(pft[3:]),
                     ls=ls,color=colores_espectro[i_color]
                     )


            axs.set_title(att)

    plt.legend(frameon=True)
    # plt.show()


dir_keys = list(dirs_l1.keys())
for i in dir_keys:
    plot_bands_by_att(i)
plt.show()

