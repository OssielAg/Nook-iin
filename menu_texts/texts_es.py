# Textos de menú en español

m_Initial = """
Seleccione una opción:
\t0 - Instrucciones.
\t1 - Cargar redes para el sistema.
\t2 - Crear sistema.
\t3 - Salir.
"""

m_Lattices = """
Cargar red:
\t1 - Entrada manual.
\t2 - Importar desde archivo.
\t3 - Terminado.
"""

m_System = """
¿Qué desea hacer?
\t0 - Crear sistema.
\t1 - Mostrar redes cargadas.
\t2 - Agregar más redes.
\t3 - Salir.
"""

m_System_Create = """
¿Qué desea hacer ahora?
\t0 - Calcular celda primitiva (PC).
\t1 - Renombrar el sistema.
\t2 - Mostrar sistema.
\t3 - Mostrar patrón de difracción.
\t4 - Exportar sistema como archivo POSCAR.
\t5 - Terminar y salir.
"""

m_System_Mat = """
¿Que desea hacer?
\t0-Usar la TM seleccionada para calcular la PC del sistema.
\t1-Mostrar tabla referente a la TM seleccionada.
\t2-Seleccionar una nueva TM.
\t3-Hacer una nueva busqueda con 'n' y 'epsilon' distintos.
"""

m_Instructions = """
x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+
   Introduzca las redes que forman el sistema, en el orden en que están apiladas
(de abajo hacia arriba).

   Las redes pueden ingresarse manualmente o importarse desde un archivo POSCAR.
Si se ingresan manualmente, primero debe proporcionar los vectores primitivos (VPs),
componente por componente.

   Luego se define la base atómica. Se ingresa el número de especies atómicas,
sus símbolos, colores para visualización y número de átomos por especie.
Cada átomo se posiciona con coordenadas relativas a los VPs.

   Una vez definidas las redes, se puede construir el sistema y posteriormente
buscar una celda primitiva para este utilizando los parámetros:
   - 'n': Para delimitar el rango de búsqueda
   - 'epsilon': Para definir un límite a la deformación aceptada

   Tras encontrar una PC válida, se puede visualizar el sistema en espacio real
y recíproco, generar un patrón de difracción o exportar como archivo POSCAR.
x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+
"""
m_newVector_err='Error en los valores ingresados. Ingrese de nuevo los componentes para el vector'

m_newAtomicBase_1="¿Cuantas especies atómicas hay en la red? "
m_newAtomicBase_2="**Error. Ingrese un número entero.**"
m_newAtomicBase_3="Base atómica bacía, no hay átomos en la red"
m_newAtomicBase_4="¿Cual es el simbolo de la especie atómica? "
m_newAtomicBase_5="Ingrese el color con el que se representarán los átomos: "
m_newAtomicBase_6="\t**ERROR.Valor no valido.**"
m_newAtomicBase_7_1="¿Cuantos átomos de "
m_newAtomicBase_7_2=" hay en la base? "
m_newAtomicBase_8="\t**Error. Ingrese un número entero.**"
m_newAtomicBase_9_1="\nIndique la posición relativa del átomo "
m_newAtomicBase_9_2=" con respecto a los VPs de la red."
m_newAtomicBase_10="Indique la componente correspondiente al VP a: "
m_newAtomicBase_11="Indique la componente correspondiente al VP b: "
m_newAtomicBase_12="Indique la componente correspondiente al VP c: "
m_newAtomicBase_13="\t**ERROR. Ingrese un número entero positivo.**"

m_menuNewL_1="""
¿Que desea hacer?
\t0-Guardar red creada
\t1-Ver POSCAR de la red creada
\t2-Ver Imagen de la red creada
\t3-Rotar la red
\t4-Crear de nuevo la red.
"""
m_menuNewL_2="Entrada inválida"
m_menuNewL_3="¿Cuantos grados se rotará la red?"
m_menuNewL_4="Entrada invalida"

m_newLattice1_1="Indique el nombre de la red: "
m_newLattice1_2="Indique los vectores primitivos de la red."
m_newLattice1_3="Ingresando Átomos de la base atómica..."
m_newLattice1_4="Red creada."

m_newLattice2_1='Ingrese el nombre del archivo VASP que describe la red (sin el .vasp): '
m_newLattice2_2="Red importada correctamente"

m_show_Lattice_1="""
¿Que imagen quiere desplegar?
\t1-Representación en el espacio Real
\t2-Representación en el espacio reciproco
\t0-Salir
"""
m_show_Lattice_2="Entrada invalida"

m_loadLattices_1="Entrada invalida. Elija 1, 2 o 3"
m_loadLattices_2_1="Hay "
m_loadLattices_2_2=" redes en memoria."

m_calcPC_1="Indique el valor de 'n' para delimitar el área de búsqueda: "
m_calcPC_2="Entrada invalida. Proporcione un número entero mayor a cero."
m_calcPC_3="""Indique el valor de 'epsilon', el error máximo aceptado.
        "Se recomienda un valor menor a 0.05: """
m_calcPC_4="Entrada invalida. Ingrese un número positivo."
m_calcPC_5="Entrada invalida. Proporcione un número positivo."
m_calcPC_6="No se encontró solución al sistema con los valores 'n' y 'epsilon' dados. Procure dar un valor mayor en 'n' o 'epsilon'."
m_calcPC_7="Se sugiere utilizar la siguiente TM:"
m_calcPC_8="Entrada invalida"
m_calcPC_9="TMs en loMat:"
m_calcPC_10="¿Cuál TM en loMat elige? "

m_newSystem_0="Entrada invalida."
m_newSystem_1="Se creo el sistema con las redes guardadas."
m_newSystem_2="Ingrese el nuevo nombre: "
m_newSystem_3="Antes calcule la PC del sistema."
m_newSystem_4="Ingrese el nombre para el archivo POSCAR: "

m_printLatticeNames_1="Redes en memoria:"

m_main_0="Entrada invalida."