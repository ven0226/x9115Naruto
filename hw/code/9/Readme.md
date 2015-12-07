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
        compare current era mean objectives with previous era objectives
         if better
            continue
         else
            reduce lives
         If ran out of lives, terminate 
```

## Experiments:  

### Models:

#### Setup

 * Standard GA on 4 different models: DTLZ 1,3,5,7
 * with decision numbers 10, 20, 40
 * and objective numbers 2, 4, 6, 8
 * repeat 4 times for each
 * mutation rate: 0.05
 * crossover: one point
 * number of candidates: 100
 * number of maximum generations: 1000 (with early termination)
 * early termination: life = 10, each new generation, if not better, life=life-1; else do nothing. Terminate when life = 0.


## Results: 
 
Table : DTLZ1 Hypervolume

|Objectives\Models   | 10   |  20 | 40  | 
|------------------------------|-----|-----|-----|
|  2  | 2.968  | 18.156 | 95.070 |
|  4  | 2.968  | 18.156 | 95.070 |
|  6  | 2.968  | 18.156 | 95.070 |
|  8  | 2.968  | 18.156 | 95.070 |

Table : DTLZ3 Hypervolume

|Objectives\Models   | 10   |  20 | 40  | 
|------------------------------|-----|-----|-----|
|  2  | 2.968  | 18.156 | 95.070 |
|  4  | 2.968  | 18.156 | 95.070 |
|  6  | 2.968  | 18.156 | 95.070 |
|  8  | 2.968  | 18.156 | 95.070 |

Table : DTLZ5 Hypervolume

|Objectives\Models   | 10   |  20 | 40  | 
|------------------------------|-----|-----|-----|
|  2  | 2.968  | 18.156 | 95.070 |
|  4  | 2.968  | 18.156 | 95.070 |
|  6  | 2.968  | 18.156 | 95.070 |
|  8  | 2.968  | 18.156 | 95.070 |

Table : DTLZ7 Hypervolume

|Objectives\Models   | 10   |  20 | 40  | 
|------------------------------|-----|-----|-----|
|  2  | 1.0  | 1.0 | 1.0 |
|  4  | 7.51339e-01  | 1.0 | 1.0 |
|  6  | 6.89056e-01   | 9.00321e-01  | 1.0 |
|  8  | 7.45424e-01  | 8.81647e-01 | 1.0 |


## Threat to Validity


## Conclusions 

## Future Work:
   
   
## References:
