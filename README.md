# InstructLab 🐶 Taxonomy

## Contents 📖 

- [Welcome to the InstructLab Taxonomy](#welcome-to-the-instructlab-taxonomy)
- [Learning](#learning)
- [Getting Started with Skill Contributions](#getting-started-with-skill-contributions)
  - [Skills: YAML examples](#skills-yaml-examples)
- [Getting Started with Knowledge Contributions](#getting-started-with-knowledge-contributions)
  - [Knowledge: YAML examples](#knowledge-yaml-examples)
- [Taxonomy tree layout](#taxonomy-tree-layout)
- [Contribute knowledge and skills to the taxonomy!](#contribute-knowledge-and-skills-to-the-taxonomy)
  - [Ways to contribute](#ways-to-contribute)
  - [How to contribute skills and knowledge](#how-to-contribute-skills-and-knowledge)
## Welcome to the InstructLab Taxonomy

InstructLab 🐶 uses a novel synthetic data-based alignment tuning method for
Large Language Models (LLMs.) The "**lab**" in Instruct**Lab** 🐶 stands for
[**L**arge-Scale **A**lignment for Chat**B**ots](https://arxiv.org/abs/2403.01081) [1].

The LAB method is driven by taxonomies, which are largely created manually and
with care.

This repository contains a taxonomy tree that allows you to create models
tuned with your data (enhanced via synthetic data generation) using LAB 🐶
method.

[1] Shivchander Sudalairaj*, Abhishek Bhandwaldar*, Aldo Pareja*, Kai Xu, David D. Cox, Akash Srivastava*. "LAB: Large-Scale Alignment for ChatBots", arXiv preprint arXiv: 2403.01081, 2024. (* denotes equal contributions)

## Learning

Learn about the concepts of "skills" and "knowledge" in our [InstructLab Community Learning Guide](https://github.com/instructlab/community/blob/main/docs/README.md).

## Getting Started with Skill Contributions

Skills require a much smaller volume of content than knowledge contributions. An entire skill contribution to the taxonomy tree can be just a few lines of YAML in the `qna.yaml` file ("qna" is short for "questions and answers") and an `attribution.txt` file for citing sources. 

Your skills contribution pull requests must include the following:
- A `qna.yaml` that contains a set of key/value entries with the following keys
  - Each `qna.yaml` file requires a minimum of five question and answer pairs.
- An `attribution.txt` that includes the sources for the information used in the `qna.yaml`

> [!TIP]
> The skill taxonomy structure is used in several ways:
>    1. To select the right subset of the taxonomy to use for data generation.
>    2. To determine the interpretability by human contributors and maintainers.
>    3. As part of the prompt to the GPT model used to generate synthetic samples.

> [!IMPORTANT]
> There is a limit to how much content can exist in the question/answer pairs for the model to process. Due to this, only add a maximum
> of around 2300 words to your question and answer seed example pairs in the `qna.yaml` file.

Taxonomy skill files must be a valid [YAML](https://yaml.org/) file named `qna.yaml`. Each `qna.yaml` files contains a set of key/value entries with the following keys:

- `task_description`: A description of the skill. **Required**
- `created_by`: The GitHub username of the contributor. **Required**
- `seed_examples`: A collection of key/value entries. New
  submissions should have at least five entries, although
  older files may have fewer. **Required**
  - `context`: Grounded skills require the user to provide context containing information that the model is expected to take into account during processing. This is different from knowledge, where the model is expected to gain facts and background knowledge from the tuning process. The context key is optional for freeform skills.
  - `question`: A question for the model. **Required**
  - `answer`: The desired response from the model. **Required**

Other keys at any level are currently ignored.

### Skills: YAML examples

To make the `qna.yaml` files easier and faster for humans to read, it is recommended to specify `task_description` first, followed by `created_by`, and finally `seed_examples`.
In `seed_examples`, it is recommended to specify `context` first (if applicable), followed by `question` and `answer`.

*Example `qna.yaml`*
```yaml
task_description: <string>
created_by: <string>
seed_examples:
  - question: <string>
    answer: |
      <multi-line string>
  - context: |
      <multi-line string>
    question: <string>
    answer: |
      <multi-line string>
  ...  
```

Then, you create an `attribution.txt` file that includes the sources of your information. These can also be self authored. 

*Example `attribution.txt`*
```
[Link to source] 
[Link to work]
[License of the work]
[Creator name]
```
For more information on what to include in your `attribution.txt` file, see [For your attribution.txt file](https://github.com/instructlab/taxonomy/blob/main/CONTRIBUTING.md#for-your-attributiontxt-file) in CONTRIBUTING.md.

If you have not written YAML before, don't be intimidated - it's just text.

> [!TIP]
> - Spaces and indentation matter in YAML. Two spaces to indent.
> - Don't use tabs!
> - Be careful to not have trailing spaces at the end of a line.
> - Each example in `seed_examples` begins with a "-". Place this "-" in
  front of the first field (`question` or `context`). The remaining keys in the
  example should not have this "-".
> - Some special characters such as " and ' need to be "escaped." This is why some
  of the lines for keys in the example YAML we provided have the '|' character.
  This character escapes all of the special characters in the value for the key.
  You might also want to use the '|' character for multi-line strings.
> - Consider quoting all values with " to avoid surprising YAML parser behavior
  (e.g. Yes answer can be interpreted by the parser as a boolean of `True`
  value, unless "Yes" is quoted.)

It is recommended that you **lint**, or verify your YAML using a tool. One linter option is [yamllint.com](https://yamllint.com). You can copy/paste your YAML into the box and click **Go** to have it analyze your YAML and make recommendations. Online tools like [prettified](https://onlineyamltools.com/prettify-yaml) and [yaml-validator](https://jsonformatter.org/yaml-validator) can automatically reformat your YAML to adhere to our `yamllint` PR checks, such as breaking lines longer than 120 characters.

#### Freeform compositional skill: YAML example

```yaml
task_description: 'Teach the model how to rhyme.'
created_by: juliadenham
seed_examples:
  - question: What are 5 words that rhyme with horn?
    answer: warn, torn, born, thorn, and corn.
  - question: What are 5 words that rhyme with cat?
    answer: bat, gnat, rat, vat, and mat.
  - question: What are 5 words that rhyme with poor?
    answer: door, shore, core, bore, and tore. 
  - question: What are 5 words that rhyme with bank?
    answer: tank, rank, prank, sank, and drank.
  - question: What are 5 words that rhyme with bake?
    answer: wake, lake, steak, make, and quake.
```
Seriously, that's it.

Here is the location of this YAML in the taxonomy tree. Note that the YAML file
itself, plus any added directories that contain the file, is the entirety of the skill
in terms of a taxonomy contribution:

#### Freeform compositional skill: Directory tree example

```ascii
[...]

└── writing
    └── freeform
    |   └── haikus <=== here it is :)
    |   |   └── qna.yaml
    |   |       attribution.txt 
    │   ├── debate
    │   │   └── qna.yaml
    |   |       attribution.txt   
    │   ├── legal
    │   │   ├── agreement
    │   │   |    └── qna.yaml
    |   |   |        attribution.txt
[...]
```

#### Grounded compositional skill: YAML example

Remember that [grounded compositional skills](https://github.com/instructlab/community/blob/main/docs/SKILLS_GUIDE.md) require additional context and include a `context` field. 

This example snippet assumes the GitHub username `mairin` and shows some of the question/answer pairs present in the actual file:

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
```

#### Grounded compositional skill: Directory tree example

```ascii
[...]

└── extraction
    └── inference
    |   └── qualitative
    |   |    ├── sentiment
    |   |    |    └── qna.yaml
    |   |    |        attribution.txt 
    |   |    └── tone_and_style
    |   |         └── qna.yaml
    |   |             attribution.txt
    │   ├── quantitative
    │   │   ├── table_analysis <=== here it is :)
    │   |   |    └── qna.yaml
    │   │   │        attribution.txt
    │   │   ├── word_frequency
    │   │   │   └── qna.yaml
    │   │   │       attribution.txt
[...]
```
## Getting Started with Knowledge Contributions

> [!IMPORTANT]
> Upon release, the taxonomy repository is only accepting contributions from Wikipedia and is capped at 50 contributions. If you want to add knowledge to the taxonomy repository, please fill out this [InstructLab Knowledge Submission Registration](https://docs.google.com/forms/d/1VWJ_XPwH3gBTIXCabpWc0I5pjWIlXETMSFKXc8fpgkA/viewform?edit_requested=true) form and await acceptance! Please do not add contributions if you do not receive the confirmation email. Thank you!

While skills are foundational or performative, knowledge is based more on answering questions that involve facts,
data, or references.

Knowledge in the taxonomy tree consists of a few more elements than skills:

- Each knowledge node in the tree has a `qna.yaml`, similar to the format of the `qna.yaml` for skills.
- ⭐ Knowledge submissions require you to create a Git repository, can be with GitHub, that contains the markdown files of your knowledge contributions. These contributions in your repository must use the markdown (.md) format.
- The `qna.yaml` includes parameters that contain information from your repository.

> [!TIP] 
> Guidelines for Knowledge contributions
> - Submit the most up-to-date version of the document
> - All submissions must be text, images will be ignored
> - Do not use tables in your markdown freeform contribution 

> [!IMPORTANT]
> There is a limit to how much content can exist in the question/answer pairs for the model to process. Due to this, only add a maximum
> of around 2300 words to your question and answer seed example pairs in the `qna.yaml` file.

Each `qna.yaml` file requires a minimum of five question-answer pairs. The `qna.yaml` format must include the following fields:
ˇ
- `task_description`: An optional description of the knowledge.
- `created_by`: Your GitHub username.
- `domain`: Category of the knowledge. 
- `seed_examples`: Five or more examples sourced from the provided knowledge documents.
  - `question`: A question for the model. This key is required.
  - `answer`: The desired response from the model. This key is required.
- `document`: The source of your knowledge contribution.
  - `repo`: The URL to your repository that holds your knowledge markdown files.
  - `commit`: The SHA of the commit in your repository with your knowledge markdown files.
  - `patterns`: A list of glob patterns specifying the markdown files in your repository. Any glob pattern that starts with `*`, such as `*.md`, must be quoted due to YAML rules. For example, `"*.md"`.

### Knowledge: YAML examples
```yaml
task_description: 'Teach the model the results of the 2024 oscars'
created_by: juliadenham
domain: pop_culture
seed_examples:
 - question: When did the 2024 oscars happen?
   answer: |
     The 2024 oscars were held on March 10, 2024.
 - question: What film had the most oscar nominations in 2024?
   answer: |
     Oppenheimer had 13 oscar nominations.
 - question: Who presented the awards for Best Original Screenplay and Best Adapted Screenplay?
   answer: |
     Octavia Spencer.
 - question: Who hosted the 2024 oscars?
   answer: |
     Jimmy Kimmel hosted the 96th Academy Awards ceremony.
 - question: At the 2024 Oscars, who were the nominees for best director and who won?
   answer: |
     The nominees for director at the 2024 oscars was Christopher Nolan for Oppenheimer,
     Justine Triet for Anatomy of a Fall, Martin Scorsese for Killers of the Flower Moon,
     Yorgos Lanthimos for Poor Things, and Jonathan Glazer for The Zone of Interest.
     Christopher Nolan won best director for Oppenheimer.
 - question: Did Billie Eilish perform at the 2024 oscars?
   answer: |
     Yes Billie Eilish performed "What Was I Made For?" from Barbie.
document:
 repo: https://github.com/juliadenham/oscars2024_knowledge.git
 commit: a22148c
 patterns:
   - oscars2024_results.md
```

*Example `attribution.txt` file*
```
Title of work: 96th Academy Awards
Link to work: https://en.wikipedia.org/wiki/96th_Academy_Awards 
License of the work: CC-BY-SA-4.0
Creator names: Wikipedia Authors
```

This knowledge example references one markdown file: `oscars2024_results.md`. You can also add multiple files for knowledge contributions. 

> [!NOTE]
> Due to the higher volume, **it will naturally take longer to receive acceptance for
> a knowledge contribution pull request than for a skill pull request**. Smaller
> pull requests are simpler and require less time and effort to review.

What might these markdown files look like? They can be freeform. Here's what a
snippet of `oscars2024_results.md` might look like in your Git repository.

#### Knowledge: Freeform example

```markdown
# 96th Academy awards

The **96th Academy Awards** ceremony, which was presented by the
[Academy of Motion Picture Arts and
Sciences](Academy_of_Motion_Picture_Arts_and_Sciences "wikilink")
(AMPAS), took place on March 10, 2024, at the [Dolby
Theatre](Dolby_Theatre "wikilink") in
[Hollywood](Hollywood,_Los_Angeles "wikilink"), Los Angeles.[1] During
the gala, the AMPAS presented [Academy
Awards](Academy_Awards "wikilink") (commonly referred to as Oscars) in
23 categories honoring [films released in
2023](2023_in_film "wikilink"). Comedian [Jimmy
Kimmel](Jimmy_Kimmel "wikilink") hosted the show for the fourth time.

The nominations were announced on January 23, 2024.
*[Oppenheimer](Oppenheimer_(film) "wikilink")* led with 13 nominations,
followed by *[Poor Things](Poor_Things_(film) "wikilink")* and *[Killers
of the Flower Moon](Killers_of_the_Flower_Moon_(film) "wikilink")* with
11 and 10, respectively.[2][3][4] *Oppenheimer* won a leading seven
awards, including [Best
Picture](Academy_Award_for_Best_Picture "wikilink") and [Best
Director](Academy_Award_for_Best_Director "wikilink")
[..]
```

In the taxonomy repository, here's what the previously referenced knowledge might look like in the tree:

#### Knowledge: directory tree example 

```ascii
[...]

└── knowledge
    └── textbooks
        ├── culture
        │ └── movies
        │     └── awards
        │         ├── oscars  <=== here it is :)
        │         │   └── qna.yaml
        |         |       attribution.txt
        │         └── golden_globes_movies
        │             └── qna.yaml
        |                 attribution.txt
[...]
```
For more information on what to include in your `attribution.txt` file, see [For your attribution.txt file](https://github.com/instructlab/taxonomy/blob/main/CONTRIBUTING.md#for-your-attributiontxt-file) in CONTRIBUTING.md.

You can organize the knowledge markdown files in your repository however you want. You just need to ensure the YAML is pointing to the correct file. 

## Taxonomy tree Layout

The taxonomy tree is organized in a cascading directory structure. At the end of
each branch, there is a YAML file (qna.yaml) that contains the examples for that
domain. Maintainers can decide to change the names of the existing branches or to add new branches.

> [!IMPORTANT] 
> Folder names do not have spaces. 

Below is an illustrative directory structure to show this layout:

```ascii
.
└── writing
    ├── freeform
    │   ├── brainstorming
    │   │   ├── idea_generation
    │   │   │   └── qna.yaml
    │   │   │       attribution.txt
    │   │   ├── refute_claim
    │   │   │   └── qna.yaml
    │   │   │       attribution.txt
    │   ├── prose
    │   │   ├── articles
    │   │   │   └── qna.yaml
    │   │   │       attribution.txt
    │   │   ├── emails
    │   │   │   ├── formal
    │   │   │   │   └── qna.yaml
    │   │   │   │       attribution.txt
    │   │   │   └── informal
    │   │   │       └── qna.yaml
    │   │   │           attribution.txt
    └── grounded
        ├── editing
        │   ├── grammar
        │   │   └── qna.yaml
        │   │       attribution.txt
        │   └── spelling
        │       └── qna.yaml
        │           attribution.txt
        └── summarization
            └── wiki_insights
                └── concise
                    └── qna.yaml
                        attribution.txt
```

For an extensive example of this layout see, [taxonomy_tree_layout](https://github.com/instructlab/taxonomy/tree/main/docs/taxonomy_tree_layout.md) in the documentation folder.

## Contribute knowledge and skills to the taxonomy!

The ability to contribute to a Large Language Model (LLM) has been difficult in no small part because it is difficult to get access to the necessary compute infrastructure.

This taxonomy repository will be used as the seed to synthesize the training data for InstructLab-trained models. We intend to retrain the model(s) using the main branch following InstructLab's progressive training on a regular basis. This enables fast iteration of the model(s), for the benefit of the open source community.

By contributing your skills and knowledge to this repository, you will see your changes built into an LLM within days of your contribution rather than months or years! If you are working with a model and notice its knowledge or ability lacking, you can correct it by contributing knowledge or skills and check if it's improved after your changes are built.

While public contributions are welcome to help drive community progress, you can also fork this repository under [the Apache License, Version 2.0](LICENSE), add your own internal skills, and train your own models internally. However, you might need your own access to significant compute infrastructure to perform sufficient retraining.

## Ways to Contribute

You can contribute to the taxonomy in the following two ways:

1. Adding new examples to **existing leaf nodes**:
2. Adding **new branches/skills** corresponding to the existing domain:

For more information, see the [Ways of contributing to the taxonomy repository](https://github.com/instructlab/taxonomy/blob/main/CONTRIBUTING.md#ways-of-contributing-to-the-taxonomy-repository) documentation. 
## How to contribute skills and knowledge

To contribute to this repo, you'll use the _Fork and Pull_ model common in many open source repositories. You can add your skills and knowledge to the taxonomy in multiple ways; for additional information on how to make a contribution, see the [Documentation on contributing](CONTRIBUTING.md). You can also use the following guides to help with contributing: 
- Contributing using the [GitHub webpage UI](docs/contributing_via_GH_UI.md).
- Contributing knowledge to the taxonomy in the [Knowledge contribution guidelines](docs/knowledge-contribution-guide.md).

### Why should I contribute?

This taxonomy repository will be used as the seed to synthesize the training
data for InstructLab-trained models. We intend to retrain the model(s) using the main
branch as often as possible (at least weekly). Fast iteration of the model(s) benefits the open source community and enables model developers who do not have access to the necessary compute infrastructure.
