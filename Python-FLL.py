from hub import port
import runloop
import motor
import motor_pair
import force_sensor
import time

#Definição de Funções
def DefinirMotores(motoresquerdo, motordireito, sensor):
    motor_pair.pair(motor_pair.PAIR_1, motoresquerdo, motordireito)
    force_sensor.force(sensor)

def Esperar(espera: int):
    time.sleep_ms(espera)

def AndarTanque(esquerdo: int, direito: int):
    motor_pair.move_tank(motor_pair.PAIR_1, esquerdo, direito)

def Andar(velocidadeesquerdo: int, velocidadedireito: int, tempo: int):
    motor_pair.move_tank_for_time(motor_pair.PAIR_1, velocidadeesquerdo, velocidadedireito, tempo)

def Direita90():
    motor_pair.move_tank_for_time(motor_pair.PAIR_1, 500, 0, 670)

def Esquerda90():
    motor_pair.move_tank_for_time(motor_pair.PAIR_1, 0, 500, 670)


async def main():
   #Variaveis
   toque = 0

   #Iniciação
   DefinirMotores(port.B, port.D, port.A)
   #As definições de portas podem variar de acordo com as portas conectadas no Spike.
   
   
   #Movimentos/Lançamentos:
   Andar(1000, 1000, 1500)
   Esperar(1500)
   motor_pair.stop(motor_pair.PAIR_1)
   motor.run(port.F, 500)
   Esperar(500)
   motor.stop(port.F)
   Andar(-1000, -1000, 1500)
   
   while True: #Laço de repetição
    
    if force_sensor.pressed(port.A) == True: #Condicional
        toque += 1
    
    if (toque >= 1):
        Esperar(1000)
        Andar(500,500,1000)
        Esperar(1000)
        Andar(-500,-500,600)
        Esperar(600)
        Andar(550, 400, 1000)
        Esperar(1000)
        Andar(500,500, 1000)
        Esperar(1000)
        Andar(300, 500,1000)
        Esperar(100)
        Andar(960,1000,6000)
        exit

 
        
runloop.run(main())
