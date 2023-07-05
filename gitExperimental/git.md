# JupyterLab Git Tutorial
#### Version 0.41.0

This tutorial is about the Git extension for JupyterLab. More than likely, you've seen Git before, so this is not a tutorial on how to use Git for version control or any such thing. Rather, this is a brief tutorial on the main features of the Git extension, focusing especially on the diff features for notebooks.

### Branches

For the sake of learning how this extension works, you will create a new branch. On the same sidebar as your file browser, you will see a button that looks like the Git logo:

<img
     style="display: block;
            margin-left: auto;
            margin-right: auto;
            width: 5%;"
     src="https://cdn3.iconfinder.com/data/icons/social-media-2169/24/social_media_social_media_logo_git-64.png"
/>

Click on that button and you should have a new tab pop up with information about the repository you are on (it should be "jupyterlab-ide" or something similar) and its various branches. In this tab, you can hide and show a selection pane for branches in the repository. You can select branches from this menu, merge two branches, or even delete branches while only using the buttons available from the menu.

#### Exercise 1: Create a Branch

You should create a new branch and title it "gitExercise" using the <kbd>New Branch</kbd> button. Using this branch, you can see even more of the features of the Git extension.

### Changes

Now that you have created a new branch, it's time to do something interesting on it. If you haven't already, complete the Code Formatter tutorial because this example requires knowledge of using the Code Formatter extension included in this repository.

First, go to the ```gitExample.ipynb``` file in the ```gitExtension``` folder and open it. This file is an example workflow borrowed from [Kaggle](https://www.kaggle.com/).<sup>[1](#kagglebook)</sup> To make changes to the notebook, we will format it with our different code formatters. To start, select every cell in the notebook and, using the <kbd>Edit</kbd> tab, format the whole notebook with the Black code formatter and save the file. This formatted notebook is a serious change from the original and should be committed as a change to your new branch.

#### Exercise 2: Commit Changes

Rather than opening up a terminal and using:
- ```git status``` to see what files have been changed
- ```git add <file> <file> ...``` to stage those changes
- ```git commit -m "<message>"``` to commit those changes

you can just go to the <kbd>Changes</kbd> tab in Git extension menu and go to the files in the "Changed" drop down. You will see the ```gitExample.ipynb``` file and, mousing over it, several different options. If you hit the <kbd>+</kbd> button, the changes made will be staged. Use this to stage the changes you made to ```gitExample.ipynb```.

Once they are staged, you can go to the text boxes at the bottom of the Git extension menu and enter both a summary of the changes AND a description of those changes. Add a summary of the changes however you want to describe it and add a description about which code formatter you used (Black) on which file (```gitExample.ipynb```) and the reason you did it (for this tutorial exercise). Once you have finished, commit the changes using the <kbd>Commit</kbd> button below the text fields. This will allow us to use the extension to check and manipulate version history.

### History

Now that you have committed changes on a branch, go to the <kbd>History</kbd> tab. This tab displays all the different changes to history of a branch, including mergers, in an interactive menu. Compared to the different ways to use ```git log```, with the ```--graph``` and ```--oneline``` options especially, this interface is cleaner to use and more intuitive. If you click on any of the different commits listed, you can see a drop down tab displaying which files were modified and you can view the file changes as well.

#### Exercise 3: View and Revert Changes

Usually, if you wanted to view and revert changes made to a file, you would have to go to the terminal and use:
- ```git diff [<commit> [<commit>]] [--<options>] [<path>…​]``` to see diffs for most files
- ```nbdiff-web [<commit> [<commit>]] [<path>]``` to see diffs for notebooks
- ```git revert <commit>``` to revert changes from one commit

In the Git extension, start by examining the commit you made earlier. By opening the drop down tab, you should see a "Changed" files section, with ```gitExample.ipynb``` underneath it. Right next to it, there should be a button that says "View file changes" when you mouse over it. Click it and, once the differences have been calculated, JupyterLab will have an interactive tab displaying the differences between the notebook before it was formatted and the notebook after it was formatted. Take a look and see what is different, which things were formatted and, if you want, which things were not. Notice how different this is from looking over changes to a notebook in the terminal.

Once you have finished looking over the changes to the file, look at the Git extension tab and look at the commit history. Opposing the "Changed" files label, there are two buttons that will either revert or reset changes. The finer details of version control don't need to be discussed here right now. For now, click the button that will revert the changes from the commit you made in the previous exercise. This will create a new commit that will reverse each and every change made to any of the files.

#### Exercise 4: Practice Makes Perfect

Now that you've made a commit, viewed the changes, and reverted the changes, do this one more time. Using the Code Formatter extension, format ```gitExample.ipynb``` with the YAPF formatter and make a commit with those changes. Look over the differences in that commit from the YAPF formatter. Once you're done with that, reset the changes one last time.

#### Exercise 5: Branch Merging

Now that you have learned the basics of manipulating commits in a branch through the Git extension, the last task you have is to merge two branches together. Using the console, you would have to use:
- ```git checkout <branch>``` to select the branch you want to merge into
- ```git merge <branch>``` to merge a feature branch into, usually, the main branch

Going back to the <kbd>Branches</kbd> tab of the Git extension, switch into the main branch by clicking on it. Now that you are in the main branch, you can merge the "gitExtension" branch into the main branch by mousing over the gitExtension branch and clicking the merge button.

### Congratulations!

You have now completed the Git extension tutorial! If you want to learn more about the awesome work that the Git extension team is doing, here is the link for the [repository](https://github.com/jupyterlab/jupyterlab-git).

# Acknowledgments

#### <a name="kagglebook">1</a>: randomarnab. (May 2023) EDA on Data Science Salaries 📊, retrieved July 5th, 2023 from https://www.kaggle.com/code/arnabchaki/eda-on-data-science-salaries