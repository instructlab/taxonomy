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
tuned with your data (enhanced via synthetic data generation) using the LAB 🐶
method.

[1] Shivchander Sudalairaj*, Abhishek Bhandwaldar*, Aldo Pareja*, Kai Xu, David D. Cox, Akash Srivastava*. "LAB: Large-Scale Alignment for ChatBots", arXiv preprint arXiv: 2403.01081, 2024. (* denotes equal contributions)

## Choosing domains for the taxonomy

In general, we use the Dewey Decimal Classification (DDC) System to determine our domains (and subdomains) in the taxonomy. This [DDC SUMMARIES document](https://www.oclc.org/content/dam/oclc/dewey/resources/summaries/deweysummaries.pdf) is a great resource for determining where a topic might be classified.

If you are unsure where to put your knowledge or compositional skill, create a folder in the `miscellaneous_unknown` folder under the `knowledge` or `compositional_skills` folders.

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
>
> 1. To select the right subset of the taxonomy to use for data generation.
> 2. To determine the interpretability by human contributors and maintainers.
> 3. As part of the prompt to the LLM used to generate synthetic samples.
<!-- -->
> [!IMPORTANT]
> There is a limit to how much content can exist in the question/answer pairs for the model to process. Due to this, only add a maximum
> of around 2300 words to your question and answer seed example pairs in the `qna.yaml` file.

Compositional skills can either be grounded (includes a context) or ungrounded (does not include a context).  Grounded or ungrounded is declared in the taxonomy tree, for example: `linguistics/writing/poetry/haiku/` (ungrounded) or `grounded/linguistics/grammar` (grounded). The `qna.yaml` is in the final node.

Taxonomy skill files must be a valid [YAML](https://yaml.org/) file named `qna.yaml`. Each `qna.yaml` file contains a set of key/value entries with the following keys:

- `version`: The value must be the number 2. **Required**
- `task_description`: A description of the skill. **Required**
- `created_by`: The GitHub username of the contributor. **Required**
- `seed_examples`: A collection of key/value entries. New
  submissions should have at least five entries, although
  older files may have fewer. **Required**
  - `context`: Grounded skills require the user to provide context containing information that the model is expected to take into account during processing. This is different from knowledge, where the model is expected to gain facts and background knowledge from the tuning process. The context key should not be used for ungrounded skills.
  - `question`: A question for the model. **Required**
  - `answer`: The desired response from the model. **Required**

Other keys at any level are currently ignored.

### Skills: YAML examples

To make the `qna.yaml` files easier and faster for humans to read, it is recommended to specify `version` first, followed by `task_description`, then `created_by`, and finally `seed_examples`.
In `seed_examples`, it is recommended to specify `context` first (if applicable), followed by `question` and `answer`.

*Example `qna.yaml`*

```yaml
version: 2
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

Then, you create an `attribution.txt` file that includes the sources of your information. These can also be self authored sources.

*Example `attribution.txt`*

```text
[Link to source]
[Link to work]
[License of the work]
[Creator name]
```

For more information on what to include in your `attribution.txt` file, see [For your attribution.txt file](https://github.com/instructlab/taxonomy/blob/main/CONTRIBUTING.md#for-your-attributiontxt-file) in CONTRIBUTING.md.

If you have not written YAML before, don't be intimidated - it's just text.

> [!TIP]
>
> - Spaces and indentation matter in YAML. Two spaces to indent.
> - Don't use tabs!
> - Be careful to not have trailing spaces at the end of a line.
> - Each example in `seed_examples` begins with a "-". Place this "-" in
  front of the first field (`question` or `context`). The remaining keys in the
  example should not have this "-".
> - Some special characters such as " and ' need to be escaped with backslash. This is why some
  of the lines for keys in the example YAML start the value with the '|' character followed a new line and then an indented multi-line string.
  This character disables all of the special characters in the value for the key.
  You might also want to use the '|' character for multi-line strings.
> - Consider quoting all values with " to avoid surprising YAML parser behavior
  (e.g. Yes answer can be interpreted by the parser as a boolean of `True`
  value, unless "Yes" is quoted.)
> - See https://yaml-multiline.info/ for more info.

It is recommended that you **lint**, or verify, your YAML using a tool. One linter option is [yamllint.com](https://yamllint.com). You can copy/paste your YAML into the box and click **Go** to have it analyze your YAML and make recommendations. Online tools like [prettified](https://onlineyamltools.com/prettify-yaml) and [yaml-validator](https://jsonformatter.org/yaml-validator) can automatically reformat your YAML to adhere to our `yamllint` PR checks, such as breaking lines longer than 120 characters.

#### Ungrounded compositional skill: YAML example

```yaml
version: 2
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

#### Ungrounded compositional skill: Directory tree example

```ascii
[...]

└── writing
    └── poetry
    |   └── haiku <=== here it is :)
    |   |   └── qna.yaml
    |   |       attribution.txt
        [...]
    └── prose
    |   └── debate
    |   |   └── qna.yaml
    |   |       attribution.txt
    [...]

[...]
```

#### Grounded compositional skill: YAML example

Remember that [grounded compositional skills](docs/SKILLS_GUIDE.md) require additional context and include a `context` field.

This example snippet assumes the GitHub username `mairin` and shows some of the question/answer pairs present in the actual file:

```yaml
version: 2
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

grounded
└── technology
    └── machine_learning
        └── natural_language_processing
    |   |     └── information_extraction
    |            └── inference
    |   |            └── qualitative
    |   |               ├── sentiment
    |   |               |     └── qna.yaml
    |   |               |         attribution.txt
    │                   ├── quantitative
    │   │                   ├── table_analysis <=== here it is :)
    │   |   |               |     └── qna.yaml
    │   │   │               |         attribution.txt

[...]
```

## Getting Started with Knowledge Contributions

While skills are foundational or performative, knowledge is based more on answering questions that involve facts,
data, or references.

Knowledge is supported by documents, such as a textbook, technical manual, encyclopedia, journal, or magazine.

Knowledge in the taxonomy tree consists of a few more elements than skills:

> [!IMPORTANT]
> If you are using InstructLab version `0.21.0` or above, you can specify PDF files in your knowledge `qna.yaml` file as a valid document type. Any previous version of InstructLab still only consumes knowledge documents in markdown format.

- Each knowledge node in the tree has a `qna.yaml`, similar to the format of the `qna.yaml` for skills.
- ⭐ Knowledge submissions require you to create a Git repository, can be with GitHub, that contains the files of your knowledge contributions.
- The `qna.yaml` includes parameters that contain information from your repository.

> [!TIP]
> Guidelines for Knowledge contributions
>
> - Submit the most up-to-date version of the document
> - All submissions must be text, images will be ignored
> - Do not use tables in your markdown freeform contribution

The `qna.yaml` format must include the following fields:

- `version`: The version of the qna.yaml file, this is the format of the file used for SDG. The value must be the number 3.
- `created_by`: Your GitHub username.
- `domain`: Specify the category of the knowledge.
- `seed_examples`: A collection of key/value entries.
  - `context`: A chunk of information from the knowledge document. Each `qna.yaml` needs five `context` blocks and has a maximum word count of 500 words.
  - `questions_and_answers`: The parameter that holds your questions and answers
    - `question`: Specify a question for the model. Each `qna.yaml` file needs at least three question and answer pairs per `context` chunk with a maximum word count of 250 words.
    - `answer`: Specify the desired answer from the model. Each `qna.yaml` file needs at least three question and answer pairs per `context` chunk with a maximum word count of 250 words.
- `document_outline`: Describe an overview of the document your submitting.
- `document`: The source of your knowledge contribution.
  - `repo`: The URL to your repository that holds your knowledge files.
  - `commit`: The SHA of the commit in your repository with your knowledge files.
  - `patterns`: A list of glob patterns specifying the files in your repository. Any glob pattern that starts with `*`, such as `*.md`, must be quoted due to YAML rules. For example, `"*.md"`.

### Knowledge: YAML examples

```yaml
version: 3
domain: astronomy
created_by: juliadenham
seed_examples:
  - context: |
      **Phoenix** is a minor [constellation](constellation "wikilink") in the
      [southern sky](southern_sky "wikilink"). Named after the mythical
      [phoenix](Phoenix_(mythology) "wikilink"), it was first depicted on a
      celestial atlas by [Johann Bayer](Johann_Bayer "wikilink") in his 1603
      *[Uranometria](Uranometria "wikilink")*. The French explorer and
      astronomer [Nicolas Louis de
      Lacaille](Nicolas_Louis_de_Lacaille "wikilink") charted the brighter
      stars and gave their [Bayer designations](Bayer_designation "wikilink")
      in 1756. The constellation stretches from roughly −39 degrees to −57 degrees
      [declination](declination "wikilink"), and from 23.5h to 2.5h of [right
      ascension](right_ascension "wikilink"). The constellations Phoenix,
      [Grus](Grus_(constellation) "wikilink"),
      [Pavo](Pavo_(constellation) "wikilink") and [Tucana](Tucana "wikilink"),
      are known as the Southern Birds.
    questions_and_answers:
      - question: |
          What is the Phoenix constellation?
        answer: |
          Phoenix is a minor constellation in the southern sky.
      - question: |
          Who charted the Phoenix constellation?
        answer: |
          The Phoenix constellation was charted by french explorer and
          astronomer Nicolas Louis de Lacaille.
      - question: |
          How far does the Phoenix constellation stretch?
        answer: |
          The phoenix constellation stretches from roughly −39° to −57°
          declination, and from 23.5h to 2.5h of right ascension.
  - context: |
      Phoenix was the largest of the 12 constellations established by [Petrus
      Plancius](Petrus_Plancius "wikilink") from the observations of [Pieter
      Dirkszoon Keyser](Pieter_Dirkszoon_Keyser "wikilink") and [Frederick de
      Houtman](Frederick_de_Houtman "wikilink"). It first appeared on a 35cm
      diameter celestial globe published in 1597 (or 1598) in Amsterdam by
      Plancius with [Jodocus Hondius](Jodocus_Hondius "wikilink"). The first
      depiction of this constellation in a celestial atlas was in [Johann
      Bayer](Johann_Bayer "wikilink")'s
      *[Uranometria](Uranometria "wikilink")* of 1603. De Houtman included
      it in his southern star catalog the same year under the Dutch name *Den
      voghel Fenicx*, "The Bird Phoenix", symbolising the
      [phoenix](Phoenix_(mythology) "wikilink") of classical mythology. One
      name of the brightest star [Alpha
      Phoenicis](Alpha_Phoenicis "wikilink")—Ankaa—is derived from the Arabic:
      العنقاء, romanized: al-‘anqā’, lit. 'the phoenix', and
      was coined sometime after 1800 in relation to the constellation.
    questions_and_answers:
      - question: |
          What is the brightest star in the Phoenix constellation
          called?
        answer: |
          Alpha Phoenicis or Ankaa is the brightest star in the Phoenix
          Constellation.
      - question: Where did the Phoenix constellation first appear?
        answer: |
          The Phoenix constellation first appeared on a 35-cm diameter
          celestial globe published in 1597 (or 1598) in Amsterdam by
          Plancius with Jodocus Hondius.
      - question: |
          What does "The Bird Phoenix" symbolize?
        answer: |
          "The Bird Phoenix" symbolizes the phoenix of classical mythology.
  - context: |
      Phoenix is a small constellation bordered by [Fornax](Fornax "wikilink")
      and Sculptor to the north, Grus to the west, Tucana to the south,
      touching on the corner of [Hydrus](Hydrus "wikilink") to the south, and
      [Eridanus](Eridanus_(constellation) "wikilink") to the east and
      southeast. The bright star [Achernar](Achernar "wikilink") is
      nearby. The three-letter abbreviation for the constellation, as
      adopted by the [International Astronomical
      Union](International_Astronomical_Union "wikilink") in 1922, is
      "Phe". The official constellation boundaries, as set by Belgian
      astronomer [Eugène Delporte](Eugène_Joseph_Delporte "wikilink") in 1930,
      are defined by a polygon of 10 segments. In the [equatorial coordinate
      system](equatorial_coordinate_system "wikilink"), the [right
      ascension](right_ascension "wikilink") coordinates of these borders lie
      between 23<sup>h</sup> 26.5<sup>m</sup> and 02<sup>h</sup> 25.0<sup>m</sup>,
      while the [declination](declination "wikilink")
      coordinates are between −39.31° and −57.84°. This means it remains
      below the horizon to anyone living north of the [40th
      parallel](40th_parallel_north "wikilink") in the [Northern
      Hemisphere](Northern_Hemisphere "wikilink"), and remains low in the sky
      for anyone living north of the [equator](equator "wikilink"). It is most
      visible from locations such as Australia and South Africa during late
      [Southern Hemisphere](Southern_Hemisphere "wikilink") spring. Most
      of the constellation lies within, and can be located by, forming a
      triangle of the bright stars Achernar, [Fomalhaut](Fomalhaut "wikilink")
      and [Beta Ceti](Beta_Ceti "wikilink")—Ankaa lies roughly in the centre
      of this.
    questions_and_answers:
      - question: What are the characteristics of the Phoenix constellation?
        answer: |
          Phoenix is a small constellation bordered by Fornax and Sculptor to
          the north, Grus to the west, Tucana to the south, touching on the
          corner of Hydrus to the south, and Eridanus to the east and southeast.
          The bright star Achernar is nearby.
      - question: |
          When is the phoenix constellation most visible?
        answer: |
          Phoenix is most visible from locations such as Australia and
          South Africa during late Southern Hemisphere spring.
      - question: |
          What are the Phoenix Constellation boundaries?
        answer: |
          The official constellation boundaries for Phoenix, as set by Belgian
          astronomer Eugène Delporte in 1930, are defined by a polygon of 10
          segments.
  - context: |
      Ten stars have been found to have planets to date, and four planetary
      systems have been discovered with the [SuperWASP](SuperWASP "wikilink")
      project. [HD 142](HD_142 "wikilink") is a yellow giant that has an
      apparent magnitude of 5.7, and has a planet ([HD 142b](HD_142_b
      "wikilink")) 1.36 times the mass of Jupiter which orbits every 328 days.
      [HD 2039](HD_2039 "wikilink") is a yellow subgiant with an apparent
      magnitude of 9.0 around 330 light years away which has a planet ([HD 2039
      b](HD_2039_b "wikilink")) six times the mass of Jupiter. [WASP-18](WASP-18
      "wikilink") is a star of magnitude 9.29 which was discovered to have a hot
      Jupiter-like planet ([WASP-18b](WASP-18b "wikilink")) taking less than a
      day to orbit the star. The planet is suspected to be causing WASP-18 to
      appear older than it really is. [WASP-4](WASP-4 "wikilink") and
      [WASP-5](WASP-5 "wikilink") are solar-type yellow stars around 1000
      light years distant and of 13th magnitude, each with a single planet
      larger than Jupiter. [WASP-29](WASP-29 "wikilink") is an orange
      dwarf of spectral type K4V and visual magnitude 11.3, which has a
      planetary companion of similar size and mass to Saturn. The planet
      completes an orbit every 3.9 days.
    questions_and_answers:
      - question: In the Phoenix constellation, how many stars have planets?
        answer: |
          In the Phoenix constellation, ten stars have been found to have
          planets to date, and four planetary systems have been discovered
          with the SuperWASP project.
      - question: |
          What is HD 142?
        answer: |
          HD 142 is a yellow giant that has an apparent magnitude of 5.7, and
          has a planet (HD 142 b) 1.36 times the mass of Jupiter which
          orbits every 328 days.
      - question: |
          Are WASP-4 and WASP-5 solar-type yellow stars?
        answer: |
          Yes, WASP-4 and WASP-5 are solar-type yellow stars around 1000 light
          years distant and of 13th magnitude, each with a single planet
          larger than Jupiter.
  - context: |
      The constellation does not lie on the
      [galactic plane](galactic_plane "wikilink") of the Milky Way, and there
      are no prominent star clusters. [NGC 625](NGC_625 "wikilink") is a dwarf
      [irregular galaxy](irregular_galaxy "wikilink") of apparent magnitude 11.0
      and lying some 12.7 million light years distant. Only 24000 light years in
      diameter, it is an outlying member of the [Sculptor Group](Sculptor_Group
      "wikilink"). NGC 625 is thought to have been involved in a collision and
      is experiencing a burst of [active star formation](Active_galactic_nucleus
      "wikilink"). [NGC 37](NGC_37 "wikilink") is a
      [lenticular galaxy](lenticular_galaxy "wikilink") of apparent magnitude
      14.66. It is approximately 42 [kiloparsecs](kiloparsecs "wikilink")
      (137,000 [light-years](light-years "wikilink")) in diameter and about
      12.9 billion years old. [Robert's Quartet](Robert's_Quartet "wikilink")
      (composed of the irregular galaxy [NGC 87](NGC_87 "wikilink"), and three
      spiral galaxies [NGC 88](NGC_88 "wikilink"), [NGC 89](NGC_89 "wikilink")
      and [NGC 92](NGC_92 "wikilink")) is a group of four galaxies located
      around 160 million light-years away which are in the process of colliding
      and merging. They are within a circle of radius of 1.6 arcmin,
      corresponding to about 75,000 light-years. Located in the galaxy ESO
      243-49 is [HLX-1](HLX-1 "wikilink"), an
      [intermediate-mass black hole](intermediate-mass_black_hole
      "wikilink")—the first one of its kind identified. It is thought to be a
      remnant of a dwarf galaxy that was absorbed in a
      [collision](Interacting_galaxy "wikilink") with ESO 243-49. Before its
      discovery, this class of black hole was only hypothesized.
    questions_and_answers:
      - question: |
          Is the Phoenix Constellation part of the Milky Way?
        answer: |
          The Phoenix constellation does not lie on the galactic plane of
          the Milky Way, and there are no prominent star clusters.
      - question: |
          How many light years away is NGC 625?
        answer: |
          NGC 625 is 24000 light years in diameter and is an outlying
          member of the Sculptor Group.
      - question: |
          What is Robert's Quartet composed of?
        answer: |
          Robert's Quartet is composed of the irregular galaxy NGC 87,
          and three spiral galaxies NGC 88, NGC 89 and NGC 92.
document_outline: |
  Information about the Phoenix Constellation including the
  history, characteristics, and features of the stars in the constellation.
document:
  repo: https://github.com/juliadenham/Summit_knowledge
  commit: 0a1f2672b9b90582e6115333e3ed62fd628f1c0f
  patterns:
    - phoenix_constellation.md

```

*Example `attribution.txt` file*

```text
Title of work: Phoenix (constellation)
Link to work: https://en.wikipedia.org/wiki/Phoenix_(constellation)
Revision: https://en.wikipedia.org/w/index.php?title=Phoenix_(constellation)&oldid=1237187773
License of the work: CC-BY-SA-4.0
Creator names: Wikipedia Authors
```

This knowledge example references one markdown file: `phoenix_constellation.md`. You can also add multiple files for knowledge contributions.

> [!NOTE]
> Due to the higher volume, **it will naturally take longer to receive acceptance for
> a knowledge contribution pull request than for a skill pull request**. Smaller
> pull requests are simpler and require less time and effort to review.

What might these markdown files look like? They can be freeform. Here's what a
snippet of `phoenix_constellation.md` might look like in your Git repository.

#### Knowledge: Markdown file example

```markdown
# Phoenix (constellation)

**Phoenix** is a minor [constellation](constellation "wikilink") in the
[southern sky](southern_sky "wikilink"). Named after the mythical
[phoenix](Phoenix_(mythology) "wikilink"), it was first depicted on a
celestial atlas by [Johann Bayer](Johann_Bayer "wikilink") in his 1603
*[Uranometria](Uranometria "wikilink")*. The French explorer and
astronomer [Nicolas Louis de
Lacaille](Nicolas_Louis_de_Lacaille "wikilink") charted the brighter
stars and gave their [Bayer designations](Bayer_designation "wikilink")
in 1756. The constellation stretches from roughly −39 degrees to −57 degrees
[declination](declination "wikilink"), and from 23.5h to 2.5h of [right
ascension](right_ascension "wikilink"). The constellations Phoenix,
[Grus](Grus_(constellation) "wikilink"),
[Pavo](Pavo_(constellation) "wikilink") and [Tucana](Tucana "wikilink"),
are known as the Southern Birds.

The brightest star, [Alpha Phoenicis](Alpha_Phoenicis "wikilink"), is
named Ankaa, an [Arabic](Arabic "wikilink") word meaning 'the Phoenix'.
It is an orange giant of apparent magnitude 2.4. Next is [Beta
Phoenicis](Beta_Phoenicis "wikilink"), actually a
[binary](Binary_star "wikilink") system composed of two yellow giants
with a combined apparent magnitude of 3.3. [Nu
Phoenicis](Nu_Phoenicis "wikilink") has a dust disk, while the
constellation has ten star systems with known planets and the recently
discovered [galaxy clusters](galaxy_cluster "wikilink") [El
Gordo](El_Gordo_(galaxy_cluster) "wikilink") and the [Phoenix
Cluster](Phoenix_Cluster "wikilink")—located 7.2 and 5.7 billion light
years away respectively, two of the largest objects in the [visible
universe](visible_universe "wikilink"). Phoenix is the
[radiant](radiant_(meteor_shower) "wikilink") of two annual [meteor
showers](meteor_shower "wikilink"): the
[Phoenicids](Phoenicids "wikilink") in December, and the July
Phoenicids.
```

In the taxonomy repository, here's what the previously referenced knowledge might look like in the tree:

#### Knowledge: directory tree example

```ascii
[...]

└── knowledge
    └── science
        ├── astronomy
        │ └── constellations
        │     └── Phoenix <=== here it is :)
        │     |    └── qna.yaml
        |     |        attribution.txt
        │     └── Orion
        │          └── qna.yaml
        |              attribution.txt
[...]
```

For more information on what to include in your `attribution.txt` file, see [For your attribution.txt file](https://github.com/instructlab/taxonomy/blob/main/CONTRIBUTING.md#for-your-attributiontxt-file) in CONTRIBUTING.md.

You can organize the knowledge markdown files in your repository however you want. You just need to ensure the YAML is pointing to the correct file.

## Taxonomy tree Layout

The taxonomy tree is organized in a cascading directory structure. At the end of
each branch, there is a YAML file (qna.yaml) that contains the examples for that
domain. Maintainers can decide to change the names of the existing branches or to add new branches.

> [!IMPORTANT]
> Folder names do not have spaces. Use underscores between words.

Below is an illustrative directory structure to show this layout:

```ascii
.
└── linguistics
    ├── writing
    │   ├── brainstorming
    │   │   ├── idea_generation
    |   │       └── qna.yaml
    │   │           attribution.txt
    │   │   ├── refute_claim
    |   │       └── qna.yaml
    │   │           attribution.txt
    │   ├── prose
    │   │   ├── articles
    │   │       └── qna.yaml
    │   │           attribution.txt
    └── grammar
        └── qna.yaml
        │   attribution.txt
        └── spelling
            └── qna.yaml
                attribution.txt
```

For an extensive example of this layout see, [taxonomy_tree_layout](docs/taxonomy_diagram.md) in the documentation folder.

## Contribute knowledge and skills to the taxonomy

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

To contribute to this repo, you'll use the *Fork and Pull* model common in many open source repositories. You can add your skills and knowledge to the taxonomy in multiple ways; for additional information on how to make a contribution, see the [Documentation on contributing](CONTRIBUTING.md). You can also use the following guides to help with contributing:

- Contributing using the [GitHub webpage UI](docs/contributing_via_GH_UI.md).
- Contributing knowledge to the taxonomy in the [Knowledge contribution guidelines](docs/knowledge-contribution-guide.md).

### Why should I contribute?

This taxonomy repository will be used as the seed to synthesize the training
data for InstructLab-trained models. We intend to retrain the model(s) using the main
branch as often as possible (at least weekly).
Fast iteration of the model(s) benefits the open source community and enables model developers who do not have access to the necessary compute infrastructure.
