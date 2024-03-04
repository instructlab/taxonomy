# Triaging Skills Pull Request Review Process:

- Triage is the practice of reviewing existing issues and pull requests (PR) to make sure they're relevant, actionable, and have all the information they need.

- Quick review, classify PRs that are/are not in line with the following criteria

### APPROVE Description                                                                                        
--------------------------------------------------------------------------------------------------- 
   * Generation seeds (success!)
   * Meets all criteria


### FURTHER REVIEW Description
--------------------------------------------------------------------------------------------------- 
 * Needs more extensive edits
 * General "I Don't Know"
 * Safety tasks and skills should always be escalated to Akash’s team
 * Super interesting, warrants further study


### REJECT Description
--------------------------------------------------------------------------------------------------- 


  * Submitted knowledge not a skill. For example, troubleshooting on an uncommon IBM Storage Fusion error message. 
  * Obviously GPT answer, blocklist. 
  * Couldn’t verify that the model actually lacks the skills — i.e. model can already answer the submitted questions well 
     enough. 
 * Provide examples of model response is too short and neglected reasoning details. For example: A logical question 
    requires multi-step reasoning to reach to the final answer. The submitted model response only gives the final answer. 
 * Uninformative examples. For example, not all examples match the skill requested; Or the user didn’t put three 
    independent question/answer pairs for the skill, but mistakenly submitted three chat turns for the three 
    questions/answer pairs. Or overly repetitive examples which do not help to clear define of the requested skill. 
 * Missing examples: didn’t provide desired model response for the skill. 


### OTHER Description
--------------------------------------------------------------------------------------------------- 
 * If it can do the primary task, but it misses some minor instruction, then reject the PR but save the data for later analysis* 
 * It can do the task by minor style or opinion details.* 
 * Wrong skill type (e.g. pure Math, code)

