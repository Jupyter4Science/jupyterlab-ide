# jupyterlab-ide

A list of JupyterLab extensions that give it the same functionalities as a traditional IDE

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nicole-brewer/jupyterlab-ide/HEAD?labpath=00_introduction.ipynb)

## Motivation

**Iterative Programming** takes place when you can explore your code and play with your objects and functions without needing to save, recompile, or leave your development environment. This has traditionally been achieved with a REPL or an interactive shell. The magic of Jupyter Notebooks is that the interactive shell is saved as a persistant document, so you don't have to flip back and forth between your code files and the shell in order to program iteratively.

There are several editors and IDE's that are intended for notebook development, but JupyterLab is a natural choice because it is free and open source and most closely related to the Jupyter Notebooks/iPython projects. The chief motivation of this repository is to enable an IDE-like development environment through the use of extensions. There are also expositional notebooks to show off the usefulness of these features.

## IDE Features

For a full walkthrough of IDE features open [introduction.ipynb](https://nbviewer.org/github/nicole-brewer/jupyterlab-ide/blob/main/introduction.ipynb) in JupyterLab (locally or with Binder)

### Native Features

- table of contents
- debugger
- tab extension

### Extensions in this repo

- [jupyterlab_code_formatter](https://github.com/ryantam626/jupyterlab_code_formatter)
  - The jupyterlab code formatter extension adds code formatting support for external code formatters while using JupyterLab.
- [jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git)
  - The jupyterlab-git extension provides a tab allowing for users to use git features in the JupyterLab interface without launching the terminal.
- [jupyterlab-lsp](https://github.com/krassowski/jupyterlab-lsp)
  - The LSP extension integrates language server protocols into JupyterLab for code linting, auto-completion, and much more.
- [jupyterlab-spellchecker](https://github.com/jupyterlab-contrib/spellchecker)
  - The jupyterlab-spellchecker extension provides a spell checker for markdown cells and .md files.
- [jupyterlab-unfold](https://github.com/jupyterlab-contrib/jupyterlab-unfold)
  - The jupyterlab-unfold extension provides an IDE-like file browser for JupyterLab.
- [jupyterlab-vim](https://github.com/jupyterlab-contrib/jupyterlab-vim) ([tutorial notebooks](https://github.com/nicole-brewer/jupyterlab-ide/tree/main/vim))
  - The jupyterlab-vim extension provides Vim style keybindings for notebook editing.

### Other extensions

- [jupyterlab-latex](https://github.com/jupyterlab/jupyterlab-latex)
  - By providing a LaTeX preview, JupyterLab LaTeX provides a live-editing experience for LaTeX documents.
- [jupyterlab-sidecar](https://github.com/jupyter-widgets/jupyterlab-sidecar)
  - The Sidecar extension provides a widget like the output widget from ipywidget.
- [jupyterlab-variableInspector](https://github.com/lckr/jupyterlab-variableInspector)
  - The jupyterlab_variableinspector extension furnished JupyterLab with a variable inspector for active kernels.

## Usage

You can use this repository in one of two ways.

1. Launch the repo with [Binder](https://mybinder.org/v2/gh/nicole-brewer/jupyterlab-ide/HEAD?labpath=introduction.ipynb) to learn about JupyterLab extensions you may want to use in your own projects in the future.
2. You can use [binder/environment.yml](https://github.com/nicole-brewer/jupyterlab-ide/blob/main/binder/environment.yml) as a starting point for your next development environment you create with conda. Please note that you will need to run the [binder/postBuild](https://github.com/nicole-brewer/jupyterlab-ide/tree/main/binder) script after you launch JupyterLab in order for the JupyterLab extensions to be enabled.
