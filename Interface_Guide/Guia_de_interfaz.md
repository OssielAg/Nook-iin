# 🖥️ Guía de Uso de la Interfaz en Consola - Nook'iin
[(English version)](/Interface_Guide/Interface_Guide.md)
  
Esta guía proporciona instrucciones paso a paso para utilizar la interfaz en consola del programa **Nook’iin**, diseñado para crear y analizar sistemas bidimensionales multicapa mediante métodos geométricos.
 
---

## 📋 Índice

1. [Requisitos previos](#requisitos-previos)  
2. [Ejecución de la interfaz](#ejecución-de-la-interfaz)  
3. [Selección de idioma](#selección-de-idioma)  
4. [Menú principal](#menú-principal)  
   4.1 [Menú de carga de redes](#menú-de-carga-de-redes)  
   &nbsp;&nbsp;&nbsp;&nbsp;4.1.1 [Entrada manual](#entrada-manual)  
   &nbsp;&nbsp;&nbsp;&nbsp;4.1.2 [Importar desde archivo](#importar-desde-archivo)  
   4.2 [Menú de red](#menú-de-red)  
   &nbsp;&nbsp;&nbsp;&nbsp;4.2.1 [Comprobar red](#comprobar-red)  
   &nbsp;&nbsp;&nbsp;&nbsp;4.2.2 [Rotar redes](#rotar-redes)  
   &nbsp;&nbsp;&nbsp;&nbsp;4.2.3 [Guardar red](#guardar-red)  
   4.3 [Menú de sistema](#menú-de-sistema)  
   &nbsp;&nbsp;&nbsp;&nbsp;4.3.1 [Cálculo de la celda primitiva](#cálculo-de-la-celda-primitiva)  
   &nbsp;&nbsp;&nbsp;&nbsp;4.3.2 [Tabla de datos para matrices](#tabla-de-datos-para-matrices)  
   &nbsp;&nbsp;&nbsp;&nbsp;4.3.3 [Mostrar sistema](#mostrar-sistema)  
   &nbsp;&nbsp;&nbsp;&nbsp;4.3.4 [Exportar a POSCAR](#exportar-a-poscar)  
5. [Créditos y contacto](#créditos-y-contacto)


---
## Requisitos previos  
- Tener instalado **Python 3.x**  
- Haber descargado el repositorio de **Nook’iin**  
- Ejecutar el programa desde una consola (Terminal, CMD o PowerShell)
---
##  Ejecución de la interfaz

   Desde la carpeta principal del repositorio, ejecuta en la consola:

   ```bash
   python  interface.py
   ```
   ---

## Selección de idioma

   Al iniciar, el primer menú que se despliega solicita al usuario seleccionar el idioma en el que se mostrará la interfaz: Español o Inglés.


   ![Menú de idioma](images/Menu_idioma.png)

   Dependiendo del idioma elegido, se debe ingresar 1 para Español o 2 para Inglés.

   ---

## Menú principal

Una vez que se ha seleccionado el idioma, se muestra el menú principal de la interfaz. Desde aquí se puede acceder a las funcionalidades principales del programa. Las opciones disponibles son las siguientes:

0. **-Instrucciones** → Despliega un texto con las instrucciones para usar la interfaz.
1. **-Cargar redes para el sistema** → Ingresa al menú para cargar las redes que conforman el sistema.
2. **-Crear sistema** → Ingresa al menú para crear y trabajar con el sistema formado por las redes cargadas previamente.
3. **-Salir** → Termina la ejecución.

![Menú principal](images/Menu_principal.png)

---

### Menú de carga de redes

Al elegir la opción **1** del menú principal, se despliega el menú de carga de redes, con las siguientes opciones:

1. **Entrada manual** → Despliega un nuevo menú para crear manualmente la red indicando sus *vectores primitivos* y su *base atómica*.
2. **Importar desde archivo** → Solicita al usuario el nombre del archivo VASP correspondiente a la red.
3. **Terminado** → Regresa al menú principal.

![Menú carga de redes](images/Menu_Redes_carga.png)

#### Entrada manual

Al seleccionar **Entrada manual** para cargar una nueva red, lo primero que se le pide al usuario es el nombre que tendrá la red (en este ejemplo, crearemos manualmente una red de grafeno).

![Menú carga manual 1](images/Menu_Redes_carga_manual1.png)

Lo siguiente es definir los vectores primitivos componente a componente, comenzando por el PV $ a = (a_1, a_2, a_3) $.

![Menú carga manual 2](images/Menu_Redes_carga_manual2.png)

Se mostrará en pantalla el vector dado por el usuario y se continuará con los vectores $ b = (b_1, b_2, b_3) $ y $ c = (c_1, c_2, c_3) $.

Una vez definidos los 3 vectores primitivos, estos se mostrarán en pantalla y se comenzará a definir la base atómica de la red. La primera pregunta para el usuario será el número de especies atómicas distintas en la base atómica de la red (en el caso del grafeno, sólo se tiene una especie atómica: el carbono).

Para cada una de estas especies atómicas, se pedirá un *símbolo* que la identifique (en el caso del carbono será la letra **C**), el *color* con el que queremos que sea representado (acepta los formatos de color de Python, tanto los definidos con texto 'white', 'b', como en formato hexadecimal) y la *cantidad* de átomos de esa especie en la base atómica.

![Menú carga manual 3](images/Menu_Redes_carga_manual3.png)

Dados estos datos, se pedirá al usuario que indique la posición relativa (con respecto a los vectores primitivos previamente definidos) de cada uno de los átomos de la especie que se está definiendo.

![Menú carga manual 4](images/Menu_Redes_carga_manual4.png)

![Menú carga manual 5](images/Menu_Redes_carga_manual5.png)

Una vez definidos todos los átomos de la base atómica, la red está creada.

#### Importar desde archivo

Al seleccionar **Importar desde archivo** para cargar una nueva red, se pedirá al usuario la dirección del archivo VASP correspondiente a la red sin escribir la extensión *.vasp* en el nombre. En la carpeta *VASP_Files* ya se tienen algunos archivos VASP de redes cristalinas que pueden ser usados (para el ejemplo, se importará desde la carpeta *VASP_files* el archivo *GeSe_beta.vasp*, correspondiente a la red del $ \beta $-GeSe).

![Menú carga archivo 1](images/Menu_Redes_carga_archivo1.png)

Si no hay problema en la importación del archivo, la red ya está correctamente cargada.
### Menú de red

Una vez cargada una red correctamente, ya sea de forma manual o importada desde un archivo, se accede al menú de red. En este, se tienen las siguientes opciones:

0. **Guardar red creada** → Guarda la red en la lista de redes que formarán el sistema y regresa al menú anterior.
1. **Ver POSCAR de la red creada** → Muestra en pantalla el archivo POSCAR de la red creada.
2. **Ver imagen de la red creada** → Despliega en pantalla una imagen de la celda primitiva de la red.
3. **Rotar la red** → Permite rotar la red antes de ingresarla a la lista de redes del sistema. Esta opción es necesaria para crear sistemas formados por redes con distintas orientaciones relativas, donde al definir la red de cada capa no se contempló previamente una transformación de rotación para los PVs.
4. **Crear de nuevo la red** → Se descarta la red y se comienza de nuevo su creación.

#### Comprobar red

Si el usuario quiere asegurarse de que la red sea correcta antes de agregarla a la lista del sistema, puede comprobarla con las opciones **1** y **2** del menú de red, ya sea verificando el archivo POSCAR o con la imagen de la celda primitiva.

![POSCAR de red](images/Menu_Redes_POSCAR.png)

*POSCAR de la red de GeSe importada.*

![PC de red](images/Menu_Redes_PC.png)

*Imagen de la celda primitiva de la red de GeSe importada.*

#### Rotar redes

Para generar la rotación en una red del sistema, se escoge la opción **3** del menú de red. Al hacerlo, se pedirá al usuario cuántos grados se rotará la red. Una vez proporcionado el valor, la red será rotada y su efecto podrá verse reflejado si se solicita ver la imagen de la celda primitiva después de la transformación.

En nuestro ejemplo, el sistema que analizaremos será una bicapa de $ \beta $-GeSe sobre grafeno con una rotación relativa entre capas de $ 13.52^\circ $, por lo que debemos rotar la red de $ \beta $-GeSe en $ 13.52^\circ $.

![PC de red rotada](images/Menu_Redes_PC-Rotada.png)

*Imagen de la celda primitiva de la red de GeSe después de ser rotada.*

#### Guardar red

Si la red definida es correcta, se elige la opción **0** del menú de red para agregarla a la lista de redes que conformarán el sistema. El orden en que las redes son guardadas en la lista será el mismo en el que estarán apiladas, donde la primera red guardada será la base de la pila (esta será la que internamente será tomada por el programa como la *capa sustrato*).

Tras guardar cada red, se regresará al *Menú de carga de redes*, donde se podrá iniciar la carga de una nueva red o finalizar el proceso eligiendo la opción **3**. Al hacerlo, se indicará cuántas redes hay guardadas y se regresará al *Menú principal*, donde se podrá inicializar el sistema.
## Menú de sistema

Al seleccionar la opción **2** del *Menú principal*, *Crear sistema*, se desplegará el **Menú de creación de sistema**, donde se presentarán las siguientes opciones:

0. **Crear sistema** → Se inicializa el sistema con las redes dadas tal y como están.
1. **Mostrar redes cargadas** → Se despliega una lista con los nombres de las redes cargadas.
2. **Agregar más redes** → Envía al *Menú de carga de redes* para agregar más redes.
3. **Salir** → Termina la ejecución del programa.

Una vez que se decida que la lista de redes es correcta, se puede elegir la opción **0** para inicializar el sistema. Si esto se realiza satisfactoriamente, se desplegará el **Menú de sistema**, que presenta las siguientes opciones:

0. **Calcular celda primitiva** → Inicia el proceso para calcular una celda primitiva del sistema.
1. **Renombrar el sistema** → Cambia el nombre del sistema.
2. **Mostrar sistema** → Si ya se calculó una PC para el sistema, la despliega en pantalla.
3. **Mostrar patrón de difracción** → Calcula el patrón de difracción del sistema y muestra una imagen de este (requiere que se haya calculado previamente una PC para el sistema).
4. **Exportar sistema como archivo POSCAR** → Genera el archivo POSCAR correspondiente a la PC calculada (requiere que ya se haya calculado una PC para el sistema).
5. **Terminar y salir** → Finaliza la ejecución del programa.

### Cálculo de la celda primitiva

Al elegir la opción **0**, comenzará el proceso para calcular posibles celdas primitivas para el sistema. Lo primero que se solicita al usuario son las variables $ n $, que determina el *área de búsqueda* que delimita las superceldas candidatas a ser celdas primitivas, y $ epsilon $, que define un *límite* para la deformación que pueden tener las redes del sistema para mantener la periodicidad.

Si se encuentra al menos una posible celda primitiva, se mostrará en pantalla la matriz de transformación correspondiente a la candidata recomendada como celda primitiva del sistema. En el ejemplo manejado, se utilizaron los valores $n = 15$ y $epsilon = 0.03$.

![Menú de elección de TM](images/Menu_Analisis1.png)

El nuevo menú desplegado presenta las opciones:

0. **Usar la TM seleccionada para calcular la PC del sistema** → Crea la celda primitiva con la TM seleccionada.
1. **Mostrar tabla referente a la TM seleccionada** → Muestra en pantalla una tabla con información correspondiente a la TM seleccionada.
2. **Seleccionar una nueva TM** → Muestra todas las opciones de matrices de transformación calculadas para que el usuario elija la más conveniente.
3. **Hacer una nueva búsqueda con $n$ y $epsilon$ distintos** → Repite la búsqueda con nuevos valores para las variables $n$ y $epsilon$.

### Tabla de datos para matrices

Si se elige la opción **1** o **2** en el menú anterior, se desplegará una tabla con la información correspondiente a cada TM. En esta se presentan, para cada capa, las matrices de transformación, las matrices de deformación, los valores de distorsión de sus PVs y el número de átomos. Estos datos ayudarán al usuario a entender los efectos de cada TM y a seleccionar la más conveniente para su problema.

![Tabla de datos de una TM](images/Menu_Analisis2.png)

Ya sea que se acepte la matriz propuesta por el sistema o se elija otra, se debe utilizar la opción **0** del menú para crear la celda primitiva correspondiente al sistema. Al hacerlo, la interfaz regresará al *Menú de sistema*.

### Mostrar sistema

Una vez calculada una PC, se puede elegir la opción **2** del *Menú de sistema*. Al hacerlo, se podrá visualizar una representación del sistema en el espacio real de la celda primitiva calculada, o en el espacio recíproco, como una superposición de las FBZ de cada capa en una malla formada por la repetición periódica de la FBZ de la PC calculada.

![Imagen del sistema en el espacio real](images/Menu_AnalisisR.png)

*Representación en el espacio real.*

![Imagen del sistema en el espacio recíproco](images/Menu_AnalisisR'.png)

*Representación en el espacio recíproco.*

También es posible obtener la imagen del patrón de difracción del sistema eligiendo la opción **3** del *Menú de sistema*. Al hacerlo, comenzará el cálculo del patrón de difracción (este proceso puede tardar algunos minutos si la celda primitiva contiene muchos átomos).

![Imagen del patrón de difracción](images/Menu_AnalisisDP.png)

*Patrón de difracción correspondiente al sistema de ejemplo.*

### Exportar a POSCAR

Una vez calculada la PC del sistema, al elegir la opción **4** del *Menú de sistema*, se solicitará al usuario el nombre del archivo `.vasp` en el que se exportará la PC. El archivo resultante se almacenará en la carpeta *VASP_files*.

El resultado del ejemplo fue exportado al archivo llamado `Sistema Grafeno-beta_GeSe(13_52)`

## Créditos y contacto

**Autor:** Ossiel Aguilar-Spíndola  
**Grado académico:** Licenciado en Ciencias de la Computación  
**Correo de contacto:** [OssielAE@ciencias.unam.mx](mailto:OssielAE@ciencias.unam.mx)  
**ORCID:** [0009-0002-8229-8543](https://orcid.org/0009-0002-8229-8543)

Este programa, *Nook’iin*, fue desarrollado como parte de la tesis de licenciatura *"Software para la construcción de sistemas multicapa conmensurables de dos dimensiones"*, bajo la supervisión del Dr. Francisco Sánchez Ochoa en el Instituto de Física de la Universidad Nacional Autónoma de México (UNAM).

### Licencia:
Este software se distribuye bajo la Licencia Pública General GNU (GNU GPL). Para más detalles, consultar el archivo `LICENSE`.

### Agradecimientos:  
Este proyecto fue posible gracias al apoyo de diversos programas e instituciones de investigación. Se agradece especialmente a los siguientes por su respaldo académico y financiero:

#### Programas de apoyo a la investigación:
- PBIF24-2: Apoyo para la finalización del proyecto de tesis.  
- DGAPA-PAPIIT (UNAM) IA105623: *Grafeno multicapa bajo presión hidrostática: un estudio de primeros principios*.  
- CONAHCYT CF-2023-I-336: *Estudio ab initio de cristales no convencionales de van der Waals presurizados*.  
- CONAHCYT 1564464: *Analogías en la física de sistemas 2D rotados: de escala atómica a nanométrica*.  
- CONAHCYT: Beca de asistente de investigación SNI-III.

#### Presentaciones y divulgación:
Resultados parciales de este proyecto fueron presentados en los siguientes eventos científicos:

- *2° Encuentro Anual, Analogías en la Física de Sistemas 2D Rotados: de Escala Atómica a Nanométrica* (2024), Pachuca, Hidalgo, México.  
- *XII Reunión Anual de la División de Estado Sólido* (2024), Xicotepec, Puebla, México.  
- *Día de Puertas Abiertas del Instituto de Física - UNAM* (2023), Ciudad de México, México.  
- *Gathering on Transport at the Nanoscale* (2023), Cuernavaca, Morelos, México.  
- *XVI International Conference on Surfaces, Materials and Vacuum* (2023), Zacatecas, Zacatecas, México.

Agradezco sinceramente el apoyo y las oportunidades brindadas por estas instituciones, así como a la comunidad científica que contribuyó al desarrollo y difusión de esta investigación.
