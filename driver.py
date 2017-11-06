#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyjugex
import hbp_human_atlas as atlas
import nibabel as nib
#UNCOMMENT THE FOLLOWING TWO LINES UPLOAD THE PMAPS TO COLLAB STORAGE
#import collab

genelist = ['ADRA2A', 'AVPR1B', 'CHRM2', 'CNR1', 'CREB1', 'CRH', 'CRHR1', 'CRHR2', 'GAD2', 'HTR1A', 'HTR1B', 'HTR1D', 'HTR2A', 'HTR3A', 'HTR5A', 'MAOA', 'PDE1A', 'SLC6A2', 'SLC6A4', 'SST', 'TAC1', 'TPH1', 'GPR50', 'CUX2', 'TPH2']
#genelist = ['ADRA2A', 'AVPR1B', 'CHRM2']
roi1 = atlas.jubrain.probability_map('FP1', atlas.MNI152)
roi2 = atlas.jubrain.probability_map('FP2', atlas.MNI152)
#UNCOMMENT THE FOLLOWING TWO LINES UPLOAD THE PMAPS TO COLLAB STORAGE
'''
collab.upload(roi1['name'])
collab.upload(roi2['name'])
#PRINT JUST UPLOADED FILES
clients = get_hbp_service_client()
collab_path = get_collab_storage_path()
pmap_folder = collab_path + '/pmaps'
print(clients.storage.list(pmap_folder))
'''

jugex = pyjugex.PyJugex(cache=".pyjugex", verbose=True)
result = jugex.DifferentialAnalysis(genelist, roi1['image'], roi2['image'])
if len([id for id in result if result[id] < .05]) > 0:
    print('Differentially expressed genes are : ')
    print([id for id in result if result[id] < .05])
else:
    print('There are no differentially expressed genes in the given regions')

