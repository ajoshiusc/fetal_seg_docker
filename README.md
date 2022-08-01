# fetal_seg_docker
This repository has code for creating a docker container for fetal brain segmentation as part of [feta 2022 challenge](https://feta.grand-challenge.org/).

Here are the steps for building docker image from the data.

1. Download this github respositry.

2. Download the trained weights [epoch66.pth](https://drive.google.com/drive/folders/1wSEx3jYgqnjiOcKkA0E9Xt44Z8IO9Nah?usp=sharing) and place it in subdirectory trained_model. The path of the file on your computer should be 
`fetal_seg_docker/trained_model/epoch66.pth`

3. Open terminal and cd fetal_seg_docker directory. Type
```docker
docker build . -t feta_challenge/ajoshiusc`
```
This will build a docker image

4. The docker assumes that the fetal image that you want to segment is in 
`<subdir>/anat/sub-026_rec-mial_T2w.nii.gz`.
For reference, the corresponding lines of code is as follows:
```python
    T2wImagePath = glob.glob(os.path.join(input_img_dir, 'anat', '*_T2w.nii.gz'))[0]
    sub = os.path.split(T2wImagePath)[1].split('_')[0] # to split the input directory and to obtain the suject name
```
This might tell you how the directory structure should be for the input data.

5. Save docker image to tar.gz file
```docker
docker save feta_challenge/ajoshiusc:latest|gzip>feta_challenge_ajoshiusc_ver1.tar.gz
```

= Download and Run the Docker Image
1. Download the Docker image from [Google Drive Link](https://drive.google.com/drive/folders/1P8NWtSxVJIZGzXwM-7kzcuqpH1ID5cVg?usp=sharing) 

2. Load the docker image docker 
```docker
load <feta_challenge_ajoshiusc_ver1.tar.gz
```

3. Run the docker image to make it into container:
```docker
 docker run -dit -v <input_dir>/:/input_img/:ro -v <meta_dir>/:/input_meta/:ro -v /output feta_challenge/ajoshiusc
```
e.g.
```docker
 docker run -dit -v /deneb_disk/feta_2022/test/sub-026/:/input_img/:ro -v /deneb_disk/feta_2022/test/:/input_meta/:ro -v /output feta_challenge/ajoshiusc
```
Check the name of the running container using `docker ps`.
4. Run the segmentation code
```docker
docker exec <container name> python feta_seg/fetal_seg_nii.py
```
You will see a slidebar showing the slices of 3d image being processed. It should take about a min or two. Message will show that the segmentation is done and output is saved (within the container).

5. Copy the output from the container to an output directory using the command
```docker 
docker cp keen_fermat:/output <local_output_dir>
``` 

Now you can inspect the files in the output directory.

