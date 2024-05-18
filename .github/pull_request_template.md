If your PR is related to a contribution to the taxonomy, please, fill
out the following questionnaire. If not, replace this whole text and the
following questionnaire with whatever information is applicable to your PR.


**Describe the contribution to the taxonomy**

<!-- A concise description of what the contribution brings, replace "..." in the bullet list -->

- ...
- ...
- ...


**Input given at the prompt**

<!-- What you entered, replace "..." -->

```
   ...
```


**Response from the original model**


<!-- What you received from the original model in response to your input, 
replace "..." -->

```
  ...
```


**Response from the fine-tuned model**


<!-- Generate a synthetic dataset based on your newly added seed data; train the model 
with the synthetic data and now re-test the model's response with the same prompt.
Replace "..." with what you receive with the finetuned model. -->

```
  ...
```

**Contribution checklist**

<!-- Insert an x between the empty brackets: [ ] >> [x] -->

- [ ] The contribution was tested with `ilab generate`
- [ ] No errors or warnings were produced by `ilab generate`
- [ ] All [commits are signed off](https://github.com/instructlab/taxonomy/blob/main/CONTRIBUTING.md#legal) (DCO)
- [ ] The `qna.yaml` file contains at least 5 `seed_examples`
- [ ] The `qna.yaml` file was [linted](https://yamllint.com) and [prettified](https://onlineyamltools.com/prettify-yaml) ([yaml-validator](https://jsonformatter.org/yaml-validator) can do both)
- [ ] An `attribution.txt` file in the same folder as the `qna.yaml` file
- [ ] Content does not include PII or otherwise sensitive or confidential information
- [ ] Content does not include anything documented in the project's [Avoid these Topics](https://github.com/instructlab/taxonomy/blob/main/docs/SKILLS_GUIDE.md#avoid-these-topics) guidelines
