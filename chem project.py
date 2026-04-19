from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt
smiles = {'Caffeine': 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C', 'Methylamine': 'CN',
'Nicotine': 'CN1CCCC1C2=CN=CC=C2', 'Lycopene':
r'CC(=CCC/C(=C/C=C/C(=C/C=C/C(=C/C=C/C=C(/C=C/C=C(/C=C/C=C(/CCC=C(C)C)\C)\C)\C)/C)/C)/C)C',
 'Beta carotene':
r'CC1=C(C(CCC1)(C)C)/C=C/C(=C/C=C/C(=C/C=C/C=C(/C=C/C=C(/C=C/C2=C(CCCC2(C)C)C)\C)\C)/C)/C',
 'Sulfasalazine': 'C1=CC=NC(=C1)NS(=O)(=O)C2=CC=C(C=C2)N=NC3=CC(=C(C=C3)O)C(=O)O', 'Efavirenz': 'C1CC1C#C[C@]2(C3=C(C=CC(=C3)Cl)NC(=O)O2)C(F)(F)F',
 'D-Glucose': 'C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O',
 'Beta lactose'
:'C([C@@H]1[C@@H]([C@@H]([C@H]([C@@H](O1)O[C@@H]2[C@H](O[C@H]([C@@H]([C@H]2O)O)O)CO)O)O)O)O',
 'Corannulene':'C1=CC2=C3C4=C1C=CC5=C4C6=C(C=C5)C=CC(=C36)C=C2',
 'Coronene': 'C1=CC2=C3C4=C1C=CC5=C4C6=C(C=C5)C=CC7=C6C3=C(C=C2)C=C7',
 'Porphyrin ring':'C1=CC2=CC3=CC=C(N3)C=C4C=CC(=N4)C=C5C=CC(=N5)C=C1N2',
 'Methylene blue': 'CN(C)C1=CC2=C(C=C1)N=C3C=CC(=[N+](C)C)C=C3S2.[Cl-]',
 'Thiamine': 'CC1=C(SC=[N+]1CC2=CN=C(N=C2N)C)CCO.[Cl-]', 'Nicotine': 'CN1CCCC1C2=CN=CC=C2',
'Codeine':'[H][C@@]12OC3=C(OC)C=CC4=C3[C@@]11CCN(C)[C@]([H])(C4)[C@]1([H])C=C[C@@H]2O',
 'Morphine': 'CN1CC[C@]23[C@@H]4[C@H]1CC5=C2C(=C(C=C5)O)O[C@H]3[C@H](C=C4)O',
'Ephedrine': 'CN[C@H]([C@@H](c1ccccc1)O)C',
 'Cocaine': 'CN1[C@H]2CC[C@@H]1[C@H]([C@H](C2)OC(=O)C3=CC=CC=C3)C(=O)OC',
 'Cholesterol':
'C[C@H](CCCC(C)C)[C@H]1CC[C@@H]2[C@@]1(CC[C@H]3[C@H]2CC=C4[C@@]3(CC[C@@H](C4)O)C)C'}
compound_name = input('Enter the name of the compound: ')
if compound_name in smiles:
 smiles_notation = smiles[compound_name]
 mol = Chem.MolFromSmiles(smiles_notation)
 # Check if the molecule was successfully created
 if mol is not None:
     img = Draw.MolToImage(mol, size=(300, 300))
     plt.imshow(img)
     plt.axis('off')
     plt.show() # Display the image using Matplotlib
 else:
     print('Invalid SMILES notation.')
else:
     print ('Compound not found in the dictionary ')
