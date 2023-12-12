import glob

import mat73
#
# MAIN_FOLDER = '/home/usuario/Documentos/MISION/CalVal/VisNir/'
#
#
# path = '/home/usuario/Documentos/MISION/CalVal/VisNir/20231127_VisNir_INVAP/'
#
#
# files = [
#     'EOM/Spectral/B01/dark/dark_20231206120042.431.mat',
#     'EOM/Spectral/B01/dark/dark_20231206113207.168.mat',
#     'EOM/Spectral/B01/dark/dark_20231206113049.174.mat',
#     'EOM/Spectral/B01/dark/dark_20231206101502.716.mat',
#     'EOM/Spectral/B07/dark/dark_20231205080925.465.mat',
#     'EOM/Spectral/B07/dark/dark_20231205093822.648.mat',
#     'EOM/Spectral/B02/dark/dark_20231205132214.732.mat',
#     'EOM/Spectral/B02/dark/dark_20231205135952.473.mat',
#     'EOM/Spectral/B02/dark/dark_20231205132923.423.mat',
#     'EOM/Spectral/B02/dark/dark_20231205120545.214.mat',
#     'EOM/Spectral/B04/dark/dark_20231205141749.492.mat',
#     'EOM/Spectral/B04/dark/dark_20231205161427.463.mat',
#     'EOM/Spectral/B04/dark/dark_20231205144931.476.mat',
#     'EOM/Spectral/B04/dark/dark_20231205144658.957.mat',
#     'EOM/Spectral/B03/dark/dark_20231206095410.628.mat',
#     'EOM/Spectral/B03/dark/dark_20231205163336.435.mat',
#     'EOM/Spectral/B03/dark/dark_20231205170427.419.mat',
#     'EOM/Spectral/B03/dark/dark_20231206083947.497.mat',
#     'EOM/Spectral/B06/dark/dark_20231205114314.468.mat',
#     'EOM/Spectral/B06/dark/dark_20231205102610.798.mat',
#     'EOM/Spectral/B06/dark/dark_20231205095610.548.mat',
#     'EOM/Spectral/B06/dark/dark_20231205102625.549.mat'
# ]
# # dt = loadmat(path+files[0])
#
# # ref_file = '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP/EOM/Spectral/B05/dark/dark_20231130151018.631.mat'
# # ref_data = mat73.loadmat(ref_file)
#
# # test = mat73.loadmat(path+files[0])
# # extras = [
# #     '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP/EOM/Spectral/20230712_correcciones/B03/dark_ib/dark_20231207103128.571.mat',
# #     '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP/EOM/Spectral/20230712_correcciones/B03/dark_ib/dark_20231207103136.239.mat',
# #     '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP/EOM/Spectral/20230712_correcciones/B04/dark_ib/dark_20231207103312.537.mat',
# #     '/home/maxpower/Documentos/SABIA_MAR/VISNIR/VISNIR/DATOS_CRUDOS/20231127_VisNir_INVAP/EOM/Spectral/20230712_correcciones/B04/dark_ib/dark_20231207103320.032.mat'
# # ]
# # new_darks = mat73.loadmat(extras [0])
#
# new_files = [
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231206120042.431.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231206113207.168.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231206113049.174.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231206101502.716.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205080925.465.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205093822.648.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205132214.732.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205135952.473.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205132923.423.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205120545.214.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205141749.492.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205161427.463.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205144931.476.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205144658.957.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231206095410.628.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205163336.435.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205170427.419.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231206083947.497.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205114314.468.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205102610.798.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205095610.548.mat',
# '/home/usuario/Documentos/MISION/CalVal/VisNir/new73/new/dark_20231205102625.549.mat'
# ]
#
# data = mat73.loadmat(new_files[21])
# print(data['salida']['imagen'])
# print(data['salida']['imagen'].shape)
# print(data['salida']['nombre_imagen'])
# print(data['salida']['tiemposInt'])
band = 'B06'
IB_path = '/home/usuario/Documentos/MISION/CalVal/VisNir/20231127_VisNir_INVAP/EOM/Spectral/{}/ib/'.format(band)

files = glob.glob(IB_path+'*.mat')
print(band)
for file in files:
    # print(file)
    mat_data = mat73.loadmat(file)
    # print(mat_data)
    value = mat_data['info']['T_Integracion']
    print(f"   - {file}: {value} ms")