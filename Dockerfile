FROM jupyter/scipy-notebook:latest

USER root

# install any user packages defined in environment.yml
WORKDIR "/home/${NB_USER}/work"
RUN mamba install --quiet --yes --channel conda-forge \
  'jupyterlab-variableinspector' \
  'jupyterlab-unfold' \
  'jupyterlab-lsp' \
  'jupyterlab-git' && \
  mamba install --quiet --yes --channel krinsman jupyterlab_html


USER ${NB_UID}
WORKDIR "${HOME}"
