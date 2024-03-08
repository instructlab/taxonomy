body { counter-reset: h1counter h2counter h3counter h4counter h5counter h6counter; }

h1 { counter-reset: h2counter; }
h2 { counter-reset: h3counter; }
h3 { counter-reset: h4counter; }
h4 { counter-reset: h5counter; }
h5 { counter-reset: h6counter; }
h6 {}

h2:before {
    counter-increment: h2counter;
    content: counter(h2counter) ".\0000a0\0000a0";
}

h3:before {
    counter-increment: h3counter;
    content: counter(h2counter) "." counter(h3counter) ".\0000a0\0000a0";
}

h4:before {
    counter-increment: h4counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) ".\0000a0\0000a0";
}

h5:before {
    counter-increment: h5counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) "." counter(h5counter) ".\0000a0\0000a0";
}

h6:before {
    counter-increment: h6counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) "." counter(h5counter) "." counter(h6counter) ".\0000a0\0000a0";
}

# Skills Guide



## NOTES

+ indicates a type of skill we should allow
- indicates a type of skill we should reject


+ formatting
- math
+ sorting when it comes to implicit knowledge
+ working with tables, sorting those tables
+ qualitative inference and reasoning
(word problems maybe yes; large numbers no - but for now avoid)
- complex rule systems and game playing (for now)
+ precision at instruction following (e.g. regex)
- red teaming
+ safety, flag for review
+ creative writing
+ more descriptive word problems, chain-of-thought style reasoning
+ searching, extraction and summarization
- real world knowledge as compositional skills - we're not giving the model real world knowledge to 
- shouldn't need to come up with its own facts; assemble facts provided
contributors document needs to be updated to reflect the triage skills doc
+ question needs to articulate the style that they want the model to provide - we want to build general case that can handle that task better
(see buddha question)
saved replies - add specified style in question
saved replies - add more examples
~ akash's take on the palindromes - turing-complete type problems?
+ rhyming / verbal behavior
+ bot-like behavior
- overspecific nitpicking of the original model responses (needs a saved reply, see the palindrome one)
"can the model not do the skill, or is it not following precise instructions about the skill?"
+ precision about response length, number of items in a list, etc
- skill as knowledge
(morse code)
if the q has the morse code alphabet, and then you're assembling facts, that's a skill
replace morse code as a 'grounded skill"
answer needs to use chain-of-thought reasoning
- attempts to make complex technical systems connecting to other systems
clarifying: after tuning step, the context will still be necessary
