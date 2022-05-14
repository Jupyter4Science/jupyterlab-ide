FROM jupyter/scipy-notebook:latest

# install any user packages defined in environment.yml
WORKDIR "/home/${NB_USER}/work"
COPY environment.yml .
RUN mamba env update --file environment.yml
