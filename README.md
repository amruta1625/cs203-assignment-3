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

The simulation is run for all combinations of `n` and `k` in the range [3, 20) and [1, 18), respectively, with a fixed number of samples (`samples`) which is 10000.

## Plotting

The simulation results are plotted as a 3D surface plot using matplotlib's `plot_surface` function. The x-axis represents the number of cars `k`, the y-axis represents the number of doors `n`, and the z-axis represents the ratio of the probability of winning when switching to the probability of winning when staying with the initial decision `(P(win|W)/P(win|T))`.

## Inference

The plot shows that the ratio of the probability of winning when switching to the probability of winning when staying with the initial decision is generally higher when there are more cars and fewer doors, and lower when there are fewer cars and more doors. This is because the probability of winning when switching is higher when there are more cars and fewer doors, and lower when there are fewer cars and more doors. The plot can help us to understand the relationship between these factors and the probability of winning in the Monty Hall problem.

### To run the python file
```
   python3 monty_hall.py

```
