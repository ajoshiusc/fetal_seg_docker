FROM continuumio/miniconda3

MAINTAINER ajoshiusc

RUN pip install numpy SimpleITK nilearn torch ml_collections

ADD python/src /feta_seg

ADD trained_model /trained_model