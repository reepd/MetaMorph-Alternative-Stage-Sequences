# -*- coding: utf-8 -*-
"""
Created on 2024-11-19 Tue Nov 19 16:19:34 2024

@author: reepd
"""
import os
import numpy as np
import matplotlib.pyplot as plt

#to do
#remove edge wells for an 80 well layout.

# Path to the stage file
file_path = r'\\prfs.hhmi.org\genie\GECIScreenData\GECI_Imaging_Data\SCaMP\20241118_SCaMP_raw\96 well template - traditional.STG'

#visualize the traditional sequence

def visualize_traditional(original_data):
    grid = np.zeros((8, 12), dtype=int)
    indices = list(range(len(original_data)))  # Original indices

    for idx, val in enumerate(indices):
        grid[val // 12][val % 12] = idx + 1

    plt.figure(figsize=(10, 6))
    plt.imshow(grid, cmap='viridis', origin='upper')
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            plt.text(j, i, f'{grid[i][j]}', ha='center',
                     va='center', color='white')
    plt.xticks(np.arange(12), labels=np.arange(1, 13))
    plt.yticks(np.arange(8), list("ABCDEFGH"))
    plt.title('Traditional Sequence')
    plt.colorbar(label='Order')
    plt.show()

original_data = [str(i) for i in range(96)]  # dummy data for a 96 well plate
visualize_traditional(original_data)

# Snaking sequence
def snaking_sequence_list(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the lines from the file
            lines = file.readlines()

            # Extract the header (first 4 lines)
            header = lines[:4]

            # Remove newline characters and create the list for the rest of the data
            data = [line.strip() for line in lines[4:]]

            # Create the custom sequence
            custom_sequence_data = []
            for i in range(0, 96, 24):
                if (i // 12) % 2 == 0:
                    custom_sequence_data.extend(data[i:i+12])
                    custom_sequence_data.extend(data[i+23:i+11:-1])
                else:
                    custom_sequence_data.extend(data[i:i+12])
                    custom_sequence_data.extend(data[i+23:i+11:-1])

            # Combine header and custom sequence data
            result = header + [line + '\n' for line in custom_sequence_data]

            # Visualize the custom sequence data with changed indices
            visualize_custom_sequence(data, custom_sequence_data)

            return result
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def visualize_custom_sequence(original_data, custom_sequence_data):
    grid = np.zeros((8, 12), dtype=int)
    indices = list(range(len(original_data)))  # Original indices

    for idx, val in enumerate(indices):
        original_index = original_data.index(custom_sequence_data[idx])
        grid[original_index // 12][original_index % 12] = idx + 1

    plt.figure(figsize=(10, 6))
    plt.imshow(grid, cmap='viridis', origin='upper')
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            plt.text(j, i, f'{grid[i][j]}', ha='center',
                     va='center', color='white')
    plt.xticks(np.arange(12), labels=np.arange(1, 13))
    plt.yticks(np.arange(8), list("ABCDEFGH"))
    plt.title('Snaking Sequence')
    plt.colorbar(label='Order')
    plt.show()


# Reversed Sequence
def reverse_list_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the lines from the file
            lines = file.readlines()

            # Extract the header (first 4 lines)
            header = lines[:4]

            # Remove newline characters and create the list for the rest of the data
            data = [line.strip() for line in lines[4:]]

            # Reverse the rest of the list
            reversed_data = data[::-1]

            # Combine header and reversed data
            result = header + [line + '\n' for line in reversed_data]

            # Visualize the reversed data with changed indices
            visualize(data, reversed_data)

            return result
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def visualize(original_data, reversed_data):
    grid = np.zeros((8, 12), dtype=int)
    indices = list(range(len(original_data)))  # Original indices

    for idx, val in enumerate(indices):
        original_index = original_data.index(reversed_data[idx])
        grid[original_index // 12][original_index % 12] = idx + 1

    plt.figure(figsize=(10, 6))
    plt.imshow(grid, cmap='viridis', origin='upper')
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            plt.text(j, i, f'{grid[i][j]}', ha='center',
                     va='center', color='white')
    plt.xticks(np.arange(12), labels=np.arange(1, 13))
    plt.yticks(np.arange(8), list("ABCDEFGH"))
    plt.title('Reversed Sequence')
    plt.colorbar(label='Order')
    plt.show()

# Function to reorder the list to diagonal patterns


def reorder_list(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the lines from the file
            lines = file.readlines()

            # Extract the header (first 4 lines)
            header = lines[:4]

            # Remove newline characters and create the list for the rest of the data
            data = [line.strip() for line in lines[4:]]

            # Reorder the list
            reordered_data = []
            for i in range(13):
                reordered_data.extend(data[i::13])

            # Combine header and reordered data
            result = header + [line + '\n' for line in reordered_data]

            # Visualize the reordered data with changed indices
            visualize_reordered(data, reordered_data)

            return result
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def visualize_reordered(original_data, reordered_data):
    grid = np.zeros((8, 12), dtype=int)
    indices = list(range(len(original_data)))  # Original indices

    for idx, val in enumerate(indices):
        original_index = original_data.index(reordered_data[idx])
        grid[original_index // 12][original_index % 12] = idx + 1

    plt.figure(figsize=(10, 6))
    plt.imshow(grid, cmap='viridis', origin='upper')
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            plt.text(j, i, f'{grid[i][j]}', ha='center',
                     va='center', color='white')
    plt.xticks(np.arange(12), labels=np.arange(1, 13))
    plt.yticks(np.arange(8), list("ABCDEFGH"))
    plt.title('Diagonal Sequence')
    plt.colorbar(label='Order')
    plt.show()

# Function to reorder the list for topdown.STG


def topdown_list(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the lines from the file
            lines = file.readlines()

            # Extract the header (first 4 lines)
            header = lines[:4]

            # Remove newline characters and create the list for the rest of the data
            data = [line.strip() for line in lines[4:]]

            # Reorder the list
            topdown_data = []
            for i in range(12):
                topdown_data.extend(data[i::12])

            # Combine header and reordered data
            result = header + [line + '\n' for line in topdown_data]

            # Visualize the topdown data with changed indices
            visualize_topdown(data, topdown_data)

            return result
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def visualize_topdown(original_data, topdown_data):
    grid = np.zeros((8, 12), dtype=int)
    indices = list(range(len(original_data)))  # Original indices

    for idx, val in enumerate(indices):
        original_index = original_data.index(topdown_data[idx])
        grid[original_index // 12][original_index % 12] = idx + 1

    plt.figure(figsize=(10, 6))
    plt.imshow(grid, cmap='viridis', origin='upper')
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            plt.text(j, i, f'{grid[i][j]}', ha='center',
                     va='center', color='white')
    plt.xticks(np.arange(12), labels=np.arange(1, 13))
    plt.yticks(np.arange(8), list("ABCDEFGH"))
    plt.title('Topdown Sequence')
    plt.colorbar(label='Order')
    plt.show()


#snaking sequence
snaking_list_with_header = snaking_sequence_list(file_path)
#save snaking sequence to a new file with name "snaking.STG"
output_file_path = os.path.join(os.path.dirname(file_path), 'snaking.STG')
with open(output_file_path, 'w') as output_file:
    output_file.writelines(snaking_list_with_header)
    
print(f"Snaking sequence saved to {output_file_path}")

# Get the reversed list with header at the start
reversed_list_with_header = reverse_list_from_file(file_path)

# Save the reversed list to a new file in the same directory with name "reverse.STG"
output_file_path = os.path.join(os.path.dirname(file_path), 'reverse.STG')
with open(output_file_path, 'w') as output_file:
    output_file.writelines(reversed_list_with_header)

print(f"Reversed list saved to {output_file_path}")

# Get the reordered list with header at the start
reordered_list_with_header = reorder_list(file_path)

# Save the reordered list to a new file in the same directory with name "diagonal.STG"
output_file_path_reordered = os.path.join(
    os.path.dirname(file_path), 'diagonal.STG')
with open(output_file_path_reordered, 'w') as output_file:
    output_file.writelines(reordered_list_with_header)

print(f"Reordered list saved to {output_file_path_reordered}")

# Get the topdown list with header at the start
topdown_list_with_header = topdown_list(file_path)

# Save the topdown list to a new file in the same directory with name "topdown.STG"
output_file_path_topdown = os.path.join(
    os.path.dirname(file_path), 'topdown.STG')
with open(output_file_path_topdown, 'w') as output_file:
    output_file.writelines(topdown_list_with_header)

print(f"Topdown list saved to {output_file_path_topdown}")


