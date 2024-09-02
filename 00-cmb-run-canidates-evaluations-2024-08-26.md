# Community Model Build Eval Summary

## Candidate Models

 - `/home/ec2-user/phased_tmp/phase2/checkpoints/hf_format/samples_3242112` A.K.A. 9-EPOCH (leading candidate w.r.t. eval metrics)
 - `/home/ec2-user/phased_tmp/phase2/checkpoints/hf_format/samples_2881920` A.K.A. 8-EPOCH
 - `/home/ec2-user/phased_tmp/phase2/checkpoints/hf_format/samples_3602304` A.K.A. 10-EPOCH
- `/home/ec2-user/phased_tmp/phase2/checkpoints/hf_format/samples_2521728` A.K.A. 7-EPOCH

NOTE: Relative data-specific comparisons are made against a baseline from the current model pipeline, not the older available `instructlab/granite-7b-lab`, in order to determine the impact of the contribution. This baseline already reasonably outperforms `instructlab/granite-7b-lab`.

## 9-EPOCH Result Scores

### General Knowledge (MMLU)

```
0.52 (across 57)
```

### General Skills (MTBench)

```
### AVERAGE:
7.23 (across 158)

### TURN ONE:
7.48

### TURN TWO:
6.97

### ERROR RATE:
0.01
```

### Data-Specific Knowledge Gain/Loss (MMLU-Branch)

```
### AVERAGE:
+0.05 (across 3)

### IMPROVEMENTS:
1. knowledge_history_public_transportation_boston (+0.05)
2. knowledge_science_animals_birds_black_capped_chickadee (+0.05)
3. knowledge_science_astronomy_constellations_phoenix (+0.04)
```

### Data-Specific Skills Gain/Loss (MTBench-Branch)

```
### IMPROVEMENTS:
compositional_skills/linguistics/ambiguity_detection/qna.yaml (+0.86)
compositional_skills/writing/grounded/editing/content/qna.yaml (+0.28)
compositional_skills/general/synonyms/qna.yaml (+0.36)

### REGRESSIONS:
compositional_skills/grounded/linguistics/inclusion/qna.yaml (-0.03)
```


## 8-EPOCH Result Scores

### General Knowledge (MMLU)

```
0.53 (across 57)
```

### General Skills (MTBench)

```
### AVERAGE:
7.19 (across 159)

### TURN ONE:
7.41

### TURN TWO:
6.96

### ERROR RATE:
0.01
```

### Data-Specific Knowledge Gain/Loss (MMLU-Branch)

```
### AVERAGE:
+0.04 (across 3)

### IMPROVEMENTS:
1. knowledge_science_animals_birds_black_capped_chickadee (+0.06)
2. knowledge_history_public_transportation_boston (+0.04)
3. knowledge_science_astronomy_constellations_phoenix (+0.02)
```

### Data-Specific Skills Gain/Loss (MTBench-Branch)

```
### IMPROVEMENTS:
1. compositional_skills/linguistics/ambiguity_detection/qna.yaml (+1.52)
2. compositional_skills/writing/grounded/editing/content/qna.yaml (+0.28)

### REGRESSIONS:
1. compositional_skills/grounded/linguistics/inclusion/qna.yaml (-0.37)
2. compositional_skills/general/synonyms/qna.yaml (-0.2)
```

## 10-EPOCH Result Scores

### General Knowledge (MMLU)

```
0.52 (across 57)
```

### General Skills (MTBench)

```
### AVERAGE:
7.07 (across 159)

### TURN ONE:
7.27

### TURN TWO:
6.88

### ERROR RATE:
0.01
```

### Data-Specific Knowledge Gain/Loss (MMLU-Branch)

```
### AVERAGE:
+0.04 (across 3)

### IMPROVEMENTS:
1. knowledge_science_animals_birds_black_capped_chickadee (+0.06)
2. knowledge_science_astronomy_constellations_phoenix (+0.06)
3. knowledge_history_public_transportation_boston (+0.03)
```

### Data-Specific Skills Gain/Loss (MTBench-Branch)

```
### IMPROVEMENTS:
1. compositional_skills/writing/grounded/editing/content/qna.yaml (+0.28)

### REGRESSIONS:
1. compositional_skills/linguistics/ambiguity_detection/qna.yaml (-0.92)
2. compositional_skills/general/synonyms/qna.yaml (-2.37)
3. compositional_skills/grounded/linguistics/inclusion/qna.yaml (-0.13)
```


## 7-EPOCH Result Scores

### General Knowledge (MMLU)

```
0.53 (across 57)
```

### General Skills (MTBench)

```
### AVERAGE:
6.99 (across 160)

### TURN ONE:
7.11

### TURN TWO:
6.86
```

### Data-Specific Knowledge Gain/Loss (MMLU-Branch)

```
### AVERAGE:
+0.06 (across 3)

### IMPROVEMENTS:
1. knowledge_science_animals_birds_black_capped_chickadee (+0.08)
2. knowledge_history_public_transportation_boston (+0.06)
3. knowledge_science_astronomy_constellations_phoenix (+0.06)
```

### Data-Specific Skills Gain/Loss (MTBench-Branch)

```
### IMPROVEMENTS:
1. compositional_skills/writing/grounded/editing/content/qna.yaml (+0.47)

### REGRESSIONS:
1. compositional_skills/general/synonyms/qna.yaml (-0.5)
2. compositional_skills/linguistics/ambiguity_detection/qna.yaml (-0.73)
3. compositional_skills/grounded/linguistics/inclusion/qna.yaml (-0.2)
```
