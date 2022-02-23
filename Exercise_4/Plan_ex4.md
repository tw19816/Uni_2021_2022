# Plan for Exercise 4
Simulation for the decay of a particle

## To do
### Particle beam generation
**Requirements:**
* Want to simulate the production of a (non-relativistic) particle beam
* Each particle in the beam:
    * velocity from a normal distribution w. specified mean and std. dev.
    * lifetime from an exponential distribution w. specified lifetime

**Solutions:**
* Compute the transformation function analytically

### Particle decay (daughter particle creation)
**Requirements:**
* Create daughter particle which is isotropic in space
    * determine direction vector from unit sphere with uniform probability derivative of solid angle

### Propagation to tracking stations
**Requirements:**
* create a particle track outwards from the decay vertex in the lab frame
    * want a function for a straight line from vertex in lab frame

### Hit smearing
**Requirements:**
* Smearing particle position, i.e. add an offset
    * offset given by normal distribution w. specified mean and std. dev.

### Track reconstruction
**Requirements:**
* Reconstruct the track in space (we do not worry about time)
    * solve an implicit matrix equation for an unchanging matrix

**Solutions:**
* Use LU substitution if a more efficient way is found to solve the permutation matrix equation
    * Use matrix inversion otherwise
### Vertex reconstruction
**Requirements:**
* use smeared tracks to determine where the original vertex was located
    * fid efficient way of determining this using the given formula (make use of vectorisation)


## Questions to answer:
* How many samples does one need?