## PyUncertaintyCalculator
Simple program to calculate uncertainty propagation, written in Python 3 with SymPy.

Calculates via the general equation:

![alt text](https://github.com/igullickson/PyUncertaintyCalc/blob/master/images/general_formula.png?raw=true "General formula")

## Example Runs
Input:

Equation, value and uncertainty for each variable.

Output:

Result of subsitution and the propogated uncertainty.

Screenshots:

![alt text](https://github.com/igullickson/PyUncertaintyCalc/blob/master/images/division.PNG?raw=true "Example using division")

![alt text](https://github.com/igullickson/PyUncertaintyCalc/blob/master/images/polynomial.PNG?raw=true "Example using a polynomial")

## Motivation

Automate uncertainty propogation calculations for college physics lab reports and practice using Python/tkinter/SymPy.

## How to Use
Install [Python3](https://www.python.org/downloads/).

Download PyUncertaintyCalc.zip and extract.

Double click main.pyw to run.

Input equation can include the following special functions: ln (natural log), sin, cos, tan, sec, csc, cot, acos, asin, atan, asec, ascs, and acot. E.g. 0.5t * sin(t-2)

For each variable, enter the value and the uncertainty in the same textbox separated by a space (see screenshots of example runs).
