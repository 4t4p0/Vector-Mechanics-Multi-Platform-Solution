# Vector Mechanics Multi-Platform Solution

A comprehensive, multi-platform mechanical engineering analysis of a rotating disk-shaft system with support reactions. Implemented identically in MATLAB and Python, featuring kinematic calculations, reaction force analysis, root-finding algorithms, and detailed visualizations.

<img width="962" height="712" alt="image" src="https://github.com/user-attachments/assets/aebb2b90-cf83-4fee-b2c9-eee8821e786b" />

## Key Features

✓ **Identical dual-language implementation** (MATLAB and Python)  
✓ **Reaction force calculations** at support points D and E  
✓ **Numerical root-finding** using the bisection method  
✓ **Comprehensive visualization** with time-series plots  
✓ **3D mechanical models** in SolidWorks  
✓ **Technical documentation** with detailed analysis  

## Technologies & Libraries

| Component | Technology |
|-----------|-----------|
| **Computational** | MATLAB, Python 3 |
| **Libraries** | NumPy, Matplotlib |
| **CAD Modeling** | SolidWorks 2024 |
| **Documentation** | MS Word, PDF |

## Applied Physics Concepts

- **Rigid body dynamics** and kinematics
- **Angular velocity** and angular acceleration calculations
- **Reaction forces** at statically determinate supports
- **Numerical methods** (bisection algorithm for root-finding)
- **Force and moment equilibrium** analysis

## How To Use It

### MATLAB

1. Open [MATLAB/Code.m](MATLAB/Code.m) in MATLAB
2. Click **Run** or press Ctrl+Enter
3. The script will:
   - Print the reaction forces data table to the console
   - Find and display the three roots (bisection method)
   - Display two interactive plots showing reactions at D and E

### Python

1. Ensure dependencies are installed:
   ```bash
   pip install numpy matplotlib
   ```

2. Run the script from the command line:
   ```bash
   cd Python
   python Code.py
   ```

3. The script will:
   - Print the reaction forces data table to the console
   - Find and display the three roots (bisection method)
   - Display two interactive plots showing reactions at D and E
   - Save plots as PNG images

### SolidWorks

1. Open the assembly: [SolidWorks/Peça_Inteira.SLDASM](SolidWorks/Peça_Inteira.SLDASM)
2. View individual components in [SolidWorks folder](SolidWorks)
3. Use SolidWorks Motion Simulation to verify kinematic behavior
4. Check the [Graphics SolidWorks](SolidWorks/Graphics%20SolidWorks) folder for renderings

### Technical Documentation

Open [Report/Report.pdf](Report/Report.pdf) for the complete technical analysis including:
- Problem statement and physical model
- Mathematical derivation of equilibrium equations
- Detailed results and interpretation
- Graphs and numerical analysis

## Implementation Notes

- **MATLAB** and **Python** implementations use identical formulas and produce numerically equivalent results
- Both scripts use the **bisection method** with tolerance = 1e-16 for precise root locations
- Reaction forces calculated using **moment equilibrium** and **force balance** equations
- Time vector resolution: 0.2 seconds from t = 0 to t = 4 seconds


## License

Educational project for mechanical engineering analysis.
