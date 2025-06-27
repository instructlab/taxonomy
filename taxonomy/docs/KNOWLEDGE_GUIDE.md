# Knowledge Guide

## What is "Knowledge"?

Knowledge consists of data and facts and is backed by documents. When you create knowledge for a model, you're giving it additional data to more accurately answer questions.

Knowledge contributions in this project contain a few things.

- A file in a git repository that holds your information. For example, these repositories can include markdown versions of information on: Oscar 2024 winners, Law books, Shakespeare, Sports, Chemistry, etc.
- A `qna.yaml` file that asks and answers questions about the information in the git repository.
- A `attribution.txt` that includes the sources for the information used in the `qna.yaml`.

You can learn more about the knowledge structure in [Getting Started with Knowledge contributions](https://github.com/instructlab/taxonomy/blob/main/README.md#getting-started-with-knowledge-contributions).

## Accepted Knowledge

> [!IMPORTANT]
> We are currently only accepting knowledge contributions as a limited private beta and sources will be limited to articles from Wikipedia.

There are a few domains of knowledge that we are currently accepting. For a full list of knowledge fields, see [Knowledge domains](https://github.com/instructlab/taxonomy/blob/main/knowledge/knowledge_domains.md) in the taxonomy documentation

A few examples are as follows:

### STEM fields

- Physics
  - Astronomy and Astrophysics
  - Quantum Mechanics
  - Special Relativity and General Relativity

- Chemistry & Chemical Engineering
  - Organic Chemistry
  - Inorganic Chemistry
  - Chemical engineering
  - Biotechnology

- Earth & Environmental Science
  - Geology
  - Geography

- Biology & Life Sciences
  - Plants (Botany)
  - Medicine & health

- Electrical Engineering
- Bioengineering
- Civil Engineering
- Industrial Engineering

### Legal and regulatory

- Intellectual Property
- Criminal Law
- Civil Rights
- Healthcare compliance

### Economy and Business

- Economy and Businesses
- Accounting and Finance
- Marketing
- Human Resource
- Management

### Philosophy

- Philosophy
- Metaphysics
- Epistemology
- Ethics
- Parapsychology & occultism
- Philosophical schools of thought

### Literature

- Literature, rhetoric & criticism
- American literature in English
- Other literatures

## Avoid These Topics

While the tuning process may eventually benefit from being used to help the models work with complex social topics, at this time this is an area of active research we do not want to take lightly. Therefore please keep your submissions clear of the following topics:

- PII (personally identifiable information) or any content invasive of individual privacy rights
- Violence including self-harm
- Cyber Bullying
- Internal documentation or other that is confidential to your employer or organization, e.g. trade secrets
- Discrimination
- Religion
  - Facts such as, "[Christianity is, according to the 2011 census, the fifth most practiced religion in Nepal, with 375,699 adherents, or 1.4% of the population](https://en.wikipedia.org/wiki/Christianity_in_Nepal)", are fine as a knowledge contribution. Advocating in favor of or against any religious faith is not acceptable.
- Medical or health information
  - Facts such as,  "[In mammals, pulmonary ventilation occurs via inhalation (breathing)](https://opentextbc.ca/biology/chapter/11-3-circulatory-and-respiratory-systems/)," are fine as a knowledge contribution. Tailored medical/health advice is not acceptable.
- Financial information
  - Facts such as "[laissez-faire economics ... argues that market forces alone should drive the economy and that governments should refrain from direct intervention in or moderation of the economic system](https://openstax.org/books/world-history-volume-2/pages/6-3-capitalism-and-the-first-industrial-revolution)," are fine as a knowledge contribution. Tailored financial advice is not acceptable.
- Legal settlements/mitigations
- Gender Bias
- Hostile Language, threats, slurs, derogatory or insensitive jokes or comments
- Profanity
- Pornography and sexually explicit or suggestive content
- Any contributions that would allow for automated decision making that affect an individual's rights or well-being, e.g. social scoring
- Any contributions that engage in political campaigning or lobbying

We are also not accepting submissions of the following content:

- Code
  - Anything code-related that can be traced back to code for a computer. Not limited to `sed` or `bash` but `yaml`s for OpenShift or Kubernetes, to `python` snippets to `Java` suggestions. There are specific models focused on this space and this isn't for this model for the time being.
- Jokes
- Poems

We received many joke and poem submissions at the beginning of the project, and with jokes being "in the eye of the beholder" and puns requiring nuance for native English speakers, we realized we were possibly unconsciously biasing our model. We have discovered that working with both topics has its own challenges, and if we want something generalized, finding consensus was unsuccessful. For now, we're not accepting additional submissions of jokes and poems.

## Building Your LLM Intuition

LLMs have inherent limitations that make certain tasks extremely difficult, like doing math problems. They're great at other tasks, like creative writing. And they could be better at things like logical reasoning.

An LLM with knowledge helps it create a basis of information that it can learn from, then you can teach it to use this knowledge via the `qna.yaml` files.

For example, you can give an LLM the entire periodic table, then in a `qna.yaml` add something like:

question: What is the symbol and atomic number for Chlorine?
answer: |
        The symbol for chlorine is Cl and the atomic number is 17.

With a few of these qna's, the model will learn the periodic table because it has the knowledge data.

### LLMs are great at

For these, however, it's common for LLMs to already have excellent performance. Try 3-5 examples in `lab chat` to confirm a deficit in the model before you build your submission, and share the examples in your Pull Request (PR).

- Brainstorming
- Creativity
- Connecting information
- Cross-lingual behavior

### LLMs need help with

LLM behavior in these sorts of topics are very difficult for the model to get right. Try several examples to understand the nuances of the model's ability to do these sorts of tasks, and consider using corrections to the results you get in your tuning process.

- Chains of reasoning
- Analysis
- Story plots
- Reassembling information
- Effective and succinct summaries

### LLMs are not so great at

LLMs may struggle with solving math and computation. That said, improving some of these foundational skills may be something this work tackles in the future, but not at this time.

- Math
- Computation
- "Turing-complete" type tasks
- Generating only true real-world information (they're prone to hallucinations)
