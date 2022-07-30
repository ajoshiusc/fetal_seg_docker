FROM continuumio/miniconda

MAINTAINER ajoshiusc

RUN pip nilearn install numpy SimpleITK

ADD python/src /feta_seg

