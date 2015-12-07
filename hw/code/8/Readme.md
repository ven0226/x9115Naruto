#Code 8

# Implementing Types of "less than" for Optimizers

## I. Abstract:
    

## II. Background:   

### Algorithm:

#### Simulated Annealing
Simulated annealing (SA) is a method for solving unconstrained and bound-constrained optimization problems. The method models the physical process of heating a material and then slowly lowering the temperature to decrease defects, thus minimizing the system energy.<br>
* A baseline study is generated
* At each iteration of the simulated annealing algorithm, a new candidate is randomly generated. 
* Type 1 comparison is performed between the best solution and new candidate 
    * If the new candidate is better update best solution
* Type 1 comparison is performed between the new candidate and local solution
    * If the new candidate is better update local solution
* After the era size
    * Type2 comparison between era and era - 1
* Exit 
    * if ran out of lives
    * if optimum energy is reached
    * if ran out of generations

#### MaxWalkSat

MaxWalkSat is a non-parametric stochastic method for sampling the landscape of the local region. Historically speaking, MaxWalkSat was a very impactful algorithm. But, at least here, the real purpose of discussing MaxWalkSat is to introduce the idea of landscapes. It will be argued that more important than the algorithms is the shape of the space they search. Since this shape can change, it is not possible to prove the adequacy of these meta-heuristics unless you first characterize the space they are trying to explore.

#### Differential Evolution

### Comparison

#### Type1
    + Two candidates _X,Y_
    + Objectives _1,2,..i,..n_.
    + A predicate _better(i,Xi,Yi)_;
         + i.e. for objective "_i_" is _Xi_ from _X_ better than _Yi_ from _Y_?
         + e.g. when minimizing all goals,
              + _better(any,Xi,Yi) =  Xi &lt; Yi_.
#### Type2
    + For each objective do
        + If any "improvement", give yourself five more lives
             + Here, "improvement" could be
                  + Sort the values for that objective in _era_ and _era+1_
                  + Run the fast _a12_ test to check for true difference
                  + Be mindful of objectives minimizing or maximizing.
    + If no improvement on anything,
         + Lives - 1
#### Type3
    + When comparing N optimizers for R repeats....\
        + For each repeat, generate one new baseline, then...
             + Run each optimizer for each repeat.

## III. Experiments: 

    Model : DLTZ7
    Decisions : 10
    Objectives : 2
    
    
    Optimizers:
     
     #### Simulated Annealing 
     
     ```
     Candidates : 
     Threshold : 
     Type : Minimizing
     Era Size : 50 
     ```
     
     #### MaxWalkSat
     
     ```
     ```
     
     #### Differential Evolution
     
     ```
     ```
    
    Table : settings for optimizers 

|Optimizer   | Candidates   | Iterations | Threshold | 
|------------------------------|-----|-------|
| Simulated Annealing    | 2.968  | 1000
| MaxWalkSat    | 2.968  | 18.156 | 2500
| Differential Evolution    | 2.968  | 2000 |
    

## IV Results: 

![statistical results](./imgs/rdiv.png)

## V Conclusions:

## Future Work:
   
   
## References:
