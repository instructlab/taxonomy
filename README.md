# LAB Taxonomy
The LAB approach is driven by taxonomies, which are largely created manually with care.

Top-level categories are
1. Knowledge
2. Core Skills
3. Compositional Skills

## Layout

The taxonomy tree is organized in a cascading directory structure. At the end of each branch, there is a YAML file (qna.yaml) that contains the examples for that domain.
Below is an illustrative directory structure to show this layout.
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
You can contribute your to the taxonomy in the following: 
- Adding new examples to existing leaf nodes: 
    - Go to the corresponding leaf node / end of the branch and modify the yaml 
    - Add new examples to the qna.yaml files as a new entry to the list
- Adding new branches/skills corresponding to the existing domain:
    - You can add new folders under the corresponding category
    - Create a new qna.yaml file with examples for the new skill




### Why should I contribute?

This taxnomy repository will be used as the seed to synthesize the training data for Labrador.
We will re-train the model using the main branch following Labrador's progressive trianing in a bi-weekly basis.
This is similar to the rolling-release model that Arch Linux uses.
This enables fast iteration of the model and the entire community would benefit from it.
