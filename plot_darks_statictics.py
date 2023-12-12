import mat73
import glob
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime

import scienceplots
sns.light_palette("seagreen", as_cmap=True)
plt.style.use(['science'])
plt.rcParams['text.usetex'] = True


path = '/home/usuario/Documentos/MISION/CalVal/VisNir/20231127_VisNir_INVAP/EOM/Spectral/'
band = 'B01'

path_band = path+band+'/dark/'
files = glob.glob(path_band+'*.mat')
cmap = plt.get_cmap('viridis')

for file in sorted(files):
    fig, axs = plt.subplots()
    df = np.mean(mat73.loadmat(file)['salida']['imagen'], axis=2)
    print('-------------------------------------------------')
    print('INFO')
    print(file[90:])
    date_str = '{} {}'.format(file[95:103],file[103:109])
    date_obj = datetime.strptime(date_str, '%Y%m%d %H%M%S')
    formatted_date = date_obj.strftime('%Y/%m/%d | %H:%M:%S')
    print('Time:', formatted_date)
    print(mat73.loadmat(file)['salida']['tiemposInt'])
    for i,element  in enumerate(df):
        mean_line = np.round(np.mean(element),2)
        axs.plot(range(len(element)),element,label='Line {} - Mean: {}'.format(i,mean_line))

    axs.set_title('T_int = {} ms'.format(mat73.loadmat(file)['salida']['tiemposInt']))
    axs.legend(fontsize=12,frameon=True)

plt.show()