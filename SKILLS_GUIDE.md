# Skills Guide

LLMs have inherent limitations that make certain tasks extremely difficult, like doing math problems. They're great at other tasks, like creative writing. And they could be better at things like logical reasoning.

## Building Your LLM Intuition

Consider these when you're generating skills. Skills in the first and second categories are welcomed. Skills in the third category are usually borderline and may be rejected.

### LLMs are great at

* Brainstorming
* Creativity
* Connecting information
* Cross-lingual behavior

### LLMs need help with

* Chains of reasoning
* Analysis
* Story plots
* Reassembling information
* Effective and succinct summaries

### LLMs are not so great at

* Math
* Computation
* "Turing-complete" type tasks
* Generating only true real-world information (they're prone to hallucinations)

## Accepted Skills

### Creative Writing / Poetics

Adding new types of documents and writing styles to the LLM are welcome. Consider:

* Song lyrics
* Soliloquies
* Five paragraph essays
* Arguments

### Learning to Format Information

Skills to better format and reassemble information are helpful.

### Table Analysis and Processing

Consider:
* Drawing verbal inferences and conclusions about what's in a table
* Sorting
* Selecting
* Joining

### Qualitative Inference and Chain-of-Thought Reasoning

e.g.
> Mary is taller than John.
> John is taller than Anna.
> Is Anna taller than Mary?

e.g.
> An elephant, a mouse and a horse are in a room. How would they be ordered if they were standing in order by size?

Great skills in this category should include the correct line of reasoning in the answer, not just what the answer is.

### Word Problems

Is your LLM smarter than a second grader?

### Trust and Safety

Please avoid HAP (hate, abuse and profanity) and PII (personal identifiable information) in your examples.

Anything related to trust and safety will be flagged for higher-level review.


### Searching, Extraction and Summarization

Skills to select odd information in a document, draw conclusions, pull out information, draw insights or generate TODOs from information provided in the "Context" field are welcome.

### Complex Rulesets and Games

> [!NOTE]
> This is a good example of the need for a _grounded skill_. Grounded skills require the user to provide context containing information that the model is expected to take into account during processing. This is different from _knowledge_, where the model is expected to gain facts and background knowledge from the tuning process.
> 
> Context added when tuning a grounded skill would need to be again provided by the end user at inference time. The skill here is better adherence to the rule set.
 
To add a skill for a structured game or other task with a complex rule set, use a grounded skill.

Add the rules to the game as "context" in every example.

Add the interpretation as a question.

### Writing Style and Personalities

When adding a skill, expect that you're tuning a fairly general purpose LLM to behave better given particular circumstances.

If you want to add a skill to better adopt a particular personality - say, "a little boy living in the 1800s" - that context needs to be provided in either the "context" or "question" field.

### Instruction-Following Behavior

LLMs could be better at following extra instructions in a prompt about how to do a task, such as: "Keep your response to 200 words." Or: "Only produce 10 items." Skills to improve this behavior will help the model behave with more precision.

## Skills to Avoid

There are several types of skills that we don't expect this procedure to improve. Most skills in these categories will be rejected.

### Math

Trying to make the LLM solve math problems will be rejected.

### Real world knowledge-based skills

Unless it can be framed as a "grounded skill", where the user is expected to provide context, knowledge contributions will be a separate part of the taxonomy. Skills shouldn't expect the model to come up with its own facts, but instead assemble facts provided.

### Red Teaming

Adversarial questions and answers will be rejected at this time.

### Turing-complete style problems

These are an edge case, but things like palindromes and regexes, where getting the right answer with a non-stochastic program would be easy, aren't good targets for the moment.

Ask in the channel if you have an idea in this space before submitting a PR.

### Small Changes to Original Response

If the original LLM response is pretty close, but it's not responding to your exact expectations, a skill is not the right way to solve that problem.