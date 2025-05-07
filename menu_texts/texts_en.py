# Menu texts in English

m_Initial = """
Select an option:
\t0 - Instructions.
\t1 - Load lattices for the system.
\t2 - Create system.
\t3 - Exit.
"""

m_Lattices = """
Load lattice:
\t1 - Manual input.
\t2 - Import from file.
\t3 - Done.
"""

m_System = """
What would you like to do?
\t0 - Create system.
\t1 - Show lattices in memory.
\t2 - Load more lattices.
\t3 - Exit.
"""

m_System_Create = """
What would you like to do next?
\t0 - Calculate primitive cell (PC).
\t1 - Rename the system.
\t2 - Show system.
\t3 - Show diffraction pattern.
\t4 - Export system to POSCAR file.
\t5 - Finish and exit.
"""

m_System_Mat = """
What do you want to do?
\t0-Use the selected TM to calculate the system's PC.
\t1-Display a table for the selected TM.
\t2-Select a new TM.
\t3-Perform a new search with different 'n' and 'epsilon'.
"""

m_Instructions = """\
x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+
   Enter the lattices that make up the system, in the same order they are stacked
(from bottom to top).

   Lattices can be added manually or imported from a POSCAR file. If added manually,
you'll first provide the primitive vectors (PVs), one component at a time.

   Then, you define the atomic basis. You'll enter the number of atomic species,
their symbols, their display colors, and the number of atoms per species.
Each atom must be placed using coordinates relative to the PVs.

   Once the lattices are defined, you can proceed to build the system. Then,
you can search for a primitive cell using two parameters: 'n' (search range)
and 'epsilon' (maximum allowed deformation).

   After finding a valid PC, you can visualize the system in real and reciprocal space,
generate a diffraction pattern, or export the result as a POSCAR file.
x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+
"""

m_newVector_err = "Invalid values entered. Please re-enter the vector components."

m_newAtomicBase_1 = "How many atomic species are in the lattice? "
m_newAtomicBase_2 = "**Error. Please enter an integer.**"
m_newAtomicBase_3 = "Empty atomic basis, there are no atoms in the lattice."
m_newAtomicBase_4 = "What is the symbol of the atomic species? "
m_newAtomicBase_5 = "Enter the display color for this atom type: "
m_newAtomicBase_6 = "\t**ERROR. Invalid value.**"
m_newAtomicBase_7_1 = "How many atoms of "
m_newAtomicBase_7_2 = " are in the basis? "
m_newAtomicBase_8 = "\t**Error. Please enter an integer.**"
m_newAtomicBase_9_1 = "\nEnter the relative position of atom "
m_newAtomicBase_9_2 = " with respect to the lattice's PVs."
m_newAtomicBase_10 = "Enter the component along primitive vector a: "
m_newAtomicBase_11 = "Enter the component along primitive vector b: "
m_newAtomicBase_12 = "Enter the component along primitive vector c: "
m_newAtomicBase_13 = "\t**ERROR. Please enter a positive integer.**"

m_menuNewL_1 = """
What would you like to do?
\t0 - Save created lattice
\t1 - View POSCAR of the created lattice
\t2 - View image of the created lattice
\t3 - Rotate the lattice
\t4 - Recreate the lattice
"""
m_menuNewL_2 = "Invalid input"
m_menuNewL_3 = "How many degrees do you want to rotate the lattice?"
m_menuNewL_4 = "Invalid input"

m_newLattice1_1 = "Enter the name of the lattice: "
m_newLattice1_2 = "Enter the primitive vectors of the lattice."
m_newLattice1_3 = "Adding atoms to the atomic basis..."
m_newLattice1_4 = "Lattice created."

m_newLattice2_1 = "Enter the name of the VASP file describing the lattice (without .vasp extension): "
m_newLattice2_2 = "Lattice imported successfully."

m_show_Lattice_1 = """
Which image would you like to display?
\t1 - Real space representation
\t2 - Reciprocal space representation
\t0 - Exit
"""
m_show_Lattice_2 = "Invalid input"

m_loadLattices_1 = "Invalid input. Choose 1, 2, or 3."
m_loadLattices_2_1 = "There are "
m_loadLattices_2_2 = " lattices in memory."

m_calcPC_1 = "Enter the value of 'n' to define the search area: "
m_calcPC_2 = "Invalid input. Please provide an integer greater than zero."
m_calcPC_3 = """Enter the value of 'epsilon', the maximum allowed deformation.
        A value below 0.05 is recommended: """
m_calcPC_4 = "Invalid input. Please enter a positive number."
m_calcPC_5 = "Invalid input. Please provide a positive number."
m_calcPC_6 = "No solution found with the given 'n' and 'epsilon'. Try increasing 'n' or 'epsilon'."
m_calcPC_7 = "It is suggested to use the following TM:"
m_calcPC_8 = "Invalid input"
m_calcPC_9 = "TMs in loMat:"
m_calcPC_10 = "Which TM in loMat do you choose? "

m_newSystem_0 = "Invalid input."
m_newSystem_1 = "System created with the stored lattices."
m_newSystem_2 = "Enter the new name: "
m_newSystem_3 = "Please calculate the PC of the system first."
m_newSystem_4 = "Enter the name for the POSCAR file: "

m_printLatticeNames_1 = "Lattices in memory:"

m_main_0 = "Invalid input."
m_main_1 = "Invalid input. Choose 0, 1, 2, or 3."