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

Click on that button and you should have a new tab pop up with information about the repository you are on and its various branches.

Go over Branches
- Go over how to create a new branch under the branches button
- merge branches
- delete branches

Go over Changes and History
- Compare the Changes tab to ```git status```
- Compare the History tab to ```git log```

Add and remove files from being committed
- Show that ```git add <file> <file>``` is frustrating
- Compare to ```git commit -m ""```
- Mention the description section as a nice feature compared to ```git commit -m "" -m ""``` or ```git commit``` with several lines

Go over diffing with the git extension
- Use both notebook and file examples
- For the notebooks, use the code formatter extension for help

Go over reverting changes in the History tab

## Example

The example is from this notebook:

Title: EDA on Data Science Salaries 📊

Author Account: randomarnab

[Link](https://www.kaggle.com/code/arnabchaki/eda-on-data-science-salaries)

Some alterations have been made so that users can see the differences between differently formatted versions of the document. The only alterations are to code formatting.