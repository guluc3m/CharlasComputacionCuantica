##########################################################################################
#                                                                                        #
#           CHARLAS COMPUTACIÓN CUÁNTICA - GRUPO USUARIOS DE LINUX UC3M - 2019           #
#                                                                                        #
##########################################################################################

from qiskit import *

#Creamos el circuito con nuestros registros clásicos y cuánticos
myQR=QuantumRegister(4,"myQubit")
myCR=ClassicalRegister(4,"myBit")
myQC= QuantumCircuit(myQR, myCR)

#Aplicamos la puerta Hadamard a todos los qubits para ponerlos en superposición
myQC.h(myQR[0])
myQC.h(myQR[1])
myQC.h(myQR[2])
myQC.h(myQR[3])

#Medimos los qubits
myQC.measure(myQR[0], myCR[0])
myQC.measure(myQR[1], myCR[1])
myQC.measure(myQR[2], myCR[2])
myQC.measure(myQR[3], myCR[3])

#Imprimimos el circuito
print(myQC.qasm())
myQC.draw(output='mpl')

#Ejecutamos con el simulador una sola vez (para incrementar la aleatoriedad del experimento)
emulator = Aer.get_backend('qasm_simulator')
myJob = execute(myQC, emulator, shots=1)

#Imprimimos el número resultante
for key in myJob.result().get_counts():
    print(key)