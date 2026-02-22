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
alpha_1 = -15       # (rad/s^2) Angular acceleration at

# -------------------- Angular acceleration --------------------

alpha_2 = M0 / (m * (0.25 * r**2 + d_BC**2 + d_AB**2))  # (rad/s^2)

# -------------------- Angular acceleration --------------------

t = np.arange(0.0, 4.0 + 1e-12, 0.2)  # Creates a time vector from 0s to 4s every 0.2s

omega_1 = omega_1_0 + alpha_1 * t  # Computes angular velocity_1 at each t

omega_2 = alpha_2 * t  # Computes angular velocity_2 at each t

# -------------------- Computes reactions at E --------------------

Ex = (m / d_DE) * (-0.5 * r**2 * alpha_1 + d_CD * d_AB * alpha_2 - d_CD * d_BC * omega_2**2)  # Reaction at E in x direction

Ey = (m / d_DE) * (-0.5 * r**2 * omega_1 * omega_2 + d_CD * d_BC * alpha_2 + d_CD * d_AB * omega_2**2)  # Reaction at E in y direction

# -------------------- Computes reactions at D --------------------

Dx = m * (d_AB * alpha_2 - d_BC * omega_2**2) - Ex  # Reaction at D in x direction

Dy = m * (d_BC * alpha_2 + d_AB * omega_2**2) - Ey  # Reaction at D in y direction

# -------------------- Writes the data --------------------

vetor = np.vstack((t, Dx, Dy, Ex, Ey))
print('Time (s), Dx (N), Dy (N), Ex (N), Ey (N)')
print()
for col in vetor.T:
    print(f'{col[0]:8.5f}  {col[1]:8.5f}  {col[2]:8.5f}  {col[3]:8.5f}  {col[4]:8.5f}')
print()

# -------------------- Plots the graphs --------------------

plt.figure(1)
plt.plot(t, Dx, 'g', label='Dx')
plt.plot(t, Dy, 'r', label='Dy')
plt.xlabel('Tempo(s)')
plt.ylabel('Reacoes em D(N)')
plt.legend()
plt.grid(True)

plt.figure(2)
plt.plot(t, Ex, 'g', label='Ex')
plt.plot(t, Ey, 'r', label='Ey')
plt.xlabel('Tempo(s)')
plt.ylabel('Reacoes em E(N)')
plt.legend()
plt.grid(True)

# -------------------- Ey(t) function --------------------

def Ey_t(t_val):
    d_AB = 0.06         # (m) Distance from A to B
    d_BC = 0.12         # (m) Distance from B to C
    d_CD = 0.15         # (m) Distance from C to D
    d_DE = 0.30         # (m) Distance from D to E
    m = 3.0             # (kg) Disk mass
    r = 0.08            # (m)
    M0 = 1.0            # (N*m)
    omega_1_0 = 90      # (rad/s)
    alpha_1 = -15       # (rad/s^2) Angular acceleration at

    alpha_2 = M0 / (m * (0.25 * r**2 + d_BC**2 + d_AB**2))  # Computes angular acceleration_2

    omega_1 = omega_1_0 + alpha_1 * t_val   # Computes angular velocity_1
    omega_2 = alpha_2 * t_val               # Computes angular velocity_2

    # Computes Ey
    Ey_val = (m / d_DE) * (-0.5 * r**2 * omega_1 * omega_2 + d_CD * d_BC * alpha_2 + d_CD * d_AB * omega_2**2)
    return Ey_val

# -------------------- Ex(t) function --------------------

def Ex_t(t_val):
    d_AB = 0.06         # (m) Distance from A to B
    d_BC = 0.12         # (m) Distance from B to C
    d_CD = 0.15         # (m) Distance from C to D
    d_DE = 0.30         # (m) Distance from D to E
    m = 3.0             # (kg) Disk mass
    r = 0.08            # (m)
    M0 = 1.0            # (N*m)
    omega_1_0 = 90      # (rad/s)
    alpha_1 = -15       # (rad/s^2) Angular acceleration at

    alpha_2 = M0 / (m * (0.25 * r**2 + d_BC**2 + d_AB**2))  # Computes angular acceleration_2

    # Computes Ex
    Ex_val = (m / d_DE) * (-0.5 * r**2 * alpha_1 + d_CD * d_AB * alpha_2 - d_CD * d_BC * (alpha_2 * t_val)**2)
    return Ex_val

# -------------------- Bisection method function --------------------

def bisseccao(f, a, b, tol, maxIter):
    if f(a) * f(b) > 0:
        raise ValueError('The interval does not contain a sign change.')

    for _ in range(maxIter):
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

# -------------------- Prints each root of the equation --------------------

raiz_Ey = bisseccao(Ey_t, 0, 0.5, 1e-16, 100)
print(f'First root of Ey t = {raiz_Ey:.8f}s')

raiz_Ey = bisseccao(Ey_t, 0.5, 4, 1e-16, 100)
print(f'Second root of Ey t = {raiz_Ey:.8f}s')

raiz_Ex = bisseccao(Ex_t, 0, 4, 1e-16, 100)
print(f'First root of Ex t = {raiz_Ex:.8f}s')

if __name__ == "__main__":
    plt.show()
