# Labrador 🐶 (LAB) Taxonomy

Labrador 🐶 is a novel synthetic data-based alignment tuning method for Large 
Language Models (LLMs.) The "**lab**" in **Lab**rador 🐶 stands for **L**arge-scale **A**lignment for Chat **B**ots.

The LAB method is driven by taxonomies, which are largely created manually and with care.

This repository contains a taxonomy tree that will allow you to create models tuned with your data (enhanced via synthetic data generation) using the Labrador 🐶 method!

Top-level categories:

1. **Knowledge**:

    Knowledge is like data and facts. It's backed by documents. When creating knowledge for a model, you're giving it additional data so it can answer questions more accurately. 
2. **Compositional Skills**: 

    Skills are performative. When creating a skill for the model, you're teaching it how to do something: "write me a song," "talk like a pirate," "summarize an email."
3. **Core Skills**: 

    Core skills are foundational skills like math, reasoning, and coding. 
    
    🗒️ **Note:** Unlike **knowledge** and **compositional skills**, core skills are not contributable to the tree. So when you see reference to contributing "skills" to the taxonomy from this point forward, it is **compositional skills** that are being referenced. 

## Knowledge vs. Skills

You can contribute both **knowledge** and **skills** to the Taxonomy. What is the difference? 

### Skills 

Again, think of skills as "performative." You're teaching the model how to **do** something when you contribute a skill. 

Skills require a much smaller volume of content to contribute. A skill contribution to the taxonomy tree can be just a few lines of YAML (named `qna.yaml` file - "qna" is short for "questions and answers").

#### _Skill YAML example:_

```
---
- answer: |
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
```

Seriously, that's it. 

Here is where this yaml sits in the taxonomy tree - note that the yaml file itself, plus any added directories it sits inside, is the entirety of the skill in terms of a taxonomy contribution.

#### _Skill directory tree example:_
```
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

### Knowledge

Meanwhile, knowledge is based more on answering questions that involves facts, data, or references. 

Knowledge in the taxonomy tree also consists of a few more elements than skills. Each knowledge node in the tree has a `qna.yaml` similar to the format of the `qna.yaml` for skills, but it has an extra entry per item, `context:`:

#### _Knowledge YAML example:_
```
---
- context: ts-world-tour-2024-schedule.md
  question: |
    Is Taytay coming to Boston in 2024?
  answer: |
    Not that is known yet. Taylor Swift last performed in the Boston area at the Gilette Stadium in Foxboro, MA for 3 nights from Friday May 19, 2023 to Sunday May 21, 2023. In 2024, she is making international tour stops for her Eras tour outside of the United States. 
- context: ts-discography-2024.md
  question: |
    Which album was released more recently, Reputation or Midnights?
  answer: |
    The Taylor Swift Album Reputation was released on November 10, 2017. Midnights was released October 21, 2022. Midnights was released more recently, but there are rumors that there will be a re-release of Reputation called Reputation (Taylor's version) in the later half of 2024 which would make that the most recently-released album of the set at that time.
- context: ts-discography-2024.md
  question: |
    Which album has the song "You Need to Calm Down?"
  answer: |
    The song "You Need to Calm Down" appears on Taylor Swift's 2019 album Lover as track 14.
```

You can see this knowledge references two markdown files: `ts-world-tour-2024-schedule.md` as well as `ts-discography-2024.md`. These files in their entirety also need to be submitted along with the knowledge's `qna.yaml` file, which means that knowledge files consists of a much higher volume of content than a skill. 

This of course, means **it will naturally take longer to receive acceptance for a knowledge contribution pull request than for a skill pull request** - smaller pull requests are simpler and require less time and effort to review.

What might these markdown files look like? They can be freeform. Here's what a snippet of `ts-discography-2024.md` might look like:

#### _Knowledge freeform example:_
```
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
    11.	"Our Song"

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

In contrast to the layout of skills in the taxonomy, here's what the knowledge referenced above might look like in the tree:

#### _Knowledge directory tree example:_
```
[...]

└── culture
    └── music
    |   └── pop
    |   |    ├── taylor swift <=== here it is :)
    |   |    |    ├── ts-discography-2024.md
    |   |    |    ├── ts-world-tour-2024-schedule.md
    |   |    |    └── qna.yaml  
    │   |    ├── the rolling stones
    |   |    |    ├── rs-discography-2024.md
    |   |    |    ├── rs-guitar-tabs.md
    |   |    |    ├── rs-lyrics-catalog-2024.md
    |   |    |    ├── rs-tour-history.md
    |   |    |    └── qna.yaml  

[...]
```

## Formatting

TBD

## Layout

The taxonomy tree is organized in a cascading directory structure. At the end of each branch, there is a YAML file (qna.yaml) that contains the examples for that domain.

#### _Illustrative directory structure to show this layout:_
```
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


## Ways to Contribute
You can contribute to the taxonomy in the following: 
- Adding new examples to existing leaf nodes: 
    - Go to the corresponding leaf node / end of the branch and modify the yaml 
    - Add new examples to the qna.yaml files as a new entry to the list
- Adding new branches/skills corresponding to an existing domain:
    - You can add new folders under the corresponding category
    - Create a new qna.yaml file with examples for the new skill

For additional information on how to make a contribution, please, consult the [contributing documentation](CONTRIBUTING.md).


### Why should I contribute?

This taxonomy repository will be used as the seed to synthesize the training data for Labrador-trained models.
We intend to re-train the model(s) using the main branch following Labrador's progressive training on a regular basis.
This enables fast iteration of the model(s), for the benefit of the open source community, in particular to enable model developers who do not have access to the necessary compute infrastructure.
