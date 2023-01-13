FROM jupyter/scipy-notebook:latest

USER root

# install texlive
RUN apt-get update -y && \
    apt-get upgrade -y && \ 
    apt-get install texlive-full -y

# retrieve files
RUN mkdir binder
COPY binder/ binder/

# install jupyterlab extensions
RUN mamba env update --file ./binder/environment.yml

# enable the extensions
RUN ./binder/postBuild

# install latest version of quarto
RUN wget https://quarto.org/docs/download/_download.json && \
    ver=$(grep -o '"version": "[^"]*' _download.json | grep -o '[^"]*$') && \
    wget https://github.com/quarto-dev/quarto-cli/releases/download/v${ver}/quarto-${ver}-linux-amd64.deb && \
    sudo dpkg -i quarto-${ver}-linux-amd64.deb && \
    rm quarto-${ver}-linux-amd64.deb && \
    rm _download.json
