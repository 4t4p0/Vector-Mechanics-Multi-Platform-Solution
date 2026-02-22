import numpy as np
import matplotlib.pyplot as plt

# -------------------- Data --------------------

d_AB = 0.06         # (m) Distance from A to B
d_BC = 0.12         # (m) Distance from B to C
d_CD = 0.15         # (m) Distance from C to D
d_DE = 0.30         # (m) Distance from D to E
m = 3.0             # (kg) Disk mass
r = 0.08            # (m)
M0 = 1.0            # (N*m)
omega_1_0 = 90      # (rad/s)
alpha_1 = -15       # (rad/s^2) Angular acceleration

# -------------------- Angular acceleration --------------------

alpha_2 = M0 / (m * (0.25 * r**2 + d_BC**2 + d_AB**2))  # (rad/s^2)

# -------------------- Time vector --------------------

t = np.arange(0, 4.2, 0.2)  # Creates a time vector from 0s to 4s every 0.2s

# -------------------- Angular velocities --------------------

omega_1 = omega_1_0 + alpha_1 * t  # Calculates angular velocity_1 at each t

omega_2 = alpha_2 * t  # Calculates angular velocity_2 at each t

# -------------------- Calculates reactions at E --------------------

Ex = (m / d_DE) * (-0.5 * r**2 * alpha_1 + d_CD * d_AB * alpha_2 - d_CD * d_BC * omega_2**2)  # Reaction at E in the x direction

Ey = (m / d_DE) * (-0.5 * r**2 * omega_1 * omega_2 + d_CD * d_BC * alpha_2 + d_CD * d_AB * omega_2**2)  # Reaction at E in the y direction

# -------------------- Calculates reactions at D --------------------

Dx = m * (d_AB * alpha_2 - d_BC * omega_2**2) - Ex  # Reaction at D in the x direction

Dy = m * (d_BC * alpha_2 + d_AB * omega_2**2) - Ey  # Reaction at D in the y direction

# -------------------- Plots the graphs --------------------

plt.figure(1)
plt.plot(t, Dx, 'g', label='Dx')
plt.plot(t, Dy, 'r', label='Dy')
plt.xlabel('Time(s)')
plt.ylabel('Reactions at D(N)')
plt.legend()
plt.grid(True)

plt.figure(2)
plt.plot(t, Ex, 'g', label='Ex')
plt.plot(t, Ey, 'r', label='Ey')
plt.xlabel('Time(s)')
plt.ylabel('Reactions at E(N)')
plt.legend()
plt.grid(True)

# -------------------- Ey(t) Function --------------------

def Ey_t(t_val):
    """Calculate Ey as a function of time"""
    d_AB = 0.06         # (m) Distance from A to B
    d_BC = 0.12         # (m) Distance from B to C
    d_CD = 0.15         # (m) Distance from C to D
    d_DE = 0.30         # (m) Distance from D to E
    m = 3.0             # (kg) Disk mass
    r = 0.08            # (m)
    M0 = 1.0            # (N*m)
    omega_1_0 = 90      # (rad/s)
    alpha_1 = -15       # (rad/s^2) Angular acceleration

    alpha_2 = M0 / (m * (0.25 * r**2 + d_BC**2 + d_AB**2))  # Calculates angular acceleration_2

    omega_1 = omega_1_0 + alpha_1 * t_val   # Calculates angular velocity_1
    omega_2 = alpha_2 * t_val                # Calculates angular velocity_2

    # Calculates Ey
    Ey_val = (m / d_DE) * (-0.5 * r**2 * omega_1 * omega_2 + d_CD * d_BC * alpha_2 + d_CD * d_AB * omega_2**2)
    return Ey_val

# -------------------- Ex(t) Function --------------------

def Ex_t(t_val):
    """Calculate Ex as a function of time"""
    d_AB = 0.06         # (m) Distance from A to B
    d_BC = 0.12         # (m) Distance from B to C
    d_CD = 0.15         # (m) Distance from C to D
    d_DE = 0.30         # (m) Distance from D to E
    m = 3.0             # (kg) Disk mass
    r = 0.08            # (m)
    M0 = 1.0            # (N*m)
    omega_1_0 = 90      # (rad/s)
    alpha_1 = -15       # (rad/s^2) Angular acceleration

    alpha_2 = M0 / (m * (0.25 * r**2 + d_BC**2 + d_AB**2))  # Calculates angular acceleration_2

    # Calculates Ex
    Ex_val = (m / d_DE) * (-0.5 * r**2 * alpha_1 + d_CD * d_AB * alpha_2 - d_CD * d_BC * (alpha_2 * t_val)**2)
    return Ex_val

# -------------------- Bisection method function --------------------

def bisseccao(f, a, b, tol, maxIter):
    """
    Bisection method to find the root of a function
    
    Parameters:
    f       - Function to find root
    a, b    - Interval [a, b]
    tol     - Tolerance
    maxIter - Maximum number of iterations
    """
    
    if f(a) * f(b) > 0:
        raise ValueError('The interval does not contain a sign change.')
    
    for k in range(maxIter):
        c = (a + b) / 2
        
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    raiz = (a + b) / 2
    print(f'Best approximation after {maxIter} iterations: t = {raiz:.8f}')
    return raiz

if __name__ == "__main__":
    print("Vector Mechanics Multi-Platform Solution")
    print("All calculations completed!")
    plt.show()
