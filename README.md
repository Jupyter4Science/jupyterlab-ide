# jupyterlab-ide

A list of JupyterLab extensions that give it the same functionalities as a traditional IDE

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nicole-brewer/jupyterlab-ide/HEAD?labpath=00_introduction.ipynb)

## Motivation

**Iterative Programming** takes place when you can explore your code and play with your objects and functions without needing to save, recompile, or leave your development environment. This has traditionally been achieved with a REPL or an interactive shell. The magic of Jupyter Notebooks is that the interactive shell is saved as a persistant document, so you don't have to flip back and forth between your code files and the shell in order to program iteratively.

There are several editors and IDE's that are intended for notebook development, but JupyterLab is a natural choice because it is free and open source and most closely related to the Jupyter Notebooks/iPython projects. The chief motivation of this repository is enable an IDE-like development environment through the use of extensions. There are also expositional notebooks to show off the usefulness of these features.

## IDE Features

For a full walkthrough of IDE features open [introduction.ipynb](https://nbviewer.org/github/nicole-brewer/jupyterlab-ide/blob/main/introduction.ipynb) in JupyterLab (locally or with Binder)

### Native Features

- table of contents
- debugger
- tab extension

### Extensions

- [jupyterlab-latex](https://github.com/jupyterlab/jupyterlab-latex) 
- [jupyterlab-lsp](https://github.com/krassowski/jupyterlab-lsp)
- [spellchecker](https://github.com/jupyterlab-contrib/spellchecker)
- [jupyterlab-sidecar](https://github.com/jupyter-widgets/jupyterlab-sidecar)
- [jupyterlab_code_formatter](https://github.com/ryantam626/jupyterlab_code_formatter)
- [jupyterlab-vim](https://github.com/jwkvam/jupyterlab-vim)
- [jupyterlab-variableInspector](https://github.com/lckr/jupyterlab-variableInspector)

## Usage

You can use this repository in one of two ways.

1. Launch the repo with [Binder](https://mybinder.org/v2/gh/nicole-brewer/jupyterlab-ide/HEAD?labpath=introduction.ipynb) to learn about JupyterLab extensions you may want to use in your own projects in the future.
2. You can use [binder/environment.yml](https://github.com/nicole-brewer/jupyterlab-ide/blob/main/binder/environment.yml) as a starting point for your next development environment you create with conda. Please note that you will need to run the [binder/postBuild](https://github.com/nicole-brewer/jupyterlab-ide/tree/main/binder) script after you launch JupyterLab in order for the JupyterLab extensions to be enabled.
