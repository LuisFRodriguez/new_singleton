"""
Singleton Design Pattern

Intent: Lets you ensure that a class has only one instance, while providing a
global access point to this instance.
"""

from __future__ import annotations

from threading import Thread

from EscribirFile import EscribirFile
from CrearFile import CrearFile

if __name__ == "__main__":
    crearFile: CrearFile = CrearFile()

    file1: EscribirFile = crearFile.crearFile("hola_baby")
    print(file1.printFile())
    file2: EscribirFile = crearFile.crearFile("hola_princess")
    print(file2.printFile())
    file3: EscribirFile = crearFile.crearFile("lali")
    print(file3.printFile())

    if file1 is file2:
        print(file1)
        print(file1.printFile())

        print(file3)
        print(file3.printFile())
        print("los objetos de las files son iguales")
    else:
        print("los objetos de las files no son iguales")

 #   process1 = Thread(target=CrearFile.crearFile(), args=("FOO",))
 #   process2 = Thread(target=CrearFile.crearFile(), args=("BAR",))

 #   process1.start()
 #    process2.start()