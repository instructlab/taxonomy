# Skills Guide

## What is a "Skill"?

There are various types of skills that you can contribute to the taxonomy.

### Compositional Skills

Skills are performative. When you create a skill for the model, you're
teaching it how to do something: "write me a song," "rearrange words in a sentence" or
"summarize an email."

There are two types of compositional skills:

#### Freeform Compositional Skills

Freeform compositional skills are performative and do **not** require additional context. An example of a freeform skill is teaching the model words that rhyme. You could provide examples of "words that rhyme with 'tool'". By providing those examples, you're essentially tickling the latent knowledge of the LLM. In our example, you're enabling the LLM to be able to identify words that rhyme in its latent knowledge.

Freeform skills include things like:

* Speak like Yoda
* Convert to camel case
* Write me a limerick
* Generate StabeDiffusion prompts

#### Grounded Compositional Skills

Grounded skills are performative and **do** require additional context. An
example of a grounded skill would be to read the value of a cell in a table
layout, or to parse a JSON file. To create a grounded skill to read a
markdown formatted table layout, the additional context could be an example
table layout. This additional context is including in the YAML for the
skill and not external to it.

> [!NOTE]
> The content of the table layout will not be used in training
> or aligning the model; only the table layout format itself will be used.

Grounded skills include things like:

* Game creation like Sudoku or tic tac toe
* Summarizing or extracting from a piece of text
* Find unresolved items in a meeting transcript

[Example Grounded compositional skill pull request](https://github.com/instructlab/taxonomy/pull/250)

### Core Skills

Core skills are foundational skills like math, reasoning, and coding.

> [!NOTE]
> Unlike **knowledge** and **compositional skills**, core skills
> are not contributable to the tree. So when you see reference to contributing
> "skills" to the taxonomy from this point forward, it is **compositional
> skills** that are being referenced.

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

Example:

> Mary is taller than John.
> John is taller than Anna.
> Is Anna taller than Mary?

Example:

> An elephant, a mouse and a horse are in a room. How would they be ordered if they were standing in order by size?

Great skills in this category should include the correct line of reasoning in the answer, not just what the answer is.

### Word Problems

Is your LLM smarter than a second grader?

### Trust and Safety

Please avoid HAP (hate, abuse and profanity) and PII (personal identifiable information) in your examples.

Anything related to trust and safety will be flagged for higher-level review.

### Searching, Extraction and Summarization

Skills to select odd information in a document, draw conclusions, pull out information, draw insights or generate TODOs from information provided in the "context" field are welcome.

### Complex Rulesets and Games

> [!NOTE]
> This is a good example of the need for a *grounded skill*. Grounded skills require the user to provide context containing information that the model is expected to take into account during processing. This is different from *knowledge*, where the model is expected to gain facts and background knowledge from the tuning process.
>
> Context added when tuning a grounded skill would need to be again provided by the end user at inference time. The skill here is better adherence to the rule set.

To add a skill for a structured game or other task with a complex rule set, use a grounded skill. Add the rules to the game as "context" in every example. Add the interpretation as a question.

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

Open an issue in the taxonomy repository if you have an idea in this space before submitting a PR.

### Small Changes to Original Response

If the original LLM response is pretty close, but it's not responding to your exact expectations, a skill is not the right way to solve that problem.

## Avoid These Topics

While the tuning process may eventually benefit from being used to help the models work with complex social topics, at this time this is an area of active research we do not want to take lightly. Therefore please keep your submissions clear of the following topics:

* PII (personally identifiable information) or any content invasive of individual privacy rights
* Violence including self-harm
* Cyber Bullying
* Internal documentation or other that is confidential to your employer or organization, e.g. trade secrets
* Discrimination
* Religion
  * Facts such as, "[Christianity is, according to the 2011 census, the fifth most practiced religion in Nepal, with 375,699 adherents, or 1.4% of the population](https://en.wikipedia.org/wiki/Christianity_in_Nepal)", are fine as a knowledge contribution. Advocating in favor of or against any religious faith is not acceptable.
* Medical or health information
  * Facts such as,  "[In mammals, pulmonary ventilation occurs via inhalation (breathing)](https://opentextbc.ca/biology/chapter/11-3-circulatory-and-respiratory-systems/)," are fine as a knowledge contribution. Tailored medical/health advice is not acceptable.
* Financial information
  * Facts such as "[laissez-faire economics ... argues that market forces alone should drive the economy and that governments should refrain from direct intervention in or moderation of the economic system](https://openstax.org/books/world-history-volume-2/pages/6-3-capitalism-and-the-first-industrial-revolution)," are fine as a knowledge contribution. Tailored financial advice is not acceptable.
* Legal settlements/mitigations
* Gender Bias
* Hostile Language, threats, slurs, derogatory or insensitive jokes or comments
* Profanity
* Pornography and sexually explicit or suggestive content
* Any contributions that would allow for automated decision making that affect an individual's rights or well-being, e.g. social scoring
* Any contributions that engage in political campaigning or lobbying

We are also not accepting submissions of the following content:

* Jokes
* Poems
* Code
  * Anything code-related that can be traced back to code for a computer. Not limited to `sed` or `bash` but `yaml`s for OpenShift or Kubernetes, to `python` snippets to `Java` suggestions. There are specific models focused on this space and this isn't for this model for the time being.
* "Guard Rails" for AI
  * We expect our upstream engineering team to create these types of skills and safe guards. We appriciate our community wanting to help with this, but there are underlying engineering decisions and taking this from the community may conflict with these.

We received so many at the beginning, and with jokes being "in the eye of the beholder" and puns requiring nuance for native English speakers, we realized we were possibly unconsciously biasing our model. We have discovered that working with both topics has its own challenges, and if we want something generalized, finding consensus was unsuccessful.

## Building Your LLM Intuition

LLMs have inherent limitations that make certain tasks extremely difficult, like doing math problems. They're great at other tasks, like creative writing. And they could be better at things like logical reasoning.

Consider these when you're generating skills. Skills in the first and second categories are welcomed. Skills in the third category are usually borderline and may be rejected.

### LLMs are great at

Skills in this category are welcomed, as refining these abilities helps us get better at the kinds of tasks where LLMs can excel.

For these, however, it's common for LLMs to already have excellent performance. Try 3-5 examples in `lab chat` to confirm a deficit in the model before you build your submission, and share the examples in your Pull Request (PR).

* Brainstorming
* Creativity
* Connecting information
* Cross-lingual behavior

### LLMs need help with

Skills in this category are welcomed, since LLM behavior in these sorts of topics are very difficult for the model to get right. Try several examples to understand the nuances of the model's ability to do these sorts of tasks, and consider using corrections to the results you get in your tuning process.

* Chains of reasoning
* Analysis
* Story plots
* Reassembling information
* Effective and succinct summaries

### LLMs are not so great at

Skills in this category are ways in which LLMs struggle, and may always struggle. Solving math and computation problems via probability on natural language queries is probably not the best way to solve them. That said, improving some of these foundational skills may be something this work tackles in the future, but not at this time.

Most skill submissions in these categories are likely to be rejected.

For hallucinations in particular, trying to solve this with a skill is unlikely to work. Consider contributing to the Knowledge taxonomy when it opens instead to improve the model's understanding of facts.

* Math
* Computation
* "Turing-complete" type tasks
* Generating only true real-world information (they're prone to hallucinations)
