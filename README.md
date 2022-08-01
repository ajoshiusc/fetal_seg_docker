# fetal_seg_docker
This repository has code for creating a docker container for fetal brain segmentation as part of feta 2022 challenge.
https://feta.grand-challenge.org/

Here are the steps for building docker image from the data.

1. Download the github respositry.

2. Download the trained weights epoch66.pth and place it in subdirectory trained_model. You should have file fetal_seg_docker/trained_model/epoch66.pth

3. Open terminal and cd fetal_seg_docker directory. Type
docker build . -t feta_challenge/ajoshiusc

This will build a docker image

4. The docker assumes that the fetal image is in 
<subdir>/anat/sub-026_rec-mial_T2w.nii.gz

For reference, the corresponding lines of code is as follows:

    T2wImagePath = glob.glob(os.path.join(input_img_dir, 'anat', '*_T2w.nii.gz'))[0]
    sub = os.path.split(T2wImagePath)[1].split('_')[0] # to split the input directory and to obtain the suject name

This might tell you how the directory structure should be for the input data.

5. Run the docker image to make it into container:

 docker run -dit -v <input_dir>/:/input_img/:ro -v <meta_dir>/:/input_meta/:ro -v /output feta_challenge/ajoshiusc

e.g. 
 docker run -dit -v /deneb_disk/feta_2022/test/sub-026/:/input_img/:ro -v /deneb_disk/feta_2022/test/:/input_meta/:ro -v /output feta_challenge/ajoshiusc

You will see a slidebar showing the slices of 3d image being processed.

6. Copy the output from the container to an output 


7. Save docker image to tar.gz file
docker save feta_challenge/ajoshiusc:latest|gzip>feta_challenge_ajoshiusc_ver0.tar.gz


= Download and Run the Docker Image
Download the Docker Image docker load feta_challenge_ajoshiusc_ver0.tar.gz

Load the docker image docker load <feta_challenge_ajoshiusc_ver0.tar.gz

