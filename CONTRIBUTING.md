# Contributing

👍🎉 First off, thank you for taking the time to contribute! 🎉👍

The following is a set of guidelines for contributing. These are just guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request. Please read the [community contribution guide](https://github.com/instruct-lab/community/blob/main/CONTRIBUTING.md) first for general practices for the InstructLab community.

## What Should I Know Before I Get Started?

### Code of Conduct

This project adheres to the [Contributor Covenant](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

Please report unacceptable behavior to one of the [Maintainers](./MAINTAINERS.md).

### How Do I Start Contributing?

The below workflow is designed to help you begin your first contribution journey. It will guide you through creating and picking up issues, working through them, having your work reviewed, and then merging.

Help on open source projects is always welcome and there is always something that can be improved. For example, documentation (like the text you are reading now) can always use improvement, code can always be clarified, variables or functions can always be renamed or commented on, and there is always a need for more test coverage. If you see something that you think should be fixed, take ownership! Here is how you get started:

## How Can I Contribute?

The whole point of InstructLab 🥼 is to enable true collaborative development around common Large Language Models (LLMs.) using a technology that enables collaboration following standard open source development practices.

So, the general gist of making a contribution to this project consists of writing an extension to the existing taxonomy, make a pull request, and your work will be reviewed and merged so that it can benefit the whole community.

Before investing time into developing a contribution, it's best to [open an issue](https://github.com/instruct-lab/taxonomy/issues/new?assignees=&labels=&template=proposal.md&title=) first to discuss your proposal idea with the maintainers.

You should also review what others have already proposed, in open issues and pull requests, to avoid duplicating efforts. You might instead be able to join forces with them by providing input to what they have started.

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

### Submitting your contribution

When submitting your PR, give it a title which is as explicit as possible, and include in the description of the PR on GitHub both what the system gave you before your contribution and what it gives you with your contribution.

#### PR Review

Once you've [created a pull request](#how-can-i-contribute), maintainers will review your proposed addition and may make suggestions to fix before merging. It will be easier for your pull request to receive reviews if you consider the criteria the reviewers follow while working. Remember to:

- Ensure your contribution is in the proper format (`lab generate` shouldn't report any warnings or errors)
- Break large changes into a logical series of smaller patches, which are easy to understand individually and combine to solve a broader issue

#### Legal

We have tried to make it as easy as possible to make contributions.
This applies to how we handle the legal aspects of contribution.
We use the same approach - the [Developer's Certificate of Origin 1.1 (DCO)][DCO] - that [the Linux Kernel community uses][Linux-DCO] to manage code contributions.

For this project, unless the file says otherwise, or unless the attributed source provided in the file says otherwise, the relevant open source license is [the Apache License, Version 2.0](LICENSE).
All contributions that leverage third party content should either come from the public domain or be licensed with an open data license that does not restrict commercial use or the creation of derivative works, including the following license types:

- CC0-1.0
- CDLA-Permissive-2.0
- CC-BY-4.0
- Apache-2.0
- MIT

Any third party content contributed to this project undergoes modifications in order to formulate it in the templated format required for submission to this project.

We simply ask that when submitting a patch for review, the developer must include a sign-off statement in the commit message.

Here is an example `Signed-off-by` line, which indicates that the submitter accepts the DCO:

```
Signed-off-by: John Doe <john.doe@example.com>
```

You can include this automatically when you commit a change to your local git repository using the following command:

```shell
git commit -s
```

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

[DCO]: https://developercertificate.org/
[Linux-DCO]: https://docs.kernel.org/process/submitting-patches.html#sign-your-work-the-developer-s-certificate-of-origin
