Energy Diagram Plotting Script:

This Python script, plot_energy_diagram.py,  creates a visual energy diagram  from ground state (GS) and transition state (TS) energies provided in a CSV file. It also allows you to optionally include an existing energy plot PDF in the output.

Usage:

- This script uses matplotlib for plotting.
- The script requires a input data file
- The script currently assumes the first column in your CSV file contains state labels and the following columns contain GS and TS energies You can modify the script to match the format of your data file.
- You can choose bettwen a exponential and gaussian spline to connect the transition states to the ground states. 
- It will generate a energy diagram plot with a user specifed name.
- Use python energy_plot.py -h to get more information on input arguments.

![Example](./Example/plot.png)
