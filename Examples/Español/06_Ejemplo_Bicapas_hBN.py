# En este ejemplo se crearán dos homoestructuras bicapas de nitruro de boro hexagonal (hBN)
# con rotaciones relativas entre capas de 21.78° y 38.22°, respectivamente.
# Este ejemplo se ejecuta directamente desde un archivo de Python (.py).
# Las redes se cargan desde el archivo POSCAR 'hBN.vasp' ubicado en la carpeta 'VASP_Files'.
# Como resultado, se generarán los archivos "hBN(21_78).vasp" y "hBN(38_22).vasp",
# ambos con el mismo número de átomos y la misma red de Bravais,
# pero con distinto ángulo relativo y apilamiento en la región AA.

import nookiin
from nookiin.system import *

def main():
    try:
        # Se crean las dos redes que formarán los sistemas
        g1 = importLattice('VASP_Files/hBN')
        g2 = importLattice('VASP_Files/hBN')

        # Se definen los sistemas con las rotaciones correspondientes
        S1 = System([g1, g2.mRot(21.78)])
        S2 = System([g1, g2.mRot(38.22)])

        # Se calcula la PC (Primitive Cell) del primer sistema, se muestran los resultados y se exporta como POSCAR
        S1.generateSuperCell(RoS=17, eps=0.03, showTable=True)
        S1.diffractionPattern()
        S1.exportPC(PCname='hBN(21_78)')

        # Se calcula la PC del segundo sistema, se muestran los resultados y se exporta como POSCAR
        S2.generateSuperCell(RoS=17, eps=0.03, showTable=True)
        S2.diffractionPattern()
        S2.exportPC(PCname='hBN(38_22)')

        # Si todo sale correctamente, se imprime un mensaje en pantalla y termina la ejecución
        print("Correct execution of Nookiin.")
        return 1

    except Exception as e:
        # En caso de error, se muestra un mensaje antes de finalizar la ejecución
        print("An error occurred. Please check that Nookiin was installed correctly.")
        print(f"Error: {str(e)}")
        return -1

if __name__ == '__main__':
    sys.exit(main())