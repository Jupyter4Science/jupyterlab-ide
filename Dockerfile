FROM jupyter/scipy-notebook:latest

# retrieve files
COPY binder/ .

RUN ls

# install jupyterlab extensions
RUN mamba env update --file ./binder/environment.yml

# enable the extensions
RUN ./binder/postBuild
