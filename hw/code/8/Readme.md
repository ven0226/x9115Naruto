#Code 8

# Implementing Types of "less than" for Optimizers

## I. Abstract:
    
Algorithms like Simulated Annealing, MaxWalkSat and Differential Evolution help us in finding the most optimal solution  in an efficient manner. Conventional methods arrive at optimal solution by compairng all the possible candidate solutions, which grow exponentially with the size of the data.This work presents a comparison of the performace of the three optimizers Simulated Annealing, MaxWalkSat and Differential Evolution. The model used for the project was DTLZ7. To evaluate the performance of the optimizers against one another, statistical machinery like Scott-Knott, a12, bootstrap were used.

## II. Background:   

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

Differential evolution optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. It makes few or no assumptions about the problem being optimized and can search very large spaces of candidate solutions. However, metaheuristics such as DE do not guarantee an optimal solution is ever found.

DE is used for multidimensional real-valued functions but does not use the gradient of the problem being optimized, which means DE does not require for the optimization problem to be differentiable as is required by classic optimization methods such as gradient descent and quasi-newton methods. DE can therefore also be used on optimization problems that are not even continuous, are noisy, change over time, etc.

DE optimizes a problem by maintaining a population of candidate solutions and creating new candidate solutions by combining existing ones according to its simple formulae, and then keeping whichever candidate solution has the best score or fitness on the optimization problem at hand. In this way the optimization problem is treated as a black box that merely provides a measure of quality given a candidate solution and the gradient is therefore not needed.

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

## III. Implementation: 

  

## IV Results: 

The results below show the best solutions obtained using the three optimizers along with their scores.

![de](./imgs/de20.PNG)

![mws](./imgs/mws20.PNG)

![sa](./imgs/sa20.PNG)

The entire set of results can be found in result.txt

After all the iterations are completed, the optimizers are ranked according to their performance. The median and inter quartile range for each optimizer are shown:

![statistical results](./imgs/rdiv.png)

We observe that MaxWalkSat performs better than the other optimizers.


## Threats to validity:

The ranking of optimizers might change if models other than DTLZ7 are used. The number of iterations used might also affect the raking of the optimizers. The current results man not hold for some cases  where certain optimizers perform better.


## Future Work:

The experiment is currently run on only one model DTLZ7. Running it on other models would give clearer insights into the perofrmance of these optimizers. Comparison techniques other than binary domination can be used to compare models. Improving the efficiency of type 1, type 2 and type 3 comparisons.
