# Contributing using the GitHub webpage UI

There are a few ways you can create pull requests in an open source project: Locally using the git CLI tool in your terminal or using the GitHub webpage user interface. The following instructions show you how to create a PR using the GitHub webpage UI 

## Prerequisites

- You have a GitHub account
- You have access to this repo

## Make a copy of the taxonomy repo

1. Go to [github.com/instructlab/taxonomy](https://github.com/instructlab/taxonomy).

2. Click **Fork** to fork your own copy of the repo.

    ![fork-button](https://github.com/instructlab/taxonomy/assets/799683/8487bff2-425e-483c-b27c-ef03da1c57a8)

3. On the **Create a new fork** page, enter the information into the following fields:
    - **Repository name:** Name your fork the same as the repository, in this case `taxonomy` is the name of your fork. 
    - **Description:** Enter the description of _your fork_, not of the skills you will create. You can write something that makes sense to you or leave it blank.
    - **Copy the main branch only:** The box is selected by default. You can choose to leave the box selected or clear it.

4. Click **Create Fork**.

    ![Screenshot from 2024-02-28 12-41-59](https://github.com/instructlab/taxonomy/assets/799683/656608ef-3040-4858-96f0-9b695bea0e8f)

You will get a copy of the taxonomy repo in your github account. This is your own copy, so don't worry about making mistakes. *If you do end up making a mistake and want to start over: you can delete the fork and create a new fork.*

## Contributing a skill

1. IMPORTANT: Before you begin, create a working branch for your contribution and name it whatever you like. This allows you to have an up-to-date `main` branch in your fork as well as a working branch to add any changes. 

2. Navigate to the directory where you want your knowledge or skill. The following image shows the compositional skills directory and its contents. Skills are contributed to this directory: 

    ![Screenshot from 2024-02-28 12-44-05](https://github.com/instructlab/taxonomy/assets/799683/2038e035-5400-4848-91fb-f575db35b565)

    The other top-level directory you can contribute to is the knowledge directory, which is used for knowlege contributions. You can read more about the difference between skills and knowledge in the [community documentation](https://github.com/instructlab/community/blob/main/docs/README.md).

3. Based on the directories that exist in the tree, make a best guess at where in the tree structure to add the skill that you want to contribute. If you get to a point where you've gone deep enough into the tree and you can't find any directories that match, create a new directory (and subdirectories, if needed) to best represent your skill.

    For example, I want to contribute a skill for creating puns. Puns are a specific type of joke. I started in the writing directory of the tree, and saw two main directories there: freeform and grounded. 

    ![Screenshot from 2024-02-28 12-57-00](https://github.com/instructlab/taxonomy/assets/799683/2fab5b92-194a-491e-8a6f-f464a8e8f2f5)

    Under the freeform directory, this example shows subdirectories such as brainstorming, debate, legal, poetry, prose, etc.

    ![Screenshot from 2024-02-28 12-57-35](https://github.com/instructlab/taxonomy/assets/799683/e52ea423-d86f-49a8-9229-b09418f1510b)

    Under the grounded directory, this example shows subdirectories such as editing, meeting_insights, summarization/wiki_insights.

    ![Screenshot from 2024-02-28 12-59-10](https://github.com/instructlab/taxonomy/assets/799683/98370d70-d7e4-4595-a259-f6ffa4ef00fb)

    Puns seemed to fit best under the freeform directory, but they didn't fit under any of the pre-existing directories under freeform, so I created a jokes directory. Under jokes, I created a puns subdirectory. By making jokes a directory, I can continue to add subdirectories for different types of jokes. For example, I can add a new subdirectory for the knock-knock joke skill that I want to create. 🙂

4. It can be a little tricky mechanically to create directories in GitHub's web UI, but you can complete the process using the following steps: 

    a. In the GitHub repo, click the folder that you want to create the new directory inside of.

    b. Click **Add File** and select **Create new file** from the menu.

    c. Type the name of the first directory that you want to create. In the example animation, we use "jokes/" as the first directory.

    > [!NOTE]
    > When you type the "/" character, the directory name will "lock in" and you'll be able to type the name of the subdirectory that you want to add under it. In the example, we typed "knock-knock/" as the subdirectory name.

    > [!NOTE]
    > Make sure to replace any spaces (` `) in the folder name with underscores (`_`)

5. After you have entered the name of all of the directories that you want to add, type the file name. The file name should always be `qna.yaml` (qna stands for "Question aNd Answer.")

Here's an animated graphic to show how it works:

![screencast-directory-naming](https://github.com/instructlab/taxonomy/assets/799683/2cb2b031-52f6-46de-bfd9-c4eae82ec9d3)

6. Verify that your YAML follows the proper structure. See [Knowledge: skills examples](https://github.com/instructlab/taxonomy/blob/main/README.md#knowledge-yaml-examples) and [Skills: YAML examples](https://github.com/instructlab/taxonomy/blob/main/README.md#skills-yaml-examples) to help with formatting. The [yamllint](https://www.yamllint.com/) tool is another great way to verify yaml. 