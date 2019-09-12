import os
import pickle

import numpy as np
from utils.path_utils import idp_preprocess, generate_path

specimen_list = [
    generate_path('ya', 0, mode='idp'), generate_path('ya', 1, mode='idp'),
    generate_path('ya', 2, mode='idp'), generate_path('ya', 3, mode='idp'),
    generate_path('ya', 4, mode='idp'), generate_path('ya', 5, mode='idp'),
    generate_path('ya', 6, mode='idp'), generate_path('ya', 7, mode='idp'),
    generate_path('ya', 8, mode='idp'), generate_path('ya', 9, mode='idp'),
    generate_path('ya', 10, mode='idp'), generate_path('ya', 11, mode='idp'),

    generate_path('zy', 0, mode='idp'), generate_path('zy', 1, mode='idp'),  # frame num 1379 problematic
    generate_path('zy', 2, mode='idp'), generate_path('zy', 3, mode='idp'),
    generate_path('zy', 4, mode='idp'), generate_path('zy', 5, mode='idp'),
    generate_path('zy', 6, mode='idp'), generate_path('zy', 7, mode='idp'),  # 6th problematic
    generate_path('zy', 8, mode='idp'), generate_path('zy', 9, mode='idp'),
    generate_path('zy', 10, mode='idp'), generate_path('zy', 11, mode='idp'),

    generate_path('zl', 0, mode='idp'), generate_path('zl', 1, mode='idp'),
    generate_path('zl', 2, mode='idp'), generate_path('zl', 3, mode='idp'),
]

# use data augmentation

isDataGen = True

for i, path in enumerate(specimen_list):
    # generate orignial data
    print('Processing specimen #' + str(i) + ' ' + str(path[0]) + '__________________________________')
    idp_preprocess(path, is_plot=False)
    idp_preprocess(path, augmentation=['trans'])

    # idp_preprocess(path, augmentation=['clp', 'trans'])
    # idp_preprocess(path, augmentation=['rot'])
    # idp_preprocess(path,  augmentation=['scale'])
    #
    # idp_preprocess(path, augmentation=['trans', 'rot'])
    # idp_preprocess(path, augmentation=['trans', 'scale'])
    # idp_preprocess(path,  augmentation=['rot', 'scale'])
    #
    # idp_preprocess(path,  augmentation=['trans', 'rot', 'scale'])

# just plot the thing
# for i, path in enumerate(specimen_list):
#     # generate orignial data
#     print('Processing specimen #' + str(i) + '__________________________________')
#     idp_preprocess(path, is_plot=True)