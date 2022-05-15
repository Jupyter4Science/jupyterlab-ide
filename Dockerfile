FROM jupyter/scipy-notebook:latest

RUN mamba install --quiet --yes --channel conda-forge \
  'jupyterlab-variableinspector' \
  'jupyterlab-unfold' \
  'jupyterlab-lsp' \
  'jupyterlab-git' && \
  mamba install --quiet --yes --channel krinsman jupyterlab_html

RUN jupyter labextension enable jupyterlab-variableinspector --debug
RUN jupyter labextension enable jupyterlab-unfold --debug
RUN jupyter labextension enable jupyterlab-lsp --debug
RUN jupyter labextension enable jupyterlab-git --debug
RUN jupyter labextension enable jupyterlab_html --debug
