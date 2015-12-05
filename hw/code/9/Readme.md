#Code 9

#A Simple Standard Genetic Algorithm  

## Abstract:   
We compare the performance results of DTLZ - 1,3,5,7 with various objectives and decisions.

## Introduction:   

### Algorithm:

```
Generate a initial population
Calculate fitness of current population
repeat for i generations
    select parents for next generation
        Perform binary domination on all the possible pairs
        select n number of candidates based on the score
    crossover
        randomly pick mom, dad from parents - mom not equal to dad
        crossover creates 2 children
        repeat until we have same number of candidates as initial population
    mutate
        Introduce random “mutations” in some of the children based on mutation probability
    termination
        compare current objective with previous objectives
         if better
            continue
         else
            reduce lives
         If ran out of lives, terminate 
```

## Experiments:   

## Results: 
 
 Table : Values of Auxiliaries Used 

|Optimizer   | DLTZ1   |  DLTZ3 | DLTZ5  | DLTZ7  |
|------------------------------|-----|-----|-----|-----|
| Standard GA      | 0  | 1 | 1 | 1 | 

## Conclusions 

## Future Work:
   
   
## References: