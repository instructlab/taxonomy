# Contributing

👍🎉 First off, thank you for taking the time to contribute! 🎉👍

The following is a set of guidelines for contributing. These are just guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request. Please read the [Community Contribution Guide](https://github.com/instructlab/community/blob/main/CONTRIBUTING.md) first for general practices for the InstructLab community.

## What Should I Know Before I Get Started?

### Code of Conduct

This project adheres to the [Contributor Covenant](https://github.com/instructlab/community/blob/main/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

Please report unacceptable behavior to one of the [Maintainers](https://github.com/instructlab/community/blob/main/MAINTAINERS.md).

### Related repositories

In addition to this repository, InstructLab has two related repositories:

- [CLI](https://github.com/instructlab/instructlab). This repository is responsible for the the `ilab` command-line interface (CLI) tool.
- [Community](https://github.com/instructlab/community). This repository is responsible for showing collaboration details across the InstructLab community.

The following sections provide a general overview for contributing to the Taxonomy repository.

## Ways of contributing to the taxonomy repository

### Contributing skills and knowledge

You can contribute to the taxonomy in the following two ways:

1. Adding new examples to **existing leaf nodes**:

    - Go to the corresponding leaf node / end of the branch and modify the YAML
    - Add a new example to the `qna.yaml` files as a new entry to the list

2. Adding **new branches/skills** corresponding to the existing domain:

    - You can add new folders under the corresponding category (replace any spaces with underscores `_`)
    - Create a new `qna.yaml` file containing examples for the new skill

A detailed contribution guide is documented in the [How can I contribute section](#how-can-i-contribute) section.

### Contributing new features, enhancements or documentation

Help on open source projects is always welcome and there is always something that can be improved. For example, documentation (like the text you are reading now) can always use improvement, code can always be clarified, variables or functions can always be renamed or commented on, and there is always a need for more test coverage. If you see something that you think should be fixed, take ownership! Here is how you get started:

To propose a new feature, it's best to raise an issue in the appropriate repository. This way, features can be discussed with the project maintainers, ensuring that your time is not wasted working on a feature that the project developers will not accept into the codebase.

*How Do I Submit A (Good) Enhancement or Improvement item?:* Enhancements and improvement items suggestions are tracked as [GitHub issues: Proposal](https://github.com/instructlab/taxonomy/issues/new?assignees=&labels=&projects=&template=proposal.md&title=). Create an issue and provide the information suggested in the proposal template.

## How do I start contributing?

The following workflow is designed to help you begin your first contribution journey. It will guide you through creating and picking up issues, working through them, having your work reviewed, and then merging.

### How Can I Contribute?

The goal of InstructLab is to enable true collaborative development around common Large Language Models (LLMs) using a technology that enables collaboration following standard open source development practices. A general overview of making a contribution to this project consists of writing an extension to the existing taxonomy, making a pull request, and getting your work reviewed and merged so that it can benefit the whole community.

Before you start, review the [open issues](https://github.com/instructlab/taxonomy/issues) and [opened pull requests](https://github.com/instructlab/taxonomy/pulls) board to see if your contribution or enhancements are already proposed. You might instead be able to join forces with them by providing input to what they have started. If you are unsure about what kind of skill or knowledge to contribute, you can [open an issue](https://github.com/instructlab/taxonomy/issues/new?assignees=&labels=&template=proposal.md&title=) first to discuss your proposal idea with the maintainers.

To contribute to this repo, you'll use the *Fork and Pull* model common in many open source repositories. You can follow this process in a local terminal or in the GitHub web UI.

- For details on the local process, check out the [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) documentation from GitHub and [The GitHub Workflow Guide](https://github.com/kubernetes/community/blob/master/contributors/guide/github-workflow.md) documentation from Kubernetes.
- For details on contributing using the GitHub webpage UI, see [Contributing using the GH UI](docs/contributing_via_GH_UI.md).

> [!IMPORTANT]
> For all contributions to InstructLab 🐶, you want to become familiar with the workflow described in the [InstructLab 🐶 CLI
> `ilab`](https://github.com/instructlab/instructlab) documentation. It would be best to understand how to test
> your changes, generating new data, training and downloading the new model, and testing it to check that it gives you the desired results.

When your contribution is ready, you can create a pull request (PR). In general, we follow the standard [GitHub pull request](https://help.github.com/en/articles/about-pull-requests) process. Follow the template to provide details about your pull request to the maintainers. Before submitting pull requests, make sure your changes pass applicable formatting tests in the repository CI.

>[!NOTE]
> Always refer to the [README.md](https://github.com/instructlab/taxonomy/blob/main/README.md)
> if you are unsure on how to format your contributions.
>
### What can I contribute?

You can contribute [Knowledge](https://github.com/instructlab/taxonomy/blob/main/README.md#getting-started-with-knowledge-contributions) or [Skills](https://github.com/instructlab/taxonomy/blob/main/README.md#getting-started-with-skill-contributions) to the taxonomy tree. Make sure to review the [general documentation](README.md) for a detail explanation of these concepts and the differences between the two.

> [!IMPORTANT]
> You can only contribute original material. **DO NOT** contribute copyrighted content or content coming from another system.

### Submitting your contribution

When submitting your PR, give it a title which is as explicit as possible. Include in the description of the PR on GitHub, both what the system gave you before your contribution and what it gives you with your contribution.

### Pull request review

Once you've [created a pull request](#how-can-i-contribute), maintainers will review your proposed addition and may make suggestions to fix before merging. It will be easier for your pull request to receive reviews if you consider the criteria the reviewers follow while working. Remember to:

- Run tests locally and ensure that they pass
- Ensure your contribution is in the proper format (`ilab generate` shouldn't report any warnings or errors)
- Break large changes into a logical series of smaller patches, which are easy to understand individually and combine to solve a broader issue
- Follow the project coding conventions
- Include the DCO sign off; see [Legal](#legal)

The project maintainers use `LGTM` (Looks Good To Me) in comments on the code review to indicate acceptance. You can see more information on the triaging process in the [Triaging skills](https://github.com/instructlab/taxonomy/blob/main/docs/triaging/triaging-contributions.md) documentation.

For a list of the maintainers and triagers, see the [MAINTAINERS.md](https://github.com/instructlab/community/blob/main/MAINTAINERS.md) page.

## Submitting bugs

To submit a new bug, raise an issue in the appropriate repository before creating a pull request. This ensures that the issue is properly tracked. To fix an existing bug, assign yourself a bug from the issues page of the desired repository. Then, submit a pull request for review.

Bugs are tracked as [GitHub issues using the Bug Report template](https://github.com/instructlab/taxonomy/issues/new?assignees=&labels=&template=bug_report.md&title=). Create an issue on that and provide the information suggested in the bug report issue template.

## Legal

We have tried to make it as easy as possible to make contributions.
This applies to how we handle the legal aspects of contribution.
We use the same approach - the [Developer's Certificate of Origin 1.1 (DCO)][DCO] - that [the Linux Kernel community uses][Linux-DCO] to manage code contributions. All contributions that leverage third-party content should either come from the public domain or be licensed with an open data license that does not restrict commercial use or the creation of derivative works, including the following license types:

- CC0-1.0
- CDLA-Permissive-2.0
- CC-BY-4.0
- CC-BY-SA-4.0
- Apache-2.0
- MIT

Any third-party content contributed to this project undergoes modifications in order to formulate it in the templated format required for submission to this project.

We simply ask that when submitting a patch for review, the developer must include a sign-off statement in the commit message.

Here is an example `Signed-off-by` line, which indicates that the submitter accepts the DCO:

```text
Signed-off-by: John Doe <john.doe@example.com>
```

You can include this automatically when you commit a change to your local Git repository using the following command:

```shell
git commit -s
```

> [!TIP]
> If you created a commit message that did not include the `-s` option, you can edit your original commit message by using the `git commit -s --amend` command. Ensure you force push the amended commit to your pull request (PR).

### License

Unless specifically stated, this project is
distributed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

SPDX-License-Identifier: [Apache-2.0](https://spdx.org/licenses/Apache-2.0)

For more details, see the [LICENSE](LICENSE).

### For your attribution.txt file

An important part of contributing to the InstructLab project is citing your sources of information. This comes in the form of your `attribution.txt` that you add to the pull requests. Almost all instances of attribution can be covered by the parameters required for Creative Commons Attribution licenses. Some parameters are as follows:

- Title of work
- Link to work
- Include link to a specific revision where possible
- License of the work
- Include an SPDX identifier where possible
- Creator names
- Copyright information
- Modification information
- Indicate if work was itself derived from another openly licensed work

You can also see this citation style in the [Data sources documentation](https://github.com/instructlab/community/blob/main/docs/DataSources.md)

## Development

Please consult the [`ilab` documentation](https://github.com/instructlab/instructlab) to set up your environment.

[DCO]: https://developercertificate.org/
[Linux-DCO]: https://docs.kernel.org/process/submitting-patches.html#sign-your-work-the-developer-s-certificate-of-origin
