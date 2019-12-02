from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from agent import Humano, Construccion, Muro, Torniquete
import math
from agent import GRID_INICIAL_X, GRID_FINAL_X, GRID_INICIAL_Y, GRID_FINAL_Y
YMURO_TORNIQUETES = GRID_FINAL_Y - math.floor(GRID_FINAL_Y * .3)
YMURO_TREN = GRID_FINAL_Y - math.floor(GRID_FINAL_Y * .7)
XTORNIQUETE_IZQ = math.floor(GRID_FINAL_X * .3)
XTORNIQUETE_CTR = math.floor(GRID_FINAL_X * .5)
XTORNIQUETE_DER = math.floor(GRID_FINAL_X * .7)

class miModelo(Model):
    def __init__(self,N_humanos):
        self.running = True
        self.schedule = RandomActivation(self)        
        self.grid = MultiGrid(GRID_FINAL_X,GRID_FINAL_Y,False)   

        pintarTorniquetes(self) #Dibuja los torniquetes
        pintarMuros(self);  #Dibuja todos los muros
        contador = 0
        while contador < N_humanos:
            pos_x = self.random.randint(GRID_INICIAL_X + 1,GRID_FINAL_X - 2) #Posicion x del humano
            pos_y = self.random.randint(GRID_INICIAL_Y + 1 ,GRID_FINAL_Y - 2) #Posicion y del humano
            if pos_y != YMURO_TORNIQUETES and pos_y !=  YMURO_TREN:
                contador+=1
                a = Humano(contador,self,(pos_x,pos_y)) #Creacion del humano
                self.schedule.add(a)
                self.grid.place_agent(a, a.pos) #Coloca  en la posicion creada

            


            
    def step(self):
        self.schedule.step()
        if self.schedule.get_agent_count()<2:
            self.running = False
        print("---- End of tick ----")

def pintarMuros(modelo):
    pintarMuro(modelo, GRID_INICIAL_X, GRID_FINAL_X, GRID_FINAL_Y - 1, GRID_FINAL_Y - 1) #Superior
    pintarMuro(modelo, GRID_INICIAL_X, GRID_FINAL_X, GRID_INICIAL_Y,  GRID_INICIAL_Y) #Inferior
    pintarMuro(modelo, GRID_INICIAL_X, GRID_INICIAL_X, GRID_INICIAL_Y+1, GRID_FINAL_Y-1) #Izquierda
    pintarMuro(modelo, GRID_FINAL_X -1, GRID_FINAL_X -1, GRID_INICIAL_Y, GRID_FINAL_Y-1) #Derecha
    pintarMuro(modelo, GRID_INICIAL_X, GRID_FINAL_X, YMURO_TORNIQUETES ,  YMURO_TORNIQUETES ) #Torniquetes .3 de distancia
    pintarMuro(modelo, GRID_INICIAL_X, GRID_FINAL_X, YMURO_TREN ,  YMURO_TREN ) #Tren .7 de distancia
    
def pintarMuro(modelo, inicial_x, final_x, inicial_y, final_y):
    if inicial_y == final_y: #horizontal
        for i in range(inicial_x,final_x):
            a = Muro(i,modelo,(i,inicial_y), False)
            modelo.schedule.add(a)
            modelo.grid.place_agent(a, a.pos)
            
    elif inicial_x == final_x: #vertical
        for i in range(inicial_y,final_y):
            a = Muro(i,modelo,(inicial_x,i),False)
            modelo.schedule.add(a)
            modelo.grid.place_agent(a, a.pos)
    else:
        print("Algo Salio Mal")

def pintarTorniquetes(modelo):
    pintarTorniquete(1,modelo,XTORNIQUETE_DER,YMURO_TORNIQUETES)
    pintarTorniquete(1,modelo,XTORNIQUETE_DER+1,YMURO_TORNIQUETES)
    pintarTorniquete(1,modelo,XTORNIQUETE_CTR,YMURO_TORNIQUETES)
    pintarTorniquete(1,modelo,XTORNIQUETE_CTR+1,YMURO_TORNIQUETES)
    pintarTorniquete(1,modelo,XTORNIQUETE_CTR-1,YMURO_TORNIQUETES)
    pintarTorniquete(1,modelo,XTORNIQUETE_IZQ,YMURO_TORNIQUETES)
    pintarTorniquete(1,modelo,XTORNIQUETE_IZQ-1,YMURO_TORNIQUETES)

def pintarTorniquete(i,modelo, pos_x,pos_y):
    a = Torniquete(i,modelo,(pos_x,pos_y),True)
    print(a.pos)
    modelo.schedule.add(a)
    modelo.grid.place_agent(a, a.pos)
    

    

    

   