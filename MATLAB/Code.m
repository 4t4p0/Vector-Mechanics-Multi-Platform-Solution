clear all
close all
clc

%--------------------Data--------------------

d_AB = 0.06;      %(m) Distance from A to B
d_BC = 0.12;      %(m) Distance from B to C
d_CD = 0.15;      %(m) Distance from C to D
d_DE = 0.30;      %(m) Distance from D to E
m = 3.0;          %(kg) Disk mass
r = 0.08;         %(m)
M0 = 1.0;         %(N*m)
omega_1_0 = 90;   %(rad/s)
alpha_1 = -15;    %(rad/s^2) Angular acceleration

%--------------------Angular acceleration--------------------

alpha_2 = M0/(m*(0.25*r^2+d_BC^2+d_AB^2)); %(rad/s^2)

%--------------------Angular acceleration--------------------

t = [0:0.2:4]; %Creates a time vector from 0s to 4s every 0.2s

omega_1 = omega_1_0 + alpha_1*t; %Calculates angular velocity_1 at each t

omega_2 = alpha_2*t; %Calculates angular velocity_2 at each t

%--------------------Calculates reactions at E--------------------

Ex = (m/d_DE)*(-0.5*r^2*alpha_1+d_CD*d_AB*alpha_2-d_CD*d_BC*omega_2.^2); %Reaction at E in the x direction

Ey = (m/d_DE)*(-0.5*r^2*omega_1.*omega_2+d_CD*d_BC*alpha_2+d_CD*d_AB*omega_2.^2); %Reaction at E in the y direction

%--------------------Calculates reactions at D--------------------

Dx = m*(d_AB*alpha_2-d_BC*omega_2.^2)-Ex; %Reaction at D in the x direction

Dy = m*(d_BC*alpha_2+d_AB*omega_2.^2)-Ey; %Reaction at D in the y direction

%--------------------Plots the graphs--------------------

figure(1)
plot(t,Dx,'g',t,Dy,'r')
xlabel('Time(s)')
ylabel('Reactions at D(N)')
legend('Dx','Dy')
grid on

figure(2)
plot(t,Ex,'g',t,Ey,'r')
xlabel('Time(s)')
ylabel('Reactions at E(N)')
legend('Ex','Ey')
grid on

%--------------------Ey(t) Function--------------------

function Ey_val = Ey_t(t)

    d_AB = 0.06;      %(m) Distance from A to B
    d_BC = 0.12;      %(m) Distance from B to C
    d_CD = 0.15;      %(m) Distance from C to D
    d_DE = 0.30;      %(m) Distance from D to E
    m = 3.0;          %(kg) Disk mass
    r = 0.08;         %(m)
    M0 = 1.0;         %(N*m)
    omega_1_0 = 90;   %(rad/s)
    alpha_1 = -15;    %(rad/s^2) Angular acceleration

    alpha_2 = M0/( m*(0.25*r^2 + d_BC^2 + d_AB^2) ); % Calculates angular acceleration_2

    omega_1 = omega_1_0 + alpha_1*t;   % Calculates angular velocity_1
    omega_2 = alpha_2 * t;             % Calculates angular velocity_2

    % Calculates Ey
    Ey_val = (m/d_DE) * ( -0.5*r^2 .* omega_1 .* omega_2 + d_CD*d_BC*alpha_2 + d_CD*d_AB .* (omega_2).^2 );
end

%--------------------Ex(t) Function--------------------

function Ex_val = Ex_t(t)

    d_AB = 0.06;      %(m) Distance from A to B
    d_BC = 0.12;      %(m) Distance from B to C
    d_CD = 0.15;      %(m) Distance from C to D
    d_DE = 0.30;      %(m) Distance from D to E
    m = 3.0;          %(kg) Disk mass
    r = 0.08;         %(m)
    M0 = 1.0;         %(N*m)
    omega_1_0 = 90;   %(rad/s)
    alpha_1 = -15;    %(rad/s^2) Angular acceleration

    alpha_2 = M0/( m*(0.25*r^2 + d_BC^2 + d_AB^2) ); % Calculates angular acceleration_2

    % Calculates Ex
    Ex_val = (m/d_DE) * ( -0.5*r^2 * alpha_1 + d_CD*d_AB*alpha_2 - d_CD*d_BC*(alpha_2*t).^2 );
end

%--------------------Bisection method function--------------------

function raiz = bisseccao(f, a, b, tol, maxIter)

    if f(a) * f(b) > 0
        error('The interval does not contain a sign change.');
    end

    for k = 1:maxIter

        c = (a + b) / 2;

        if abs(f(c)) < tol || (b - a)/2 < tol
            raiz = c;
            return;
        end

        if f(a)*f(c) < 0
            b = c;
        else
            a = c;
        end
    end

    raiz = (a + b)/2;
    fprintf('Best approximation after %d iterations: t = %.8f\n', maxIter, raiz);

end
