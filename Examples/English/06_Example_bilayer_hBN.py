# Example 6: Construction of two bilayer homostructures of hexagonal Boron Nitride (hBN)
# Each bilayer will have a relative rotation angle between layers of 21.78° and 38.22°, respectively.
#
# This example is written as a standalone Python script (not a Jupyter notebook).
# The lattice structures are loaded directly from the POSCAR file 'hBN.vasp' located in the folder 'VASP_Files'.
# The resulting output files will be "hBN(21_78).vasp" and "hBN(38_22).vasp".
# Both structures will have the same number of atoms and the same Bravais lattice,
# but with different relative twist angles and AA stacking regions.

import nookiin
from nookiin.system import *

def main():
    try:
        # Create the two lattices that will form the systems
        g1 = importLattice('VASP_Files/hBN')
        g2 = importLattice('VASP_Files/hBN')
        
        # Define the systems with the corresponding rotation angles
        S1 = System([g1, g2.mRot(21.78)])
        S2 = System([g1, g2.mRot(38.22)])
        
        # Compute the commensurate supercell of the first system,
        # display results in the console, and export the POSCAR file
        S1.generateSuperCell(RoS=17, eps=0.03, showTable=True)
        S1.diffractionPattern()
        S1.exportPC(PCname='hBN(21_78)')
        
        # Compute the commensurate supercell of the second system,
        # display results in the console, and export the POSCAR file
        S2.generateSuperCell(RoS=17, eps=0.03, showTable=True)
        S2.diffractionPattern()
        S2.exportPC(PCname='hBN(38_22)')
        
        # If everything executed correctly, print success message and return
        print("Correct execution of Nookiin.")
        return 1
    
    except Exception as e:
        # If an error occurs, display an error message before exiting
        print("An error occurred. Please check that Nookiin is correctly installed.")
        print(f"Error: {str(e)}.")
        return -1

if __name__ == '__main__':
    sys.exit(main())
