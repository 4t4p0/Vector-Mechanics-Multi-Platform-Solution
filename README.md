# Vector Mechanics Multi-Platform Solution

A small, consistent implementation of the same vector mechanics problem in MATLAB and Python, including computed reactions, plots, and root-finding by the bisection method.

## Objective

Provide a clear, side-by-side reference of the same mechanical model in two languages, ensuring identical calculations, outputs, and plot structure.

## Technologies

- Language: MATLAB, Python
- Libraries: NumPy, Matplotlib

## Applied Concepts

- Rigid body kinematics and dynamics
- Angular velocity and angular acceleration
- Reaction forces at supports
- Numerical root finding (bisection method)

## How It Was Done

The MATLAB script defines the model parameters, computes angular quantities, calculates reactions at points D and E, prints a formatted data table, plots the results, and computes roots for Ey(t) and Ex(t). The Python script mirrors the same structure, formulas, and outputs using NumPy and Matplotlib.

## How To Use It

### MATLAB

1. Open [MATLAB/Code.m](MATLAB/Code.m).
2. Run the script. It prints the data table, finds roots, and opens the plots.

### Python

1. Open [Python/Code.py](Python/Code.py).
2. Install dependencies (if needed): `pip install numpy matplotlib`.
3. Run the script: `python Code.py`.
4. It prints the data table, finds roots, and opens the plots.
