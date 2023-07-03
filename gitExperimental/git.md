# JupyterLab Git Tutorial

This tutorial is about the Git extension for JupyterLab. More than likely, you've seen Git before, so this is not a tutorial on how to use Git for version control or any such thing. Rather, this is a brief tutorial on the main features of the Git extension, focusing especially on the diff features for notebooks.

## Branches

For the sake of learning how this extension works, you will create a new branch. On the same sidebar as your file browser, you will see a button that looks like the Git logo:

<img
     style="display: block;
            margin-left: auto;
            margin-right: auto;
            width: 5%;"
     src="https://cdn3.iconfinder.com/data/icons/social-media-2169/24/social_media_social_media_logo_git-64.png"
/>

Click on that button and you should have a new tab pop up with information about the repository you are on (it should be "jupyterlab-ide" or something similar) and its various branches. In this tab, you can hide and show a selection pane for branches in the repository. You can select branches from this menu, merge two branches, or even delete branches while only using the buttons available from the menu.

Right now though, you should create a new branch and title it "gitExercise" using the <kbd>New Branch</kbd> button.

## Changes

Now that you have created a new branch, it's time to do something interesting on it. If you haven't already, complete the Code Formatter tutorial because this example requires knowledge of using the Code Formatter extension included in this repository.

First, go to the ```gitExample.ipynb``` file in the ```gitExtension``` folder and open it. This file is an example workflow borrowed from [Kaggle](https://www.kaggle.com/).<sup>[1](#kagglebook)</sup> To make changes to the notebook, we will format it with our different code formatters. To start, select every cell in the notebook and, using the <kbd>Edit</kbd> tab

Add and remove files from being committed
- Show that ```git add <file> <file>``` is frustrating
- Compare to ```git commit -m ""```
- Mention the description section as a nice feature compared to ```git commit -m "" -m ""``` or ```git commit``` with several lines

## Changes and History

Go over Changes and History
- Compare the Changes tab to ```git status```
- Compare the History tab to ```git log```



Go over diffing with the git extension
- Use both notebook and file examples
- For the notebooks, use the code formatter extension for help

Go over reverting changes in the History tab

<a name="kagglebook">1</a>: Example

[Citation style](https://academia.stackexchange.com/questions/171172/how-can-i-cite-a-kaggle-dataset-in-ieee-conference-paper#:~:text=There%20was%20a%20solution%20and%20that%20was%3A%20%5BDataset,Retrieved%20%5BDate%20Retrieved%5D%20from%20%5BURL%20of%20the%20dataset%5D.)

The example is from this notebook:

Title: EDA on Data Science Salaries 📊

Author Account: randomarnab

[Link](https://www.kaggle.com/code/arnabchaki/eda-on-data-science-salaries)

Some alterations have been made so that users can see the differences between differently formatted versions of the document. The only alterations are to code formatting.