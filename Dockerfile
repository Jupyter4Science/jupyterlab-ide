FROM jupyter/scipy-notebook:latest

# retrieve local files
COPY environment.yml .
COPY postBuild .

# install jupyterlab extensions
RUN mamba env update --file environment.yml

# enable the extensions
RUN python postBuild
