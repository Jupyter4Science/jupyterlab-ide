FROM jupyter/scipy-notebook:latest

# retrieve files
RUN mkdir binder
COPY binder/ binder/

# install jupyterlab extensions
RUN mamba env update --file ./binder/environment.yml

# enable the extensions
RUN ./binder/postBuild
