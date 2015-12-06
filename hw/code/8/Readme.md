#Code 8

# Types of "less than" for Optimizers

## I. Abstract:
    

## II. Background:   

### Algorithm:

#### Simulated Annealing
    Simulated annealing (SA) is a method for solving unconstrained and bound-constrained optimization problems. The method models the physical process of heating a material and then slowly lowering the temperature to decrease defects, thus minimizing the system energy.
    <br>
    At each iteration of the simulated annealing algorithm, a new point is randomly generated. The distance of the new point from the current point, or the extent of the search, is based on a probability distribution with a scale proportional to the temperature. The algorithm accepts all new points that lower the objective, but also, with a certain probability, points that raise the objective. By accepting points that raise the objective, the algorithm avoids being trapped in local minima in early iterations and is able to explore globally for better solutions.
#### MaxWalkSat

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

    Compare with the stats methods discussed last week.
    
    Warning:
    
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