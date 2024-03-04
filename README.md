# InstructLab 🥼 (LAB) Taxonomy

InstructLab 🥼 uses a novel synthetic data-based alignment tuning method for
Large Language Models (LLMs.) The "**lab**" in Instruct**Lab** 🥼 stands for
**L**arge-scale **A**lignment for Chat **B**ots.

The LAB method is driven by taxonomies, which are largely created manually and
with care.

This repository contains a taxonomy tree that will allow you to create models
tuned with your data (enhanced via synthetic data generation) using LAB 🐶
method.

The top-level categories are:

1. **Core Skills**:

    Core skills are foundational skills like math, reasoning, and coding.

    🗒️ **Note:** Unlike **knowledge** and **compositional skills**, core skills
    are not contributable to the tree. So when you see reference to contributing
    "skills" to the taxonomy from this point forward, it is **compositional
    skills** that are being referenced.
2. **Knowledge**:

    Knowledge consists of data and facts and is backed by documents. When you
    create knowledge for a model, you're giving it additional data to more
    accurately answer questions.
3. **Compositional Skills**:

    Skills are performative. When you create a skill for the model, you're
    teaching it how to do something: "write me a song," "talk like a pirate,"
    "summarize an email."

There are two types of compositional skills:

1. **Freeform Compositional Skills**:

     Freeform compositional skills are performative and do **not** require
     additional context. An example of a compositional skill is "talk like a
     pirate." You could provide examples of "pirate-like" speech. By providing
     those examples, you're essentially tickling the latent knowledge of the
     LLM. In our "talk like a pirate" example, you're enabling the LLM to be
     able to recall pirate-like speechs in its latent knowledge.
      
2. **Grounded Compositional Skills**:

     Grounded skills are performative and **do** require additional context. An
     example of a grounded skill would be to read the value of a cell in a table
     layout, or to parse a JSON file. To create a grounded skill to read a 
     markdown formatted table layout, the additional context could be an example
     table layout. This additional context is including in the YAML for the
     skill and not external to it. 

     🗒️ **Note:** The content of the table layout will not be used in training
     or aligning the model; only the table layout format itself will be used.

## Compositional Skills vs. Knowledge

You can contribute both **compositional skills** (and in the future, 
**knowledge**) to the Taxonomy. What is the difference?

### Compositional Skills

Again, think of skills as "performative." You're teaching the model how to
**do** something when you contribute a skill.

Skills require a much smaller volume of content to contribute. A skill
contribution to the taxonomy tree can be just a few lines of YAML (its
`qna.yaml` file - "qna" is short for "questions and answers") in its entirety:

#### Freeform compositional skill: YAML example

This example assumes the GitHub username `mairin`:

``` yaml
created_by: mairin # Use your GitHub username; only one creator supported
seed_examples:
  - answer: |  # The | is needed to escape characters like ` or '
      Why do birds eat wood?
      
      Because they're peckish!
    question: Tell me a pun about birds.
  - answer: |
      What do dentists call their x-rays?

      Tooth pics!
    question: Tell me a pun about x-rays.
  - answer: |
      Why did the car have a belly ache?

      Because it had too much gas!
    question: Tell me a pun about gas.
  - answer: |
      What did the ocean say to the ocean?

      Nothing. It just waved!
    question: Tell me a pun about waves.
task_description: |
  The pun task enables the telling of funny pun-based jokes.
```

Seriously, that's it.

Here is where this yaml sits in the taxonomy tree - note that the yaml file
itself, plus any added directories it sits inside, is the entirety of the skill
in terms of a taxonomy contribution:

#### Freeform compositional skill: Directory tree example

``` ascii
[...]

└── writing
    └── freeform
    |   └── jokes
    |   |    └── puns <=== here it is :)
    |   |         └── qna.yaml
    │   ├── debate
    │   │   └── qna.yaml
    │   ├── legal
    │   │   ├── agreement
    │   │   │   └── qna.yaml

[...]
```

#### Grounded compositionial skill: YAML example

Remember that grounded compositional skills require additional context

This example assumes the GitHub username `mairin`:

```
created_by: mairin # Use your GitHub username; only one creator supported
seed_examples:
  - answer: |
      The breed with the most energy is the InstructLab.
    context: 
      | **Breed**      | **Size**     | **Barking** | **Energy** |
      |----------------|--------------|-------------|------------|
      | Afghan Hound   | 25-27 in     | 3/5         | 4/5        |
      | InstructLab    | 22.5-24.5 in | 3/5         | 5/5        |
      | Cocker Spaniel | 14.5-15.5 in | 3/5         | 4/5        |
      | Poodle (Toy)   | <= 10 in     | 4/5         | 4/5        |
    question: |
      Which breed has the most energy?
  - answer: |
      Gráinne's letter is B and her color is red.
    context:
      | **Name** | **Date** | **Color** | **Letter** | **Number** |
      |----------|----------|-----------|------------|------------|
      | George   | Mar 5    | Green     | A          | 1          |
      | Gráinne  | Dec 31   | Red       | B          | 2          |
      | Abigail  | Jan 17   | Yellow    | C          | 3          |
      | Bhavna   | Apr 29   | Purple    | D          | 4          |
      | Rémy     | Sep 9    | Blue      | E          | 5          |
    question: |
      What is Gráinne's letter and what is her color?
  - answer: |
      The blueberry is blue, small, and has no peel.
    context:
      | Banana | Apple      | Blueberry | Strawberry |
      |--------|------------|-----------|------------|
      | Yellow | Red, Green | Blue      | Red        |
      | Large  | Medium     | Small     | Small      |
      | Peel   | Peel       | No peel   | No peel    |
    question: |
      Which fruit is blue, small, and has no peel?
task_description: | 
    This skill provides the ability to read a markdown-formatted table.
```

#### Grounded compositional skill: Directory tree example

``` ascii
[...]

└── extraction
    └── inference
    |   └── qualitative
    |   |    ├── sentiment
    |   |    |    └── qna.yaml
    |   |    └── tone_and_style
    |   |         └── qna.yaml
    │   ├── quantitative
    │   │   ├── markdown_table <=== here it is :)
    │   |   |    └── qna.yaml
    │   │   ├── word_frequency
    │   │   │   └── qna.yaml

[...]
```

### Knowledge

⚠️ **Note:** We are not currently accepting knowledge contributions, but we 
will open this up in the future!

Meanwhile, knowledge is based more on answering questions that involve facts,
data, or references.

Knowledge in the taxonomy tree also consists of a few more elements than skills.
Each knowledge node in the tree has a `qna.yaml` similar to the format of the
`qna.yaml` for skills, but it has an extra folder for knowledge documents called
`knowledge_documents`. These knowledge document formats are are currently
supported are markdown (.md) and text (.txt).

Each `qna.yaml` file is required to contain a minimum of three question-answer
pairs. The `qna.yaml` format should include the following fields:

- `seed_examples` (three or more examples sourced from the provided knowledge
  documents)
- `created_by` (your name)
- `task_description` (an optional description of the knowledge).

#### Knowledge: yaml example

``` yaml
---
created_by: mairin   # Use your GitHub username; only one creator supported
seed_examples:
  - answer: |
      Not that is known yet. Taylor Swift last performed in the Boston area at 
      the Gilette Stadium in Foxboro, MA for 3 nights from Friday May 19, 2023 
      to Sunday May 21, 2023. In 2024, she is making international tour stops 
      for her Eras tour outside of the United States.
    question: |
      Is Taytay coming to Boston in 2024?
  - answer: |
      The Taylor Swift Album Reputation was released on November 10, 2017. 
      Midnights was released October 21, 2022. Midnights was released more 
      recently, but there are rumors that there will be a re-release of 
      Reputation called Reputation (Taylor's version) in the later half of 2024 
      which would make that the most recently-released album of the set at that 
      time.
    question: |
      Which album was released more recently, Reputation or Midnights?
  - answer: |
      The song "You Need to Calm Down" appears on Taylor Swift's 2019 album 
      Lover as track 14.
    - question: |
        Which album has the song "You Need to Calm Down?"
task_description: |
  Knowledge about Taylor Swift's music.
```

This knowledge references two markdown files: 
`ts-world-tour-2024-schedule.md` as well as `ts-discography-2024.md` - these
files in their entirety need to be submitted along with the knowledge's
`qna.yaml` file in a `knowledge_documents` folder, which means that knowledge
consists of a much higher volume of content than a skill.

This of course, means **it will naturally take longer to receive acceptance for
a knowledge contribution pull request than for a skill pull request** - smaller
pull requests are simpler and require less time and effort to review.

What might these markdown files look like? They can be freeform. Here's what a
snippet of `ts-discography-2024.md` might look like:

``` markdown
# Albums

## Studio Albums

### Taylor Swift
- Released: October 24, 2006
- Label: Big Machine
- Track Listing:
  1. "Tim McGraw"
  2. "Picture to Burn"
  3. "Teardrops on My Guitar"
  4. "A Place in This World"
  5. "Cold as You"
  6. "The Outside"
  7. "Tied Together with a Smile"
  8. "Stay Beautiful"
  9. "Should've Said No"
  10. "Mary's Song (Oh My My My)"
  11. "Our Song"

### Fearless
- Released: November 11, 2008
- Label: Big Machine
- Track Listing:
  1. "Fearless"
  2. "Fifteen"
  3. "Love Story"
  4. "Hey Stephen"
[..]
```

In contrast to the layout of skills in the taxonomy, here's what the knowledge
referenced above might look like in the tree:

#### Knowledge: directory tree example

``` ascii
[...]

└── knowledge
    └── textbooks
        ├── culture
        │ └── music
        │     └── pop
        │         ├── taylor swift <=== here it is :)
        │         │ ├── knowledge_documents
        │         │ │ ├── ts-discography-2024.md
        │         │ │ └── ts-world-tour-2024-schedule.md
        │         │ └── qna.yaml
        │         └── the rolling stones
        │             ├── knowledge_documents
        │             │ ├── rs-discography-2024.md
        │             │ ├── rs-guitar-tabs.md
        │             │ ├── rs-lyrics-catalog-2024.md
        │             │ └── rs-tour-history.md
        │             └── qna.yaml

[...]
```

## YAML Format

Taxonomy skill files can be any valid [YAML](https://yaml.org/) file ending in
`.yaml` containing a set of key/value entries, in which the following three
keys are recognized: `created_by`, `seed_examples`, and `task_description`.

* The value of the `created_by` key can be any string.
* The value of the `seed_examples` key is a collection of one or more key/value entries in which the
two recognized keys are: `question` and `answer`, each of which can have any string
as value. For an entry to be valid, it **MUST** have both the question and answer specified. 
* The value of the `task_description` key is currently ignored and left empty.

Other keys at any level are currently ignored.

So in essence the format looks something like this:

```
created_by: <string>
seed_examples:
   - answer: <string>
     question: <string>
   - answer: <string>
     question: <string>
   ...  
task_description: 
```


If you have not written YAML before, don't be intimidated - it's just text. 
There's a few things to know:

- Spaces and indentation matter in YAML. Two spaces to indent.
- Don't use tabs!
- Be careful to not have trailing spaces at the end of a line.
- The line for the `answer` key should start with a "-", but the other keys
  should not have this "-".
- Some special characters such as " and ' need to be "escaped." This is why some
  of the lines for keys in the example YAML we provided have the "|" character.
  This character escapes all of the special characters in the value for the key.

It is recommended that you **lint**, or check that the YAML is correct using a
tool. There is a very nice website you can use to do this:

[yamllint.com](https://yamllint.com)

You can copy/paste your YAML into the box and click the "Go" button to have it
analyse your YAML and make recommendations.

## Layout

The taxonomy tree is organized in a cascading directory structure. At the end of
each branch, there is a YAML file (qna.yaml) that contains the examples for that
domain.

Below is an illustrative directory structure to show this layout:

``` ascii
.
└── writing
    ├── freeform
    │   ├── brainstorming
    │   │   ├── idea_generation
    │   │   │   └── qna.yaml
    │   │   ├── refute_claim
    │   │   │   └── qna.yaml
    │   │   └── support_claim
    │   │       └── qna.yaml
    │   ├── debate
    │   │   └── qna.yaml
    │   ├── legal
    │   │   ├── agreement
    │   │   │   └── qna.yaml
    │   │   └── contracts
    │   │       └── qna.yaml
    │   ├── poetry
    │   │   ├── ballad
    │   │   │   └── qna.yaml
    │   │   ├── epic_poetry
    │   │   │   └── qna.yaml
    │   │   ├── freeverse
    │   │   │   └── qna.yaml
    │   │   ├── haiku
    │   │   │   └── qna.yaml
    │   │   ├── limerick
    │   │   │   └── qna.yaml
    │   │   ├── narrative_poetry
    │   │   │   └── qna.yaml
    │   │   ├── ode
    │   │   │   └── qna.yaml
    │   │   └── sonnet
    │   │       └── qna.yaml
    │   ├── prose
    │   │   ├── articles
    │   │   │   └── qna.yaml
    │   │   ├── emails
    │   │   │   ├── formal
    │   │   │   │   └── qna.yaml
    │   │   │   └── informal
    │   │   │       └── qna.yaml
    │   │   ├── screenplay
    │   │   │   └── qna.yaml
    │   │   └── stories
    │   │       └── qna.yaml
    │   ├── social_media
    │   │   ├── facebook
    │   │   │   └── qna.yaml
    │   │   ├── instagram
    │   │   │   └── qna.yaml
    │   │   ├── linkedin
    │   │   │   └── qna.yaml
    │   │   └── twitter
    │   │       └── qna.yaml
    │   └── technical
    │       ├── guide
    │       │   └── qna.yaml
    │       ├── product_description
    │       │   └── qna.yaml
    │       ├── proposal
    │       │   └── qna.yaml
    │       ├── report
    │       │   └── qna.yaml
    │       ├── specification
    │       │   └── qna.yaml
    │       └── user_manual
    │           └── qna.yaml
    └── grounded
        ├── editing
        │   ├── grammar
        │   │   └── qna.yaml
        │   ├── punctuation
        │   │   └── qna.yaml
        │   └── spelling
        │       └── qna.yaml
        ├── meeting_insights
        │   ├── action_items
        │   │   └── qna.yaml
        │   ├── corporate_email
        │   │   └── qna.yaml
        │   ├── executive_summaries
        │   │   └── qna.yaml
        │   └── minutes_of_meeting
        │       └── qna.yaml
        └── summarization
            └── wiki_insights
                ├── concise
                │   └── qna.yaml
                ├── detailed
                │   └── qna.yaml
                ├── five_point
                │   └── qna.yaml
                ├── high_level_outline
                │   └── qna.yaml
                └── one_line
                    └── qna.yaml
```
