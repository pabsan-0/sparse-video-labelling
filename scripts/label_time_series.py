import os
import matplotlib.pyplot as plt
import argparse
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument('-d','--dir',       help="Path to the label-holding dir",     type=str)
parser.add_argument('-p','--prefix',    help="Prefix in <PREF>XXXX<SUF>.<EXT>",    type=str, default="")
parser.add_argument('-s','--suffix',    help="Suffix in <PREF>XXXX<SUF>.<EXT>",    type=str, default="")
parser.add_argument('-e','--extension', help="Extension in <PREF>XXXX<SUF>.<EXT>", type=str, default="txt")

args = parser.parse_args()


x_values = []
y_values = []
area_values = []

for ii in range(15000):
    
    fileidx = '{0:05d}'.format(ii)
    filename = f"{args.prefix}{fileidx}{args.suffix}.{args.extension}"
    filepath = os.path.join(args.dir, filename)
        
    # Initialize x, y, and area values
    x, y, area = (0, 0, 0)

    try:
        # Read the label file and extract x, y, and area values
        with open(filepath, 'r') as file:
            lines = file.readlines()
            if len(lines) > 0:
                line = lines[0].split()
                if len(line) >= 5:
                    x = float(line[1])
                    y = float(line[2])
                    width = float(line[3])
                    height = float(line[4])
                    area = width * height * 100 ## AREA GAIN

        # Append the values to the corresponding lists
        x_values.append(x)
        y_values.append(y)
        area_values.append(area)

    except FileNotFoundError:
        x_values.append(np.nan)
        y_values.append(np.nan)
        area_values.append(np.nan)

# Plotting the time series
fig = plt.figure(figsize=(12, 4))
plt.plot(y_values, label='y')
plt.plot(x_values, label='x')
plt.plot(area_values, label='area')
plt.xlabel('Label Number')
plt.ylabel('Value')
plt.legend()

# Save the plot as an SVG file to disk
output_path = f"{args.prefix}_{args.suffix}_ts.png"
plt.savefig(output_path)
plt.show()
