#Code 10

# Hyper parameter optimization

## Abstract:   

## Introduction:   

### Algorithm:


* SettingModel
  * lo = [50,100,0.01]
  * hi = [150,1000,0.15]
  * Decisions - 3
    * Candidates, Generations, Mutate Probability
  * Objectives - 1
    * Hypervolume of the GA
    
* Create a frontier of randomly chosen settings
* Run DE on each setting as a candidate 
  * the energy score of each candidate will be the hypervolume from GA. 
  * GA runs with the settings from DE using the Kursawe model
  * Exit
    * When there is no improvement in the era from the previous era
    * maximum tries reached

## Experiments:   

## Results: 
 
## Conclusions 

## Future Work:
   
## References:
