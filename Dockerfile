FROM continuumio/miniconda3

MAINTAINER ajoshiusc

RUN pip install numpy SimpleITK

ADD python/src /feta_seg

