# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:43:24 2024

@author: reepd
"""

# Function to reorder the list for inward_spiral.STG
# A1->A12, then B12-> H12, then H11->H1, then G1->B1, then B2-> B11,
# then C11->G11, then G10-> G2, then F2->C2, then C3->C10, then D10-> F10,
# then F9-> F3, then E3->D3, then D4->D9, then E9->E4.

# alternative explanation:
# positions 1-12, then 24-96 in increments of 12, then 95-85 counting down
# in increments of 1, then 73 to 13 counting down in increements of 12, then
# 14-23, then 35 to 83 in increments of 12, then 82-74, then 62 to 26
# counting down in increments of 12, then 27-34, then 46-70 in increments of 12,
# then 69 to 63 counting down, then 51, then 39, then 40-45, then 57 to 52 counting
# down. that should be a total of 96 positions.
import os
import matplotlib.pyplot as plt
import numpy as np


#to do
#remove edge wells for an 80 well layout.


# Path to the stage file

file_path = r'\\prfs.hhmi.org\genie\GECIScreenData\GECI_Imaging_Data\SCaMP\20241118_SCaMP_raw\96 well template - traditional.STG'



def inward_spiral_list(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            header, data = lines[:4], [line.rstrip('\n') for line in lines[4:]]
            if len(data) != 96:
                print("The list length is not 96. Cannot create inward_spiral.STG.")
                return []
            spiral_indices = [
                *range(0, 12),      # A01-A12
                *range(23, 96, 12), # B12-H12
                *range(94, 83, -1), # H11-H01
                *range(72, 11, -12),# G01-B01
                *range(13, 23),     # B02-B11
                *range(34, 83, 12), # C11-G11
                *range(81, 72, -1), # G10-G02
                *range(61, 24, -12),# F02-C02
                *range(26, 34),     # C03-C10
                *range(45, 71, 12), # D10-F10
                *range(68, 61, -1), # F09-F03
                50, 38,             # E03&D03
                *range(39, 45),     # D04-D09
                *range(56, 50, -1)  # E09-E04
            ]
            return header + [data[i] + '\n' for i in spiral_indices]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


output_file_path_inward_spiral = os.path.join(
    os.path.dirname(file_path), 'inward_spiral.STG')
with open(output_file_path_inward_spiral, 'w') as output_file:
    output_file.writelines(inward_spiral_list(file_path))
print(f"Inward spiral list saved to {output_file_path_inward_spiral}")


def visualize_inward_spiral():
    grid = np.zeros((8, 12), dtype=int)
    spiral_indices = [
                *range(0, 12),      # A01-A12
                *range(23, 96, 12), # B12-H12
                *range(94, 83, -1), # H11-H01
                *range(72, 11, -12),# G01-B01
                *range(13, 23),     # B02-B11
                *range(34, 83, 12), # C11-G11
                *range(81, 72, -1), # G10-G02
                *range(61, 24, -12),# F02-C02
                *range(26, 34),     # C03-C10
                *range(45, 71, 12), # D10-F10
                *range(68, 61, -1), # F09-F03
                50, 38,             # E03&D03
                *range(39, 45),     # D04-D09
                *range(56, 50, -1)  # E09-E04
    ]
    for idx, val in enumerate(spiral_indices):
        grid[val // 12][val % 12] = idx + 1
    plt.figure(figsize=(10, 6))
    plt.imshow(grid, cmap='viridis', origin='upper')
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            plt.text(j, i, f'{grid[i][j]}', ha='center',
                     va='center', color='white')
    plt.xticks(np.arange(12), labels=np.arange(1, 13))
    plt.yticks(np.arange(8), list("ABCDEFGH"))
    plt.title('Inward Spiral Sequence')
    plt.colorbar(label='Order')
    plt.show()


visualize_inward_spiral()
