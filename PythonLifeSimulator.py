##########################################################################################
#                                                                                        #
#           CHARLAS COMPUTACIÓN CUÁNTICA - GRUPO USUARIOS DE LINUX UC3M - 2019           #
#                                                                                        #
##########################################################################################

import random
 
#Clase con los atributos del jugador
class Player():
    #Usamos self para los atributos globales a la clase
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sleepiness = 0
        self.energy = 100
        self.hunger = 0
        self.happiness = 50
        self.alive = True
 
    def eat(self):
        self.hunger -= 3
        self.sleepiness += 2
        self.energy += 1
        self.happiness += 1
 
    def sleep(self):
        self.hunger += 5
        self.sleepiness = 0
        self.energy = 90
        self.happiness = 65
 
#Clase con el juego y atributos métodos propios
class Simulador():
    #Utilizamos pass cuando no queremos borrar un método, para que no de error
    def __init__(self):
        pass
 
    #npc es un atributo, puede tener cualquier nombre, se puede ver en las otras funciones
    def study(npc):
        npc.hunger += 3
        npc.energy -= 4
        npc.sleepiness += 4
        npc.happiness -= 4
 
    def go_out(jugador):
        jugador.hunger -= 2
        jugador.energy -= 5
        jugador.happiness = 7
        jugador.sleepiness -= 5
 
    #Imprimimos un menú para que el jugador sepa que opciones tiene
    def options():
        print('1-Estudiar')
        print('2-Salir')
        print('3-Comer')
        print('4-Dormir')
 
    #En cada iteración imprimimos el nivel de cada atributo para mayor claridad
    def status(npc):
        print('Tu nivel de hambre se encuentra al: ' + str(npc.hunger) + '%')
        print('Tu nivel de energía se encuentra al: ' + str(npc.energy) + '%')
        print('Tu nivel de felicidad se encuentra al: {}%'.format(npc.happiness))
        print('Tu nivel de sueño se encuentra al: {}%'.format(npc.sleepiness))
 
 ######     EL JUEGO     #####
    
    #Pedimos al jugador los valores de inicio
    player_name = input('¿Cómo te llamas?: ')
    player_age = input('¿Cuántos años tienes?: ')
    #Inicializamos al jugador
    player = Player(player_name, player_age)
 
    #Inicializamos la lista de acciones con un elemento vacío para que no de errores al hacer  index-2 en el primer elemento, hay opciones más elegantes pero dada la velocidad con la que se desarrollo este script aceptamos la ñapa
    actions = ['']
 
    #Nuestro while True de juego
    while(player.alive):
 
        #Pedimos acción y la añadimos a la lista de acciones
        answer = input('¿Qué quieres hacer? (escribe help para más información): ')
        actions.append(answer)
 
        if(answer == 'help'):
            #Comprobamos si las dos últimas acciones han sido help, en cuyo caso imprimimos un mensaje personalizado, veremos esto con todas las posibles accinoes
            if(actions[len(actions)-1] == 'help' and actions[len(actions)-2] == 'help'):
                print('Estás empezando a aburrirme...')
            options()
        else:
            #Comprobamos tanto la palabra como el número que se ha impreso en help
            if((answer == 'Estudiar') or (answer == '1')):
                if((actions[len(actions)-1] == 'Estudiar' and actions[len(actions)-2] == 'Estudiar') or (actions[len(actions)-1] == '1' and actions[len(actions)-2] == '1')):
                    print('Me ha tocado el empollón de turno...')
                #Llamamos a la función estudiar, que está en esta misma clase
                study(player)
            elif(answer == 'Salir' or answer == '2'):
                if((actions[len(actions)-1] == 'Salir' and actions[len(actions)-2] == 'Salir') or (actions[len(actions)-1] == '2' and actions[len(actions)-2] == '2')):
                    print('El rollo de siempre, ¿no?') #https://www.youtube.com/watch?v=ULJhS7QdksM
                #Llamamos a la función salir, que está en esta misma clase
                go_out(player)
            elif(answer == 'Comer' or answer == '3'):
                if((actions[len(actions)-1] == 'Comer' and actions[len(actions)-2] == 'Comer') or (actions[len(actions)-1] == '3' and actions[len(actions)-2] == '3')):
                    print('¿Te crees Álex?')
                #Llamamos a la función comer, que en este caso se encuentra en la clase jugador
                player.eat()
            elif(answer == 'Dormir' or answer == '4'):
                if((actions[len(actions)-1] == 'Dormir' and actions[len(actions)-2] == 'Dormir') or (actions[len(actions)-1] == '4' and actions[len(actions)-2] == '4')):
                    print('¿Piensas hacer algo con tu vida en algún momento?')
                #Este método también se encuentra en la clase jugador
                player.sleep()
 
            #La única forma de morir es si el sueño se pasa de 100 o baja de 0
            if(player.sleepiness >= 100 or player.sleepiness < 0):
                player.alive = False
                print('Has perdido.')
 
            #Al final de cada iteración imprimimos el estado del jugador
            status(player)
 
        #En cada iteración sacamos un número aleatorio, si es 16 pierdes
        if(random.randint(0, 20) == 16 and player.alive == True):
            player.alive = False
            print('Has perdido, la vida es dura, asúmelo.')