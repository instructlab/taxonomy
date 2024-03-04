# Contributing

👍🎉 First off, thank you for taking the time to contribute! 🎉👍

The following is a set of guidelines for contributing. These are just guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request. Please read the [community contribution guide](https://github.com/instruct-lab/community/blob/main/CONTRIBUTING.md) first for general practices for the InstructLab community.



## What Should I Know Before I Get Started?

### Code of Conduct

This project adheres to the [Contributor Covenant](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

Please report unacceptable behavior to one of the [Maintainers](./MAINTAINERS.md).

### Why should I contribute?

This taxonomy repository will be used as the seed to synthesize the training
data for InstructLab-trained models. We intend to re-train the model(s) using the main
branch as often as possible (at least weekly). This enables fast iteration of the model(s), for the benefit of the open source community, in particular to enable model developers who do not have access to the necessary compute infrastructure.


### How Do I Start Contributing?

The below workflow is designed to help you begin your first contribution journey. It will guide you through creating and picking up issues, working through them, having your work reviewed, and then merging.

Help on open source projects is always welcome and there is always something that can be improved. For example, documentation (like the text you are reading now) can always use improvement, code can always be clarified, variables or functions can always be renamed or commented on, and there is always a need for more test coverage. If you see something that you think should be fixed, take ownership! Here is how you get started:

## How Can I Contribute?

The whole point of InstructLab 🥼 is to enable true collaborative development around common Large Language Models (LLMs.) using a technology that enables collaboration following standard open source development practices.

So, the general gist of making a contribution to this project consists of writing an extension to the existing taxonomy, make a pull request, and your work will be reviewed and merged so that it can benefit the whole community.

If you're planning on making a large addition or if you find a problem with the existing taxonomy, it's best to [write an issue](https://github.com/instruct-lab/cli/issues/new?assignees=&labels=&template=feature_request.md&title=) first to discuss it with maintainers.

To contribute to this repo, you'll use the Fork and Pull model common in many open source repositories. For details on this process, check out [The GitHub Workflow
Guide](https://github.com/kubernetes/community/blob/master/contributors/guide/github-workflow.md)
from Kubernetes.

For contributions to InstructLab 🥼, you will want to become familiar with the workflow described in the [How to use InstructLab 🥼 CLI `lab`](https://github.com/instruct-lab/cli?tab=readme-ov-file#how-to-use-lab) documentation. In particular, you need to understand how to test your changes going through the steps to generate new data, training and downloading the new model, and testing it to check that it gives you the desired results.

When your contribution is ready, you can create a pull request. Pull requests are often referred to as "PR". In general, we follow the standard [GitHub pull request](https://help.github.com/en/articles/about-pull-requests) process. Follow the template to provide details about your pull request to the maintainers.

Before submitting pull requests, make sure your changes pass applicable formatting tests.

## What can I contribute?

You can contribute either Knowledge or Skills to the taxonomy. Make sure to review the [general documentation](README.md) for a detail explanation of these concepts and the differences between the two.

You can then either:
- add new examples to existing leaf nodes by expanding the corresponding qna.yaml files
- or add new branches by creating new folders under existing ones and creating new qna.yaml files

**Note** that you can only contribute original material. **DO NOT** contribute copyrighted content or content coming from another system. 


## Ways to Contribute

You can contribute to the taxonomy in the following two ways:

1. Adding new examples to **existing leaf nodes**:
    - Go to the corresponding leaf node / end of the branch and modify the yaml
    - Add new examples to the qna.yaml files as a new entry to the list
- Adding new branches/skills corresponding to the existing domain:
1. Adding **new branches/skills** corresponding to the existing domain:
    - You can add new folders under the corresponding category
    - Create a new qna.yaml file with examples for the new skill

## Contribute knowledge and skills to the taxonomy!

The ability to contribute to a large language model (LLM) has been difficult in no small part because it is difficult to get access to the necessary compute infrastructure.

This taxonomy repository will be used as the seed to synthesize the training data for InstructLab-trained models. We intend to re-train the model(s) using the main branch following InstructLab's progressive training on a nightly basis. This enables fast iteration of the model(s), for the benefit of the open source community. 

By contributing your skills and knowledge to this repository, you will see your changes built into an LLM within days of your contribution rather than months or years! If you are working with a model and notice its knowledge or ability lacking, you could correct it by contributing knowledge or skills and check if it's improved once your changes are built in a nightly build.

### Detailed Contribution Instructions

#### Pre-requisites:
- You need a GitHub account
- You need access to this repo

#### Make a copy of the taxonomy repo

1. Go to [github.com/instruct-lab/taxonomy](github.com/instruct-lab/taxonomy)
2. Press the Fork button in the upper right:
   ![fork-button](https://github.com/instruct-lab/taxonomy/assets/799683/8487bff2-425e-483c-b27c-ef03da1c57a8)
3. On the "Create a new fork" form:
   - **Repository name:** `taxonomy` is fine
   - **Description:** Please describe the skill your skill provides. Give an example question it could answer with your contributed knowledge, or an example prompt your skill will improve.
   - **Copy the main branch only:** It's OK to leave this checked on.

When you are ready, press the **Create Fork** button.

![Screenshot from 2024-02-28 12-41-59](https://github.com/instruct-lab/taxonomy/assets/799683/656608ef-3040-4858-96f0-9b695bea0e8f)

4. You will get a copy of the taxonomy repo in your github account. This is your own copy, so don't worry about making mistakes or anything like that. *(If you do end up making a mistake and want to start over: you can delete the fork and create a new fork.)*


#### Contributing a skill

In the screenshot, you can see we are under the compositional skills directory. This is the directory under which you want to contribute skills. (The other top-level directory you can contribute to is the knowledge directory, which is a little different than skills. You can read more about the difference between skills and knowledge [in that section of this README](#k-vs-s) above.)

![Screenshot from 2024-02-28 12-44-05](https://github.com/instruct-lab/taxonomy/assets/799683/2038e035-5400-4848-91fb-f575db35b565)

Based on the directories that exist in the tree, make a best guess at where in the tree structure you feel the skill you have to contribute best fits. If you get to a point where you've gone deep enough into the tree and you can't find any directories that match, please feel free to create a new directory or a directory and subdirectories to best represent your skill.

For example, I'd like to contribute a skill for creating puns. Puns are a specific type of joke. I started out in the writing directory of the tree, and saw two main directories there:

![Screenshot from 2024-02-28 12-57-00](https://github.com/instruct-lab/taxonomy/assets/799683/2fab5b92-194a-491e-8a6f-f464a8e8f2f5)

When I looked at the directories under freeform, I saw subdirectories such as brainstorming, debate, legal, poetry, prose, etc.:

![Screenshot from 2024-02-28 12-57-35](https://github.com/instruct-lab/taxonomy/assets/799683/e52ea423-d86f-49a8-9229-b09418f1510b)

When I looked under grounded, I saw subdirectories such as editing, meeting_insights, summarization/wiki_insights:

![Screenshot from 2024-02-28 12-59-10](https://github.com/instruct-lab/taxonomy/assets/799683/98370d70-d7e4-4595-a259-f6ffa4ef00fb)

Puns seemed to fit best under the freeform directory, but I didn't think they fit under any of the pre-existing directories under freeform, so I created a jokes directory, then I created a puns directory under jokes. (I started with jokes as a directory, because I also have a knock-knock joke skill I'd like to create. 🙂)

It can be a little tricky mechanically to create directories in GitHub's web UI:

* Navigate to the folder in which you want to create the directory inside of.
* Click the "Add File" dropdown button in the upper right corner of the screen.
* Start typing the name of the first directory you want to create. In the animation below we use "jokes/" as the first directory.
* When you type the "/" character, the directory name will "lock in" and you'll be able to type the next of the next subdirectory under it, as desired. Below we typed "knock-knock/" as the next directory name.
* Finally, you'll type the file name. The file name should always be qna.yaml. (qna stands for "Question aNd Answer.")  

Here's an animated graphic to show how it works:

![screencast-directory-naming](https://github.com/instruct-lab/taxonomy/assets/799683/2cb2b031-52f6-46de-bfd9-c4eae82ec9d3)

**TO BE CONTINUED**

### Submitting your contribution

When submitting your PR, give it a title which is as explicit as possible, and include in the description of the PR on GitHub both what the system gave you before your contribution and what it gives you with your contribution.

#### PR Review

Once you've [created a pull request](#how-can-i-contribute), maintainers will review your proposed addition and may make suggestions to fix before merging. It will be easier for your pull request to receive reviews if you consider the criteria the reviewers follow while working. Remember to:

- Ensure your contribution is in the proper format (`lab generate` shouldn't report any warnings or errors)
- Break large changes into a logical series of smaller patches, which are easy to understand individually and combine to solve a broader issue

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report ✏️, reproduce the behavior 💻, and find related reports 🔎.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues using the Bug Report template](https://github.com/instruct-lab/taxonomy/issues/new?assignees=&labels=&template=bug_report.md&title=). Create an issue on that and provide the information suggested in the bug report issue template.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features, tools, and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion ✏️ and find related suggestions 🔎

#### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues using the Feature Request template](https://github.com/instruct-lab/taxonomy/issues/new?assignees=&labels=&template=feature_request.md&title=). Create an issue and provide the information suggested in the feature requests or user story issue template.

#### How Do I Submit A (Good) Improvement Item?

Improvements to existing functionality are tracked as [GitHub issues using the User Story template](https://github.com/instruct-lab/Taxonomy/issues/new?assignees=&labels=&template=user_story.md&title=). Create an issue and provide the information suggested in the feature requests or user story issue template.

## Development

Please consult the [CLI documentation](https://github.com/instruct-lab/cli) to set up your environment.
