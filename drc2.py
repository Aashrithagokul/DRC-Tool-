import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

def plot_layout(lines):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 10))  # Adjust figsize as needed for your display

    # Set axis limits
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)

    # Major ticks every 0.45 units
    major_ticks = [i * 0.65 for i in range(7)]
    ax.set_xticks(major_ticks)
    ax.set_yticks(major_ticks)

    # Minor ticks every 0.15 units
    minor_ticks = [i * 0.15 for i in range(19)]
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(minor_ticks, minor=True)
    
    ax.grid(which='both', color='gray', linestyle=':', linewidth=0.5)

    # Plot lines
    colors = ['blue', 'green', 'red', 'purple', 'orange']
    labels = ['METAL 1', 'VIA 1', 'METAL 2', 'VIA 2', 'METAL 3']
    
    for i, line in enumerate(lines):
        for segment in line:
            x_vals = [point[0] for point in segment]
            y_vals = [point[1] for point in segment]
            ax.plot(x_vals, y_vals, marker='o', linestyle='-', color=colors[i], linewidth=2, markersize=6)
        
        # Add rectangle with label for each layer
        if i < len(labels):
            x_min = min(point[0] for segment in line for point in segment)
            x_max = max(point[0] for segment in line for point in segment)
            y_min = min(point[1] for segment in line for point in segment)
            y_max = max(point[1] for segment in line for point in segment)
            
            ax.add_patch(patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min, linewidth=1, edgecolor='black', facecolor='none'))
            ax.text((x_min + x_max) / 2, (y_min + y_max) / 2, labels[i], ha='center', va='center', fontsize=12, fontweight='bold', color='black')

    # Set labels and title
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Design Layout')

    # Adjust spacing between ticks
    ax.tick_params(axis='both', which='major', pad=35)  # Increase spacing between major ticks

    # Show plot
    plt.grid(True)
    plt.show()

def create_layer(layer_name, num_pairs):
    print("")
    print(f"Enter coordinates for {layer_name}:")
    points = []
    for i in range(num_pairs):
        try:
            x1, y1 = map(float, input(f"Enter x1, y1 for {layer_name} pair {i+1}: ").split(','))
            x2, y2 = map(float, input(f"Enter x2, y2 for {layer_name} pair {i+1}: ").split(','))
            points.append([(x1, y1), (x2, y2)])
        except ValueError:
            print("Invalid input! Please enter coordinates as 'x, y'")
    return points

def calculate_length_width_spacing(layer, layer_name):
    x1, y1 = layer[0][0]
    x2, y2 = layer[0][1]
    length_spacing = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    y1_first = layer[0][0][1]
    y2_first = layer[1][0][1]
    width_spacing = abs(y2_first - y1_first)
    
    return length_spacing, width_spacing

def check_rules(length_spacing, width_spacing, layer_name, length_rule, width_rule):
    if length_spacing > length_rule or width_spacing > width_rule:        
        print(f"Rules violated at {layer_name}")
    elif  length_spacing < length_rule or width_spacing < width_rule:
        print(f"Rules violated at {layer_name}")
            
    else:
        print(f"Rules not violated for {layer_name}")

# Define number of pairs for each layer
num_pairs_metal1 = 2
num_pairs_via1 = 2

# Create layers for metals and vias
metal1 = create_layer('METAL 1', num_pairs_metal1)
via1 = create_layer('VIA 1', num_pairs_via1)
metal2 = create_layer('METAL 2', num_pairs_metal1)
via2 = create_layer('VIA 2', num_pairs_via1)
metal3 = create_layer('METAL 3', num_pairs_metal1)

# Print the resulting nested lists
print("metal1 =", metal1)
print("via1 =", via1)
print("metal2 =", metal2)
print("via2 =", via2)
print("metal3 =", metal3)
print("")

# Calculate length and width spacings
length_spacing_metal1, width_spacing_metal1 = calculate_length_width_spacing(metal1, 'METAL 1')
length_spacing_via1, width_spacing_via1 = calculate_length_width_spacing(via1, 'VIA 1')
length_spacing_metal2, width_spacing_metal2 = calculate_length_width_spacing(metal2, 'METAL 2')
length_spacing_via2, width_spacing_via2 = calculate_length_width_spacing(via2, 'VIA 2')
length_spacing_metal3, width_spacing_metal3 = calculate_length_width_spacing(metal3, 'METAL 3')


# Foundry rules
foundry_rules = {
    'METAL 1': {'length': 0.05, 'width': 0.01},
    'VIA 1': {'length': 0.5, 'width': 0.005},
    'METAL 2': {'length': 0.05, 'width': 0.01},
    'VIA 2': {'length': 0.1, 'width': 0.02},
    'METAL 3': {'length': 0.1, 'width': 0.2}
}

# Check rules
check_rules(length_spacing_metal1, width_spacing_metal1, 'METAL 1', foundry_rules['METAL 1']['length'], foundry_rules['METAL 1']['width'])
check_rules(length_spacing_via1, width_spacing_via1, 'VIA 1', foundry_rules['VIA 1']['length'], foundry_rules['VIA 1']['width'])
check_rules(length_spacing_metal2, width_spacing_metal2, 'METAL 2', foundry_rules['METAL 2']['length'], foundry_rules['METAL 2']['width'])
check_rules(length_spacing_via2, width_spacing_via2, 'VIA 2', foundry_rules['VIA 2']['length'], foundry_rules['VIA 2']['width'])
check_rules(length_spacing_metal3, width_spacing_metal3, 'METAL 3', foundry_rules['METAL 3']['length'], foundry_rules['METAL 3']['width'])

# Plot layout
lines = [metal1, via1, metal2, via2, metal3]
plot_layout(lines)


'''
metal1 = [[(0.0, 0.0), (1.5, 0.0)], [(0.0, 0.5), (1.5, 0.5)]]
via1 = [[(0.5, 0.5), (1.0, 0.5)], [(0.5, 1.0), (1.0, 1.0)]]
metal2 = [[(0.0, 1.0), (1.5, 1.0)], [(0.0, 1.5), (1.5, 1.5)]]
via2 = [[(0.25, 1.5), (1.25, 1.5)], [(0.25, 2.0), (1.25, 2.0)]]
metal3 = [[(0.0, 2.0), (1.5, 2.0)], [(0.0, 2.5), (1.5, 2.5)]]
'''

def generate_report(spacings, foundry_rules):
    print(" ")
    print("  DESIGN RULE CHECKING(DRC)REPORT  ")
    
    # Summary of Calculations
    print("\n  CALCULATION SUMMARY   ")
    print("| {:<10} | {:>27} | {:>26} |".format('Layer', 'Calculated Length (μm)', 'Calculated Width (μm)'))
    print("|" + "-"*12 + "|" + "-"*29 + "|" + "-"*28 + "|")
    
    for layer_name in spacings:
        length_spacing = spacings[layer_name]['length']
        width_spacing = spacings[layer_name]['width']
        print(f"| {layer_name:<10} | {length_spacing:>27.2f} | {width_spacing:>26.2f} |")
    
    # Correction Summary
    print("\n  CORRECTION SUMMARY  ")
    print("| {:<10} | {:>29} | {:>28} |".format('Layer', 'Length Correction', 'Width Correction'))
    print("|" + "-"*12 + "|" + "-"*31 + "|" + "-"*30 + "|")
    
    for layer_name in spacings:
        length_spacing = spacings[layer_name]['length']
        width_spacing = spacings[layer_name]['width']
        foundry_length = foundry_rules[layer_name]['length']
        foundry_width = foundry_rules[layer_name]['width']
        
        length_action = ""
        width_action = ""
        
        if length_spacing > foundry_length:
            length_action = f"Decrease by {length_spacing - foundry_length:.2f} μm"
        else:
            length_action = f"Increase by {foundry_length - length_spacing:.2f} μm"

        if width_spacing > foundry_width:
            width_action = f"Decrease by {width_spacing - foundry_width:.2f} μm"
        else:
            width_action = f"Increase by {foundry_width - width_spacing:.2f} μm"
        
        print(f"| {layer_name:<10} | {length_action:>29} | {width_action:>28} |")

# Define spacings for each layer in a single dictionary
spacings = {
    'METAL 1': {'length': length_spacing_metal1, 'width': width_spacing_metal1},
    'VIA 1': {'length': length_spacing_via1, 'width': width_spacing_via1},
    'METAL 2': {'length': length_spacing_metal2, 'width': width_spacing_metal2},
    'VIA 2': {'length': length_spacing_via2, 'width': width_spacing_via2},
    'METAL 3': {'length': length_spacing_metal3, 'width': width_spacing_metal3}
}

# Generate the report
generate_report(spacings, foundry_rules)
