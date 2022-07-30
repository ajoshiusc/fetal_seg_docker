# -*- coding: utf-8 -*-
"""
@author: branhongweili
"""

import os
import glob
import SimpleITK as sitk
import ast
import json

input_img_dir = '/input_img'
input_meta_dir = '/input_meta'
outputDir = '/output'

T2wImagePath = glob.glob(os.path.join(input_img_dir, 'anat', '*_T2w.nii.gz'))[0]
sub = os.path.split(T2wImagePath)[1].split('_')[0] # to split the input directory and to obtain the suject name

# Load the image
T2wImage = sitk.ReadImage(T2wImagePath)

# read JSON file
jsonPath = os.path.join(input_meta_dir, 'meta.json')
with open(jsonPath) as jsonFile:
    jsonData = json.dumps(json.load(jsonFile))
    jsonFile.close()
jsonData = ast.literal_eval(jsonData)

pathology = jsonData['Pathology']
GA = jsonData['Gestational age']

##
# your logic here. Below we do binary thresholding as a demo
##

# using SimpleITK to do binary thresholding between 100 - 10000
resultImage = sitk.BinaryThreshold(T2wImage, lowerThreshold=100, upperThreshold=10000)
# print the pathological info and GA info

print('pathological info:', pathology)
print('GA:', GA)
# save the segmentation mask
sitk.WriteImage(resultImage, os.path.join(outputDir, sub + '_seg_result.nii.gz'))
