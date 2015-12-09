#Code 9

#A Simple Standard Genetic Algorithm  

## Abstract:   
Genetic algorithm is a search heuristic that mimics the process of natural selection. It is routinely used to generate useful solutions to optimization and search problems. We compare the performance results of DTLZ1, DTLZ3, DTLZ5 and DTLZ7 using Genetic algorithms with various objectives and decisions.

## Introduction:   

A genetic algorithm is a method for solving both constrained and unconstrained optimization problems based on a natural selection process that mimics biological evolution. The algorithm repeatedly modifies a population of individual solutions. At each step, the genetic algorithm randomly selects individuals from the current population and uses them as parents to produce the children for the next generation. Over successive generations, the population "evolves" toward an optimal solution.

We can apply the genetic algorithm to solve problems that are not well suited for standard optimization algorithms, including problems in which the objective function is discontinuous, nondifferentiable, stochastic, or highly nonlinear.

The genetic algorithm differs from a classical, derivative-based, optimization algorithm in the following two main ways:

* Generates a population of points at each iteration.
* Selects the next population by computation which uses random number generators.

### Algorithm of GA:

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
## Implementation:  

The algorithm was  Setup with the following parameters:

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

The results show the hyper volume values of frontiers for all the models under study:
 
Table : DTLZ1 Hypervolume

|Objectives\Models   | 10   |  20 | 40  | 
|------------------------------|-----|-----|-----|
|  2  | 3.32747979431e+35  | 5.066437015e+35 | 6.31051754292e+35 |
|  4  | 5.9473185912e+62  | 1.61090550056e+62 | 4.98178346614e+64 |
|  6  | 1.34548356172e+89 | 2.32531305276e+89 | 7.57224185459e+91 |
|  8  | 4.60962750992e+124  | 1.13532321382e+126 | 4.08813412286e+132 |

Table : DTLZ3 Hypervolume

|Objectives\Models   | 10   |  20 | 40  | 
|------------------------------|-----|-----|-----|
|  2  | 3.93658108795e+12  | 4.28212251058e+12 | 4.77400970862e+12 |
|  4  | 1.08833310333e+25  | 9.50709249305e+24 | 1.2789013551e+25 |
|  6  | 3.45763792745e+37  | 6.17502611927e+37 | 8.36349534507e+37 |
|  8  | 5.29513948693e+49  | 7.19018712524e+49 | 7.25556553431e+49 |

Table : DTLZ5 Hypervolume

|Objectives\Models   | 10   |  20 | 40  | 
|------------------------------|-----|-----|-----|
|  2  | 31999.0623  | 33026.807 | 35526.6548 |
|  4  | 599304440.293  | 676918605.61 | 681917881.975 |
|  6  | 1.06210869455e+13 | 9.46689239941e+12 | 1.04952844616e+13 |
|  8  | 1.38853289205e+17 | 1.60219027742e+17 | 1.55291235957e+17 |

Table : DTLZ7 Hypervolume

|Objectives\Models   | 10   |  20 | 40  | 
|------------------------------|-----|-----|-----|
|  2  | 26.0801 | 29.5332 | 33.0061 |
|  4  | 55.4165  | 98.0283 | 120.3165 |
|  6  | 368.4891   | 782.3625 | 765.8458 |
|  8  | 1336.2828  | 3268.3843 | 3930.9786 |


## Threat to Validity
* Not enough repeats to test stability
* No additional lives given if the objectives are better
* Consideration of metrics other than Hyper volume could lead to different results

## Future Work:
* Try other domination techniques other than binary domination
* Improve the default parameters used for the GA
* Try with different values of mutation and cross over
   
## Appendix:

Detailed results are available [here](./Data)
