**_A repository for contributing a "HELLO WORLD" program in any of the programming languages you know Or can Create a File With some Info about You_**

## **Not Comfortable With CMD ??**

No issue [Click HERE](Practice-2.md)

## **Comfortable With CMD ??**

_This is all Yours_

## How to Contribute: 👨🏻‍💻

1. Star the Project.
2. Fork the project.<br>
   <img height="100px" width="auto" src="./images/fork.png"></img>
3. Make any changes in your forked repo (This will Create a new Remote repo in your Dashboard)
4. Make Some changes
5. On this repo, click `Pull Requests` and raise a `Pull Request` selecting your fork on the right drop down

Questions can be asked by raising an `Issue`.

## What is forking?

When we love someone’s repository and would like to have it in our GitHub account, we fork it so that we can work with it separately.

When we fork a repository, we get an instance of that entire repository with its whole history. After forking, we can do whatever we want to do without affecting the original version.

## How to clone repo and make changes locally: ✂📋

- Download [GIT](https://git-scm.com/downloads) and Install

```
  click on the clone button (green in colour). This gives you a copy of the project. Its now yours to play around with
```

- Using git on your local machine. Do this to download the forked copy of this repo to your computer

```
  git clone https://github.com/yourGitHubUsername/Learn-Git-Github.git
```

- switch to the cloned folder. This can be done with Git Bash or the integrated terminal in the VSCode editor

```
  cd Learn-Git-Github
```

- Make a new branch. Your name would make a good branch because it's unique

```
  git checkout -b <name of new branch>
```

- Open the Contributors folder inside that create a folder of your Name(_Your Name_). Add all the files of the HELLO WORLD program inside the folder of your name.<br>
  eg:<br>

  ```bash
    print("Hello World !")
    print("I am <YourName>")
    print("I am From <Place>")
    print("I am <Your College Name and Year of Study>")
    print("Email ID : <Your Email>")
    print("Github : <Your Github>")
  ```

- Stage your changes

  - For example, if you have added 1 file
    ```
    git add "./Contributors/*Your Name*/Hello.txt"
    ```
  - If there are many files, to add all the files use
    ```
    git add "./Contributors/*Your Name*/."
    ```

- Commit the changes

```
  git commit -m "Initial commit"
```

- Check the status of your repository

```
  git status
```

- Pushing your repository to github

```
  git push origin <name of your branch>
```

- Pulling your request. Click on the Pull requests tab on the forked github repository.
  - **_Note : A pull request allows your changes to be merged with the original project._**

```
  Click on Pull Request
```

- Wait for your changes to be merged
  - You may Also Get Comments 😉 This will Help you To understand the Workflow
- Voila! You successfully made a contribution. 😉
