# InstructLab 🐶 (LAB) Taxonomy

InstructLab 🐶 uses a novel synthetic data-based alignment tuning method for
Large Language Models (LLMs.) The "**lab**" in Instruct**Lab** 🐶 stands for
**L**arge-scale **A**lignment for Chat **B**ots.

The LAB method is driven by taxonomies, which are largely created manually and
with care.

This repository contains a taxonomy tree that will allow you to create models
tuned with your data (enhanced via synthetic data generation) using LAB 🐶
method.

The top-level categories are:

1. **Core Skills**:

    Core skills are foundational skills like math, reasoning, and coding.

1. **Knowledge**:

    Knowledge consists of data and facts and is backed by documents. When you
    create knowledge for a model, you're giving it additional data to more
    accurately answer questions.
2. **Compositional Skills**:

    Skills are performative. When you create a skill for the model, you're
    teaching it how to do something: "write me a song," "talk like a pirate,"
    "summarize an email."
3. **Core Skills**:

    Core skills are foundational skills like math, reasoning, and coding.

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
      The breed with the most energy is the Labrador.
    context: 
      | **Breed**      | **Size**     | **Barking** | **Energy** |
      |----------------|--------------|-------------|------------|
      | Afghan Hound   | 25-27 in     | 3/5         | 4/5        |
      | Labrador       | 22.5-24.5 in | 3/5         | 5/5        |
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
    context: ts-world-tour-2024-schedule.md
    question: |
      Is Taytay coming to Boston in 2024?
  - answer: |
      The Taylor Swift Album Reputation was released on November 10, 2017. 
      Midnights was released October 21, 2022. Midnights was released more 
      recently, but there are rumors that there will be a re-release of 
      Reputation called Reputation (Taylor's version) in the later half of 2024 
      which would make that the most recently-released album of the set at that 
      time.
    # You can reference multiple documents with comma separation on one line.
    context: |
      knowledge_documents/ts-discography-2024.md, 
      knowledge_documents/ts-news-2024.md
    question: |
      Which album was released more recently, Reputation or Midnights?
  - answer: |
      The song "You Need to Calm Down" appears on Taylor Swift's 2019 album 
      Lover as track 14.
    context: knowledge_documents/ts-discography-2024.md
    - question: |
        Which album has the song "You Need to Calm Down?"
task_description: |
  Knowledge about Taylor Swift's music.
```

You can see this knowledge references two markdown files:
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

## Formatting

Taxonomy skill files can be any valid [YAML](https://yaml.org/) file ending in
`.yaml` containing a collection of key/value entries in which the two recognized
keys are: `question` and `answer`. For an entry to be valid, it **MUST** have
both the question and answer specified. Other keys are currently ignored.

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
## Contribute knowledge and skills to the taxonomy!

The ability to contribute to a large language model (LLM) has been difficult in no small part because it is difficult to get access to the necessary compute infrastructure.

This taxonomy repository will be used as the seed to synthesize the training data for Labrador-trained models. We intend to re-train the model(s) using the main branch following Labrador's progressive training on a nightly basis. This enables fast iteration of the model(s), for the benefit of the open source community. 

By contributing your skills and knowledge to this repository, you will see your changes built into an LLM within days of your contribution rather than months or years! If you are working with a model and notice its knowledge or ability lacking, you could correct it by contributing knowledge or skills and check if it's improved once your changes are built in a nightly build.

## Ways to Contribute

You can contribute to the taxonomy in the following two ways: 

1. Adding new examples to **existing leaf nodes**: 
    - Go to the corresponding leaf node / end of the branch and modify the yaml 
    - Add new examples to the qna.yaml files as a new entry to the list
- Adding new branches/skills corresponding to the existing domain:
1. Adding **new branches/skills** corresponding to the existing domain:
    - You can add new folders under the corresponding category
    - Create a new qna.yaml file with examples for the new skill
  
### Detailed Contribution Instructions

#### Pre-requisites:
- You need a GitHub account
- You need access to this repo

#### Make a copy of the taxonomy repo

1. Go to [github.com/open-labrador/taxonomy](github.com/open-labrador/taxonomy)
2. Press the Fork button in the upper right:
   ![fork-button](https://github.com/mairin/taxonomy/assets/799683/bc228b5b-b2a5-4d52-9a55-058c9495d4f2)
3. On the "Create a new fork" form:
   - **Repository name:** `taxonomy` is fine
   - **Description:** Please describe the skill your skill provides. Give an example question it could answer with your contributed knowledge, or an example prompt your skill will improve.
   - **Copy the main branch only:** It's OK to leave this checked on.

When you are ready, press the **Create Fork** button.

![Screenshot from 2024-02-28 12-41-59](https://github.com/mairin/taxonomy/assets/799683/2dbd43c3-f976-49cf-a99a-ab7ed0318425)

4. You will get a copy of the taxonomy repo in your github account. This is your own copy, so don't worry about making mistakes or anything like that. *(If you do end up making a mistake and want to start over: you can delete the fork and create a new fork.)*

#### Contributing a skill

In the screenshot, you can see we are under the compositional skills directory. This is the directory under which you want to contribute skills. (The other top-level directory you can contribute to is the knowledge directory, which is a little different than skills. You can read more about the difference between skills and knowledge [in that section of this README](#k-vs-s) above.) 

![Screenshot from 2024-02-28 12-44-05](https://github.com/mairin/taxonomy/assets/799683/ff8d33ba-d1fd-412c-99de-cd9de66886c2)

Based on the directories that exist in the tree, make a best guess at where in the tree structure you feel the skill you have to contribute best fits. If you get to a point where you've gone deep enough into the tree and you can't find any directories that match, please feel free to create a new directory or a directory and subdirectories to best represent your skill.

For example, I'd like to contribute a skill for creating puns. Puns are a specific type of joke. I started out in the writing directory of the tree, and saw two main directories there:

![Screenshot from 2024-02-28 12-57-00](https://github.com/mairin/taxonomy/assets/799683/9370023e-9782-4497-977e-fca54b8fd9fe)

When I looked at the directories under freeform, I saw subdirectories such as brainstorming, debate, legal, poetry, prose, etc.:

![Screenshot from 2024-02-28 12-57-35](https://github.com/mairin/taxonomy/assets/799683/18447e4a-2bbb-40cf-b90b-e95824ee1656)

When I looked under grounded, I saw subdirectories such as editing, meeting_insights, summarization/wiki_insights:

![Screenshot from 2024-02-28 12-59-10](https://github.com/mairin/taxonomy/assets/799683/22be3188-bbc1-4c76-97d4-256de974593d)

Puns seemed to fit best under the freeform directory, but I didn't think they fit under any of the pre-existing directories under freeform, so I created a jokes directory, then I created a puns directory under jokes. (I started with jokes as a directory, because I also have a knock-knock joke skill I'd like to create. 🙂)

It can be a little tricky mechanically to create directories in GitHub's web UI:

* Navigate to the folder in which you want to create the directory inside of.
* Click the "Add File" dropdown button in the upper right corner of the screen.
* Start typing the name of the first directory you want to create. In the animation below we use "jokes/" as the first directory. 
* When you type the "/" character, the directory name will "lock in" and you'll be able to type the next of the next subdirectory under it, as desired. Below we typed "knock-knock/" as the next directory name.
* Finally, you'll type the file name. The file name should always be qna.yaml. (qna stands for "Question aNd Answer.")  

Here's an animated graphic to show how it works:

![screencast-directory-naming](https://github.com/mairin/taxonomy/assets/799683/706c3ddd-13fc-43c4-9cb6-e246ba0e009a)

**TO BE CONTINUED**

### Why should I contribute?

For additional information on how to make a contribution, please, consult the 
[contributing documentation](CONTRIBUTING.md).

### Why should I contribute?

This taxonomy repository will be used as the seed to synthesize the training
data for InstructLab-trained models. We intend to re-train the model(s) using the main
branch as often as possible (at least weekly). This enables fast iteration of the model(s), for the benefit of the open source community, in particular to enable model developers who do not have access to the necessary compute infrastructure.
