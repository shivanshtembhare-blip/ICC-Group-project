# 2D Molecular Structure Generator
A lightweight Python utility that converts chemical compound names into high-quality 2D skeletal diagrams. This tool leverages the RDKit informatics library to parse SMILES strings and Matplotlib for rendering.

#  Features
Dictionary-Based Lookup: Includes a pre-defined library of common organic compounds (e.g., Caffeine, Nicotine, Cholesterol).

SMILES Validation: Automatically checks if a SMILES string is valid before attempting to render.

Interactive Input: Allows users to query compounds by name through a simple command-line interface.

Clean Visualization: Generates standardized 2D diagrams with axes removed for a professional look.

#  Prerequisites
Before running the script, ensure you have Python installed along with the following libraries:
RDKIT,MATPLOTLIB
# Included Compounds
The generator currently supports a wide variety of molecules, including:

Alkaloids: Caffeine, Nicotine, Cocaine, Morphine.

Pigments: Lycopene, Beta-carotene.

Sugars: D-Glucose, Beta-lactose.

Polycyclic Aromatics: Coronene, Corannulene.

Medicinal: Sulfasalazine, Thiamine, Ephedrine.

# Usage
Enter the name of a compound when prompted (ensure correct capitalization as per the dictionary keys).

A window will pop up displaying the 2D molecular structure.

Example
Input: Cocaine

Output: <img width="1918" height="1015" alt="Screenshot 2026-04-19 220513" src="https://github.com/user-attachments/assets/f95206a1-b9f4-4507-9d08-5789263714d0" />


# How it Works
SMILES Mapping: The script maps the user-provided name to a SMILES string.

Molecule Object: Chem.MolFromSmiles() converts the string into an RDKit molecule object.

Image Generation: Draw.MolToImage() creates a PIL image of the 2D structure.

Rendering: Matplotlib displays the image without coordinate axes for clarity.
