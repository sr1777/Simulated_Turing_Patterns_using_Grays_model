# Gray-Scott Model: Simulated Turing Patterns (Spots & Stripes)

## Overview
This Python project implements an interactive simulation of Turing patterns using the **Gray-Scott reaction-diffusion model**. The simulation generates striking spots, stripes, and mixed patterns by numerically solving the coupled partial differential equations (PDEs):

$$
\frac{\partial u}{\partial t} = D_u \nabla^2 u - u v^2 + F(1-u)
$$

$$
\frac{\partial v}{\partial t} = D_v \nabla^2 v + u v^2 - (F+k)v
$$

where:

- $u$ and $v$ are chemical concentrations on a 2D grid  
- $D_u$, $D_v$ are diffusion rates  
- $F$ is the feed rate of chemical $u$  
- $k$ is the kill rate of chemical $v$

The simulation demonstrates the emergence of **self-organized patterns** reminiscent of natural phenomena such as:

- animal coat markings  
- seashell patterns  
- chemical reactions

## Features
- Interactive real-time simulation using **Matplotlib's `FuncAnimation`**  
- Adjustable parameters for **feed rate (F)** and **kill rate (k)** to generate different patterns:  
  - Spots: `F = 0.035`, `k = 0.065`  
  - Stripes: `F = 0.060`, `k = 0.062`  
- Visualization of the sum of $u$ and $v$ concentrations with the **magma** colormap  
- Fast computation using **NumPy array operations** and periodic boundary conditions

## References
- Wael Mahmoud Al Etaiwi, et al., *"Reaction-Diffusion Systems for Pattern Formation."*  
- Alan Turing, *"The Chemical Basis of Morphogenesis,"* 1952.

## License
MIT License © SR
