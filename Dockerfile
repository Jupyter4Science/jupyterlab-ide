FROM jupyter/scipy-notebook:latest

# retrieve files
COPY binder/* .

# install jupyterlab extensions
RUN mamba env update --file environment.yml

# enable the extensions
RUN python postBuild
