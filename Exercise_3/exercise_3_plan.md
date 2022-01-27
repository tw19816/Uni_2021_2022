# Exercise 3 Plan
## What needs to be done?
* Solve the 1-D diffusion equation in 1D
    * poker initially at equilibrium at 20C
    * At t=0 one end is thrust into a furnace at 1000C and the other end is thrust into an ice bath at 0C.
        * corresponds to one end at 0C and the other end at 1000C
    * Determine how the energy evolves over time
## What is required for a complete solution?
* An 2D array containing to X and time axes
    * Thus one can determine how X evolves in time
    * *might be a idea to enclose this is a data-class