# Monty Hall Problem Simulation

This project simulates the Monty Hall Problem for a generalized number of doors and cars. The simulation assesses the probability of winning for switching (W) versus sticking (T) to the original decision. A surface plot of n, k versus (P(win|W)/P(win|T)) is also generated.

## Dependencies

* Python 3.x
* NumPy
* Matplotlib

## Usage

To run the simulation and generate the surface plot, simply run the script. The plot will be displayed in a new window.

## Simulation

The simulation is implemented in the `simulate` function, which takes in the number of doors `n`, the number of cars `k`, and the number of samples `samples`. The function simulates the Monty Hall Problem for the given parameters and returns the number of wins when switching (`switched_choice_wins`) and the number of wins when staying with the initial choice (`same_choice_wins`).

The simulation is run for all combinations of `n` and `k` in the range [3, 20) and [1, 18), respectively, with a fixed number of samples (`samples`).

## Plotting

The simulation results are plotted as a 3D surface plot using matplotlib's `plot_surface` function. The x-axis represents the number of cars `k`, the y-axis represents the number of doors `n`, and the z-axis represents the ratio of the probability of winning when switching to the probability of winning when staying with the initial decision `(P(win|W)/P(win|T))`.

## Interpreting the Results:

* Users can observe how the probability ratio (P(win|W) / P(win|T)) changes with different values of n and k.
* From this plot, we can infer the conditions under which switching is more advantageous than sticking, and vice versa.
* The probability of winning when switching is always higher than the probability of winning when sticking. This is because switching takes advantage of the host's revelation, which provides additional information that can be used to make a more informed decision.
* Mathematically, the probability of winning under no switch is k/n and under switch is k(n-1)/n(n-2). So the ratio P(win|W)/P(win|T) is (n-1)/(n-2) which is independent of k. This result can also be seen in the plots where the variation with k is almost negligible and for variation with n, as n takes up large values the ratio tends to 1.

Note:

* Users can modify parameters such as the number of doors, the number of doors with cars, and the number of samples to analyze different scenarios. By editing the values of n, k in the code.

  
### To run the python file
```
   python3 monty_hall.py

```
