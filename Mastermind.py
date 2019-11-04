##########################################################################################
#                                                                                        #
#           CHARLAS COMPUTACIÓN CUÁNTICA - GRUPO USUARIOS DE LINUX UC3M - 2019           #
#                                                                                        #
##########################################################################################

from qiskit import *

#Creamos el circuito con nuestros registros clásicos y cuánticos
myQR=QuantumRegister(5,"myQubit")
myCR=ClassicalRegister(4,"myBit")
myQC= QuantumCircuit(myQR, myCR)

#Le aplicamos hadamard a los primeros 4 qubits
myQC.h(myQR[0])
myQC.h(myQR[1])
myQC.h(myQR[2])
myQC.h(myQR[3])

#Convertimos el último qubit (temp) de |0> a |1> y lo superponemos
myQC.x(myQR[4])
myQC.h(myQR[4])

#Operas con una CNOT (cambia de fase si es 1) aquellos bits que nosotros elegimos como clave
myQC.cx(myQR[3], myQR[4])
myQC.cx(myQR[1], myQR[4])

#Volvemos a hacer una Hadamard, esto debería poner a 0 los que son 0 y a 1 los que son 1
myQC.h(myQR[3])
myQC.h(myQR[2])
myQC.h(myQR[1])
myQC.h(myQR[0])

#Medimos
myQC.measure(myQR[0], myCR[0])
myQC.measure(myQR[1], myCR[1])
myQC.measure(myQR[2], myCR[2])
myQC.measure(myQR[3], myCR[3])

#Dibujamos el circuito
print(myQC.qasm())
myQC.draw(output='mpl')

#Ejecutamos el simulador, esta vez lo haceos 1024 para tener más probabilidades de conseguir el número correcto
emulator = Aer.get_backend('qasm_simulator')
myJob = execute(myQC, emulator, shots=1024)

#Imprimimos el número de mayor probabilidad
histogram = myJob.result().get_counts()
max = 0
for i in histogram:
    if max == 0 or histogram[max] < histogram[i]:
        max = i
print(i)