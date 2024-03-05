# Triaging Skills Pull Request Review Process:

- Triage is the practice of reviewing existing issues and pull requests (PR) to make sure they're relevant, actionable, and have all the information they need.
- Quick review, classify PRs that are/are not in line with the following criteria

### Skills contribution triaging process

1. Contributor installs [lmdk](https://github.com/instruct-lab/cli?tab=readme-ov-file#-installing-lab), runs model, identify gap, write skill to fill gap
1. Contributor opens pull request with necessary files
1. Skills triager reviews pull request
1. Skills triager marks pull request with appropriate determination as described below using one of the labels below

### APPROVE Description

label: `triage-approved`

Reasons for approval:

- Generation seeds (success!) <!-- TODO: what does this mean? -->
- Meets all criteria

### FURTHER REVIEW Description

label: `needs-further-review`

Reasons for needing further review:

- Needs more extensive edits
- General "I Don't Know"
- Safety tasks and skills should always be escalated to Akash’s team <!-- TODO: create a team for this? -->
- Super interesting, warrants further study

### NEEDS EDITING Description

label: `needs-editing`

Note: This categorization is for contributions that are good but not quite good enough and we can give guidance to the contributor to get review approval

Reasons for needing editing:

- Sent back to contributor to fix

### REJECT Description

label: `rejected`

Note: Skills triagers should try to include as much information as to why the contribution is rejected.

Reasons for rejection:

- Submitted knowledge not a skill. For example, troubleshooting on an uncommon IBM Storage Fusion error message.
- Obviously GPT answer, blocklist.
- Couldn’t verify that the model actually lacks the skills — i.e. model can already answer the submitted questions well enough.
- Provide examples of model response is too short and neglected reasoning details. For example: A logical question requires multi-step reasoning to reach to the final answer. The submitted model response only gives the final answer.
- Uninformative examples. For example, not all examples match the skill requested; Or the user didn’t put three independent question/answer pairs for the skill, but mistakenly submitted three chat turns for the three questions/answer pairs. Or overly repetitive examples which do not help to clear define of the requested skill.
- Missing examples: didn’t provide desired model response for the skill.

## OTHER Notes

- If it can do the primary task, but it misses some minor instruction, then reject the PR but save the data for later analysis\*
- It can do the task by minor style or opinion details.\*
- Wrong skill type (e.g. pure Math, code)
