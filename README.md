# InstructLab 🥼 (LAB) Taxonomy

InstructLab 🥼 uses a novel synthetic data-based alignment tuning method for
Large Language Models (LLMs.) The "**lab**" in Instruct**Lab** 🥼 stands for
**L**arge-scale **A**lignment for Chat **B**ots.

The LAB method is driven by taxonomies, which are largely created manually and
with care.

This repository contains a taxonomy tree that will allow you to create models
tuned with your data (enhanced via synthetic data generation) using LAB 🐶
method.

## Learning

Learn about the concepts of "skills" and "knowledge" in our [InstructLab Community Learning Guide](https://github.com/instruct-lab/community/blob/main/docs/README.md).

## Getting Started with Skill Contributions

Skills require a much smaller volume of content to contribute. A skill
contribution to the taxonomy tree can be just a few lines of YAML (its
`qna.yaml` file - "qna" is short for "questions and answers") in its entirety:

Each `qna.yaml` file is required to contain a minimum of five question and
answer pairs. The `qna.yaml` format should include the following fields:

- `seed_examples` (five or more examples of question and answer pairs)
- `created_by` (your Github username)
- `task_description` (an optional description of the skill).
- `attribution` `source` `license` (cite your sources)

> [!TIP]
> The skill taxonomy structure is used in several ways:
>    1. Selecting the right subset of the taxonomy to use for data generation.
>    2. Interpretability by human contributors and maintainers.
>    3. As part of the prompt to GPT model used to generate synthetic samples.
> Therefore: Make sure the names of directories match the intent of the
> taxonomy files, perhaps also see if there's a more logical place in the
> taxonomy structure for a person's contribution to live before signing off.

## YAML Format

Taxonomy skill files must be a valid [YAML](https://yaml.org/) file named
`qna.yaml` containing a set of key/value entries which contain the following keys:

- `task_description` - A description of the skill. This key is required.

- `created_by` - The GitHub username of the contributor. This key is required.

- `seed_examples` - A collection of key/value entries which contain the following keys. This key is required.

  - `question` - A question for the model. This key is required.

  - `answer` The desired response from the model. This key is required.

  - `context` - Grounded skills require the user to provide context containing information that the model is expected to take into account during processing. This is different from knowledge, where the model is expected to gain facts and background knowledge from the tuning process. The context key is optional for freeform skills.

  - `attribution` - A collection of key/value entries which contain the following keys. All sources of information must be specified. This key is required.

    - `source` - If information in the context, question, or answer come from a 3rd party, for example Wikipedia, then the value must specify a URL to the source material. If the contributor self-authored all the information, then the value must be `self-authored`. This key is required.

    - `license` - The value must specify the [SPDX License Identifier](https://spdx.org/licenses/) of the source information. See [CONTRIBUTING.MD](./CONTRIBUTING.md#legal) for guidance on acceptable licenses for source information. If the information is self-authored, then `Apache-2.0` must be used. This key is required.

Other keys at any level are currently ignored.

To make these files easier and faster for humans to read, it is recommended to
specify `task_description` first, followed by `created_by`, and finally `seed_examples`.
In `seed_examples`, it is recommended to specify `context`
first (if applicable), followed by `question`, `answer`, and finally `attribution`.

So in essence the format looks something like this:

```yaml
task_description: <string>
created_by: <string>
seed_examples:
  - question: <string>
    answer: |
      <multi-line string>
    attribution:
      - source: <string>
        license: <SPDX license identifier>
  - context: |
      <multi-line string>
    question: <string>
    answer: |
      <multi-line string>
    attribution:
      - source: <string>
        license: <SPDX license identifier>
  ...  
```

If you have not written YAML before, don't be intimidated - it's just text.
There's a few things to know:

- Spaces and indentation matter in YAML. Two spaces to indent.
- Don't use tabs!
- Be careful to not have trailing spaces at the end of a line.
- Each example in `seed_examples` begins with a "-". Place this "-" in
  front of the first field (`question` or `context`). The remaining keys in the
  example should not have this "-".
- Some special characters such as " and ' need to be "escaped." This is why some
  of the lines for keys in the example YAML we provided have the '|' character.
  This character escapes all of the special characters in the value for the key.
  You may also want to use the '|' character for multi-line strings.

It is recommended that you **lint**, or verify your YAML using a
tool. There is a very nice website you can use to do this:

[yamllint.com](https://yamllint.com)

You can copy/paste your YAML into the box and click the "Go" button to have it
analyze your YAML and make recommendations.

Online tools like [prettified](https://onlineyamltools.com/prettify-yaml) and
[yaml-validator](https://jsonformatter.org/yaml-validator) can automatically
reformat your YAML to adhere to our `yamllint` PR checks, like breaking lines
longer than 120 characters.


#### Freeform compositional skill: YAML example

This example snippet assumes the GitHub username `mairin`, showing
some of the question/answer pairs that would be present in the actual
file:

```yaml
task_description: |
  The pun task enables the telling of funny pun-based jokes.
created_by: mairin # Use your GitHub username; only one creator supported
seed_examples:
  - question: Tell me a pun about birds.
    answer: |  # The | is needed to escape characters like ` or '
      Why do birds eat wood?
      
      Because they're peckish!
    attribution:
      - source: self-authored
        license: Apache-2.0
  - question: Tell me a pun about x-rays.
    answer: |
      What do dentists call their x-rays?

      Tooth pics!
    attribution:
      - source: self-authored
        license: Apache-2.0
  - question: Tell me a pun about gas.
    answer: |
      Why did the car have a belly ache?

      Because it had too much gas!
    attribution:
      - source: self-authored
        license: Apache-2.0
  - question: Tell me a pun about waves.
    answer: |
      What did the ocean say to the ocean?

      Nothing. It just waved!
    attribution:
      - source: self-authored
        license: Apache-2.0
  - question: Tell me a pun about frogs.
    answer: |
      What happens when frogs park illegally? 

      They get toad. 
    attribution:
      - source: self-authored
        license: Apache-2.0
```

Seriously, that's it.

Here is where this yaml sits in the taxonomy tree - note that the yaml file
itself, plus any added directories it sits inside, is the entirety of the skill
in terms of a taxonomy contribution:

#### Freeform compositional skill: Directory tree example

```ascii
[...]

└── writing
    └── freeform
    |   └── jokes/puns <=== here it is :)
    |   |   └── qna.yaml
    │   ├── debate
    │   │   └── qna.yaml
    │   ├── legal
    │   │   ├── agreement
    │   │   │   └── qna.yaml

[...]
```

#### Grounded compositional skill: YAML example

Remember that [grounded compositional skills](https://github.com/instruct-lab/community/blob/main/docs/SKILLS_GUIDE.md) require additional context and include a `context` field. 

This example snippet assumes the GitHub username `mairin`, again
omitting some of the question/answer pairs in the actual file:

```yaml
task_description: | 
    This skill provides the ability to read a markdown-formatted table.
created_by: mairin # Use your GitHub username; only one creator supported
seed_examples:
  - context: |
      | **Breed**      | **Size**     | **Barking** | **Energy** |
      |----------------|--------------|-------------|------------|
      | Afghan Hound   | 25-27 in     | 3/5         | 4/5        |
      | Labrador       | 22.5-24.5 in | 3/5         | 5/5        |
      | Cocker Spaniel | 14.5-15.5 in | 3/5         | 4/5        |
      | Poodle (Toy)   | <= 10 in     | 4/5         | 4/5        |
    question: |
      Which breed has the most energy?
    answer: |
      The breed with the most energy is the Labrador.
    attribution:
      - source: self-authored
        license: Apache-2.0
  - context: |
      | **Name** | **Date** | **Color** | **Letter** | **Number** |
      |----------|----------|-----------|------------|------------|
      | George   | Mar 5    | Green     | A          | 1          |
      | Gráinne  | Dec 31   | Red       | B          | 2          |
      | Abigail  | Jan 17   | Yellow    | C          | 3          |
      | Bhavna   | Apr 29   | Purple    | D          | 4          |
      | Rémy     | Sep 9    | Blue      | E          | 5          |
    question: |
      What is Gráinne's letter and what is her color?
    answer: |
      Gráinne's letter is B and her color is red.
    attribution:
      - source: self-authored
        license: Apache-2.0
  - context: |
      | Banana | Apple      | Blueberry | Strawberry |
      |--------|------------|-----------|------------|
      | Yellow | Red, Green | Blue      | Red        |
      | Large  | Medium     | Small     | Small      |
      | Peel   | Peel       | No peel   | No peel    |
    question: |
      Which fruit is blue, small, and has no peel?
    answer: |
      The blueberry is blue, small, and has no peel.
    attribution:
      - source: self-authored
        license: Apache-2.0
```

#### Grounded compositional skill: Directory tree example

```ascii
[...]

└── extraction
    └── inference
    |   └── qualitative
    |   |    ├── sentiment
    |   |    |    └── qna.yaml
    |   |    └── tone_and_style
    |   |         └── qna.yaml
    │   ├── quantitative
    │   │   ├── table_analysis <=== here it is :)
    │   |   |    └── qna.yaml
    │   │   ├── word_frequency
    │   │   │   └── qna.yaml

[...]
```

### Knowledge

> [!NOTE]
> We are not currently accepting knowledge contributions, but we will open this
> up in the future!

Meanwhile, knowledge is based more on answering questions that involve facts,
data, or references.

Knowledge in the taxonomy tree also consists of a few more elements than skills.
Each knowledge node in the tree has a `qna.yaml` similar to the format of the
`qna.yaml` for skills, but it has an extra folder for knowledge documents called
`knowledge_documents`. The knowledge document formats currently supported are
markdown (.md).

Each `qna.yaml` file is required to contain a minimum of five question-answer
pairs. The `qna.yaml` format must include the following fields:

- `created_by` (your Github username)
- `domain` (category the knowledge falls under)
- `seed_examples` (five or more examples sourced from the provided knowledge documents)
- `created_by` (your GitHub username)
- `task_description` (an optional description of the knowledge).
- `attribution` `source` `license` (cite your sources)

#### Knowledge: yaml example

```yaml
task_description: |
  Knowledge about Taylor Swift's music.
created_by: mairin
domain: pop culture 
seed_examples:
  - question: |
      Is Taytay coming to Boston in 2024?
    answer: |
      Not that is known yet. Taylor Swift last performed in the Boston area at 
      the Gilette Stadium in Foxboro, MA for 3 nights from Friday May 19, 2023 
      to Sunday May 21, 2023. In 2024, she is making international tour stops 
      for her Eras tour outside of the United States.
    attribution:
      - source: self-authored
        license: Apache-2.0
  - question: |
      Which album was released more recently, Reputation or Midnights?
    answer: |
      The Taylor Swift Album Reputation was released on November 10, 2017. 
      Midnights was released October 21, 2022. Midnights was released more 
      recently, but there are rumors that there will be a re-release of 
      Reputation called Reputation (Taylor's version) in the later half of 2024 
      which would make that the most recently-released album of the set at that 
      time.
    attribution:
      - source: self-authored
        license: Apache-2.0
  - question: |
      Which album has the song "You Need to Calm Down?"
    answer: |
      The song "You Need to Calm Down" appears on Taylor Swift's 2019 album 
      Lover as track 14.
    attribution:
      - source: self-authored
        license: Apache-2.0
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

```markdown
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

```ascii
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
keys are recognized: `task_description`, `created_by`, and `seed_examples`.

* The value of the `task_description` key can be any string.
* The value of the `created_by` key can be any string.
* The value of the `seed_examples` key is a collection of one or more
key/value entries in which the three recognized keys are: `context`,
`question`, and `answer`, each of which can have any string as
value. For an entry to be valid, it **MUST** have the question and
answer specified.  While older files may have fewer question/answer
pairs, it is recommended that all new additions contain at least five
pairs.
* Under the `attribution` key, the value of `source` should state where 
the content came from, and the value of `license` should state the license of
the content.

Other keys at any level are currently ignored.

To make these files easier and faster for humans to read, it is recommended to 
specify the `task_description` first, followed by `created_by`, and finally 
`seed_examples`. In `seed_examples`, it is recommended to specify the `context` 
first (if applicable), followed by the `question`, and finally the `answer`.

So in essence the format looks something like this:

``` yaml
task_description: <string>
created_by: <string>
seed_examples:
  - question: <string>
    answer: |
      <multi-line string>
    attribution:
      - source: self-authored
        license: Apache-2.0
  - context: |
      <multi-line string>
    question: <string>
    answer: |
      <multi-line string>
    attribution:
      - source: self-authored
        license: Apache-2.0
  ...  
```


If you have not written YAML before, don't be intimidated - it's just text. 
There's a few things to know:

- Spaces and indentation matter in YAML. Two spaces to indent.
- Don't use tabs!
- Be careful to not have trailing spaces at the end of a line.
- Each example in `seed_examples` should start with a "-". Place this "-" in
  front of the first field (`question` or `context`). The remaining keys in the
  example should not have this "-".
- Some special characters such as " and ' need to be "escaped." This is why some
  of the lines for keys in the example YAML we provided have the "|" character.
  This character escapes all of the special characters in the value for the key.
  You may also want to use the "|" character for multi-line strings.

It is recommended that you **lint**, or check that the YAML is correct using a
tool. There is a very nice website you can use to do this:

[yamllint.com](https://yamllint.com)

You can copy/paste your YAML into the box and click the "Go" button to have it
analyse your YAML and make recommendations.

Online tools like [prettified](https://onlineyamltools.com/prettify-yaml) and
[yaml-validator](https://jsonformatter.org/yaml-validator) can automatically
reformat your YAML to adhere to our `yamllint` PR checks, like breaking lines
longer than 120 characters.

## Layout

The taxonomy tree is organized in a cascading directory structure. At the end of
each branch, there is a YAML file (qna.yaml) that contains the examples for that
domain. The branch names can change or more can be added, that decision is up to the maintainers. 
> **Note:** Folder names should not have a space. 

Below is an illustrative directory structure to show this layout:

```ascii
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

The ability to contribute to a Large Language Model (LLM) has been difficult in no small part because it is difficult to get access to the necessary compute infrastructure.

This taxonomy repository will be used as the seed to synthesize the training data for InstructLab-trained models. We intend to re-train the model(s) using the main branch following InstructLab's progressive training on a regular basis. This enables fast iteration of the model(s), for the benefit of the open source community.

By contributing your skills and knowledge to this repository, you will see your changes built into an LLM within days of your contribution rather than months or years! If you are working with a model and notice its knowledge or ability lacking, you could correct it by contributing knowledge or skills and check if it's improved once your changes are built.

While public contributions are welcome to help drive community progress, you can also fork this repository under [the Apache License, Version 2.0](LICENSE), add your own internal skills, and train your own models internally.
However, you may need your own access to significant compute infrastructure to perform sufficient retraining.

## Ways to Contribute

You can contribute to the taxonomy in the following two ways:

1. Adding new examples to **existing leaf nodes**:

    - Go to the corresponding leaf node / end of the branch and modify the yaml 
    - Add new examples to the qna.yaml files as a new entry to the list

2. Adding **new branches/skills** corresponding to the existing domain:

    - You can add new folders under the corresponding category (replace any spaces ` ` with underscores `_`)
    - Create a new qna.yaml file with examples for the new skill
  
### Detailed Contribution Instructions

#### Pre-requisites

- You need a GitHub account
- You need access to this repo

#### Make a copy of the taxonomy repo

1. Go to [github.com/instruct-lab/taxonomy](https://github.com/instruct-lab/taxonomy)

2. Press the Fork button in the upper right:

    ![fork-button](https://github.com/instruct-lab/taxonomy/assets/799683/8487bff2-425e-483c-b27c-ef03da1c57a8)

3. On the "Create a new fork" form:
    - **Repository name:** `taxonomy` is fine
    - **Description:** This is the description of _your fork_, not of the skills you will create. You can write something that makes sense to you or leave it blank.
    - **Copy the main branch only:** It's OK to leave this checked on.

    When you are ready, press the **Create Fork** button.

    ![Screenshot from 2024-02-28 12-41-59](https://github.com/instruct-lab/taxonomy/assets/799683/656608ef-3040-4858-96f0-9b695bea0e8f)

4. You will get a copy of the taxonomy repo in your github account. This is your own copy, so don't worry about making mistakes or anything like that. *(If you do end up making a mistake and want to start over: you can delete the fork and create a new fork.)*

#### Contributing a skill

In the screenshot, you can see we are under the compositional skills directory. This is the directory under which you want to contribute skills. (The other top-level directory you can contribute to is the knowledge directory, which is a little different than skills. You can read more about the difference between skills and knowledge [community documentation](https://github.com/instruct-lab/community/blob/main/docs/README.md).)

![Screenshot from 2024-02-28 12-44-05](https://github.com/instruct-lab/taxonomy/assets/799683/2038e035-5400-4848-91fb-f575db35b565)

Based on the directories that exist in the tree, make a best guess at where in the tree structure you feel the skill you have to contribute best fits. If you get to a point where you've gone deep enough into the tree and you can't find any directories that match, please feel free to create a new directory or a directory and subdirectories to best represent your skill.

For example, I'd like to contribute a skill for creating puns. Puns are a specific type of joke. I started out in the writing directory of the tree, and saw two main directories there:

![Screenshot from 2024-02-28 12-57-00](https://github.com/instruct-lab/taxonomy/assets/799683/2fab5b92-194a-491e-8a6f-f464a8e8f2f5)

When I looked at the directories under freeform, I saw subdirectories such as brainstorming, debate, legal, poetry, prose, etc.:

![Screenshot from 2024-02-28 12-57-35](https://github.com/instruct-lab/taxonomy/assets/799683/e52ea423-d86f-49a8-9229-b09418f1510b)

When I looked under grounded, I saw subdirectories such as editing, meeting_insights, summarization/wiki_insights:

![Screenshot from 2024-02-28 12-59-10](https://github.com/instruct-lab/taxonomy/assets/799683/98370d70-d7e4-4595-a259-f6ffa4ef00fb)

Puns seemed to fit best under the freeform directory, but I didn't think they fit under any of the pre-existing directories under freeform, so I created a jokes directory, then I created a puns directory under jokes. (I started with jokes as a directory, because I also have a knock-knock joke skill I'd like to create. 🙂)

It can be a little tricky mechanically to create directories in GitHub's web UI:

- Navigate to the folder in which you want to create the directory inside of.

- Click the "Add File" dropdown button in the upper right corner of the screen.

- Start typing the name of the first directory you want to create. In the animation below we use "jokes/" as the first directory.

- When you type the "/" character, the directory name will "lock in" and you'll be able to type the next of the next subdirectory under it, as desired. Below we typed "knock-knock/" as the next directory name.

- Make sure to replace any spaces (` `) in the folder name with underscores (`_`)

- Finally, you'll type the file name. The file name should always be qna.yaml. (qna stands for "Question aNd Answer.")

Here's an animated graphic to show how it works:

![screencast-directory-naming](https://github.com/instruct-lab/taxonomy/assets/799683/2cb2b031-52f6-46de-bfd9-c4eae82ec9d3)

**TO BE CONTINUED**

#### Contributing Knowledge
This information will be added once knowledge contributions are opened up. 

### How should I contribute?

For additional information on how to make a contribution, please, consult the
[documentation on contributing](CONTRIBUTING.md).

### Why should I contribute?

This taxonomy repository will be used as the seed to synthesize the training
data for InstructLab-trained models. We intend to re-train the model(s) using the main
branch as often as possible (at least weekly). This enables fast iteration of the model(s), for the benefit of the open source community, in particular to enable model developers who do not have access to the necessary compute infrastructure.
