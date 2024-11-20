# Docs

The purpose of these documents is to inform users and maintainers on the review/triaging process and different ways to contribute to the taxonomy repository. You can view the following:

- Full layout of taxonomy repository - [Taxonomy diagram](taxonomy_diagram.md)
- Flowchart of the pull request review process - [Review process](assets/review-process.png)
- Flowchart of how the backend works with reviewing PRS - [Backend process](assets/backend.png)

## Overview of the Review Process

The review process starts with contributor drafting the PR.

1. At the PR stage, reviewers manually check its contents (e.g. making sure the examples are added to the correct path, inspecting the contents of examples).
   - If not valid, go back to the contributor and ask them to take actions.
2. If a PR passes step 1, the SDG will be triggered to generate synthetic data samples.
   - If not valid, go back to the contributor and ask them to take actions.
3. If step 2 passes, it will be used in the next model update.

See the [README.md in `instructlab/docs`](https://github.com/instructlab/instructlab/blob/main/docs/README.md) on how to modify and render the flowcharts.

For more information on the review process, see [Pull request review in CONTRIBUTING.md](https://github.com/instructlab/taxonomy/blob/main/CONTRIBUTING.md#pull-request-review)

## Triaging documentation

For more information on triaging contributions pull requests, see:

- [Safe responses for common PR mistakes](triaging/safe-responses.md)
- [Triaging guide](triaging/triaging-contributions.md)

## Contributing documentation

For documentation contribution processes, see:

- [Contributing using the GitHub webpage UI](contributing_via_GH_UI.md)
- [Knowledge contribution guidelines](knowledge-contribution-guide.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
