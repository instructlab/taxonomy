# Triaging Skills pull request contribution process:
Skills triagers should review open pull requests to the taxonomy repo looking to apply one of the following labels to the PR:

* approved
* rejected
* needs-further-review

### Approved:

- meets requirements

### Rejected:

- Submitted knowledge not a skill. For example, troubleshooting on an uncommon IBM Storage Fusion error message. 
- Obviously GPT answer, blocklist. 
- Couldn’t verify that the model actually lacks the skills — i.e. model can already answer the submitted questions well enough. 
- Provide examples of model response is too short and neglected reasoning details. For example: A logical question requires multi-step reasoning to reach to the final answer. The submitted model response only gives the final answer. 
- Uninformative examples. For example, not all examples match the skill requested; Or the user didn’t put three independent question/answer pairs for the skill, but mistakenly submitted three chat turns for the three questions/answer pairs. Or overly repetitive examples which do not help to clear define of the requested skill. 
- Missing examples: didn’t provide desired model response for the skill. 

### Needs futher review:

- Triager is generally not sure
- Safety tasks and skills should always be escalated to Akash’s team
- Super interesting, warrants further study
1. Quick review, throw out people who didn’t follow instructions (PR Wrangling)
1. Deeper review, taking notes and making minor edits as needed. Potential places that a PR can be triaged into: (PR Ting)
	* Generation seeds (success!!)
	* Training 
		* if there is no explanation of the answer, then it mixtral can’t handle it and it should go into the training data (assuming everything else is fine)
		* if it is overly templated (and we don’t want the model to memorize that pattern)
	* Needs more extensive edits
	* Needs further review
		* General IDK
		* Safety tasks and skills should always be escalated to Akash’s team
		* Super interesting, warrants further study
	* Total reject:
		* Submitted knowledge not a skill. For example, troubleshooting on an uncommon IBM Storage Fusion error message. 
		* Obviously GPT answer, blocklist. 
		* Couldn’t verify that the model actually lacks the skills — i.e. model can already answer the submitted questions well enough. 
		* Provide examples of model response is too short and neglected reasoning details. For example: A logical question requires multi-step reasoning to reach to the final answer. The submitted model response only gives the final answer. 
		* Uninformative examples. For example, not all examples match the skill requested; Or the user didn’t put three independent question/answer pairs for the skill, but mistakenly submitted three chat turns for the three questions/answer pairs. Or overly repetitive examples which do not help to clear define of the requested skill. 
		* Missing examples: didn’t provide desired model response for the skill. 
		* Need clarification from Kate
			* ~[\#72](https://airtable.com/appmwxXCurh6B4on2/tblv0dKl3LtNvq0Dy/viwA2knaFDbgOACaV/rec9nbO1uzWjHu17b?blocks=hide)~: This looks like the expectation for model to know up-to-date fact (current currency conversion rate). 
			* ~[\#11](https://airtable.com/appmwxXCurh6B4on2/tblv0dKl3LtNvq0Dy/viwA2knaFDbgOACaV/rechobaH1J4drfoo4?blocks=hide)~: Not able to extract the right Json format is not a skill gap? 
			* *If it can do the primary task, but it misses some minor instruction, then reject the PR but save the data for later analysis* ← Hui: does this mean that the model already has the skill? 
			* *It can do the task by minor style or opinion details.* ← Hui: does this mean that the model already has the skill? 
			* *Wrong skill type (e.g. pure Math, code);* ← Hui: do we still reject all submission for math and code? 
1. Go through and systematically rewrite all of the skill descriptions (very few were written descriptively enough or in the right format)
1. Classify by high level taxonomy
1. Final edits and export to YAML
1. Organize YAMLs into taxonomy


#### Other Best Practices:
* Always good to provide step by step, especially for Math and Reasoning tasks 
* In API calling tasks, you need to provide descriptions of the API that you are trying to call
