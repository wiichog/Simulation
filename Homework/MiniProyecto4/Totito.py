import random
import copy
import numpy as th

board = [
  [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ],
  [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ]
]

p1_token = 1
p2_token = -1
draw_token = 0


def slice_winner(state_slice):
  slice_size = len(state_slice)
  sums = [sum(row) for row in state_slice]
  sums.extend([sum([row[i] for row in state_slice]) for i in range(slice_size)])

  if (p1_token * slice_size) in sums:
    return p1_token
  elif (p2_token * slice_size) in sums:
    return p2_token

  return 0


def winner(state):
  for state_slice in state:
    winner_in_slice = slice_winner(state_slice)
    if winner_in_slice != draw_token:
      return winner_in_slice

  state_size = len(state)

  for i in range(state_size):
    state_slice = []
    for j in range(state_size):
      state_slice.append([state[j][i][k] for k in range(state_size)])

    winner_in_slice = slice_winner(state_slice)

    if winner_in_slice != draw_token:
      return winner_in_slice

  diagonals = [0, 0, 0, 0]
  for i in range(state_size):
    diagonals[0] += state[i][i][i]
    diagonals[1] += state[state_size - 1 - i][i][i]
    diagonals[2] += state[i][state_size - 1 - i][i]
    diagonals[3] += state[state_size - 1 - i][state_size - 1 - i][i]

  if (p1_token * state_size) in diagonals:
    return p1_token

  elif (p2_token * state_size) in diagonals:
    return p2_token

  return draw_token


def str_token(cell):
  if cell == p1_token:
    return "X"
  elif cell == p2_token:
    return "O"

  return "."


def draw_board(state):
  result = ""
  state_size = len(state)
  for y in range(state_size):
    for z in range(state_size):
      for x in range(state_size):
        result += str_token(state[x][y][z]) + " "
      result += "\t"
    result += "\n"
  return result



player_1_turn = True
occupied_position = []

def MonteCarlo(Tablero,TurnoPersona,NumeroRepeticiones,contador,Posicion):
     #Aqui guardaremos los movimientos que se hicieron
    for i in range(NumeroRepeticiones):
        x = random.randint(0,3)#X para Computadora
        y = random.randint(0,3)#Y para Computadora
        z = random.randint(0,3)#Z para Computadora
        c = 128
        posicionGanadora = [x,y,z]#la movida la guardamos en un array
        posicionToString = str(x)+","+str(y)+","+str(z)#necesitamos esto para identificar la movida
        player_1_turn = False #para que la maquina haga su movimiento
        first_turn = True
        Temporal = copy.deepcopy(TurnoPersona)
        TableroCompu = copy.deepcopy(Tablero)
        while (posicionGanadora in Temporal):
            contador = contador + 1
            x = random.randint(0,3)# X simulacion para computadora
            y = random.randint(0,3)# Y para Simulacion para computadora
            z = random.randint(0,3)#Z para simulacion
            posicionGanadora = [x,y,z]#Lo guardamos en un array
            posicionToString =  str(x)+","+str(y)+","+str(z)#Lo pasamos a una cadena para ser identificador
            if(posicionToString not in Posicion):#si la posicion generada no esta en el diccionario
                Posicion[posicionToString] = 0#ponemos un 0
            while(winner(TableroCompu) == draw_token and c > 0):#mientras no haya ganador y se tenga un c mayor a cero
                if player_1_turn and not(first_turn):
                    [x,y,z] = th.random.randint(4, size = 3) #hacemos un vector de randoms
                elif not(first_turn):
                    [x,y,z] = th.random.randint(4, size = 3)
                if(TableroCompu[x][y][z]==draw_token):#si esta desocupada la posicion
                    first_turn = False#cambiamos de turno
                    Temporal.append([x,y,z])#Guardamos la posicion
                    TableroCompu[x][y][z] = 1 if player_1_turn else -1#dibujamos 1 si es el turno del jugador 1 y -1 si es del turno del jugador 3
                    player_1_turn = not player_1_turn#cambiamos de turno
                c += -1#restamos 1 a C
            if winner(TableroCompu) == 1:
                Posicion[posicionToString] += 1#Si el juego peirde le restamos uno
            elif winner(TableroCompu) == -1:
                Posicion[posicionToString] += - 1#si el juego gana le sumamos uno
            else:
                Posicion[posicionToString] += 0#si empata no hacemos nada
            Temporal = []
            TableroCompu = []
    MejorBusqueda =  max(Posicion, key=lambda k: Posicion[k]) #buscamos el mayor de sumatorioa
    Partir = map(int, MejorBusqueda.split(','))#hacemos un split para devolver solo la x y z
    print MejorBusqueda  
    print "juego de veces", contador
    return Partir

player_1_turn = True
contador = 0
Posicion = {}
while winner(board) == draw_token:
  # Print board state
  print ""
  print "Board:"
  print draw_board(board)
  print ""

  # Print 
  print "Player %s turn:" % (1 if player_1_turn else 2)

  if player_1_turn:
      x = int(raw_input("x: "))
      y = int(raw_input("y: "))
      z = int(raw_input("z: "))
  else:
      temp_board = copy.deepcopy(board)
      [x, y, z] = MonteCarlo(temp_board, occupied_position, 10000,contador,Posicion)
  if board[x][y][z] == draw_token:
      occupied_position.append([x,y,z])#regresamos la que mejor tuvo y la imprimimos
      board[x][y][z] = 1 if player_1_turn else -1
      player_1_turn = not player_1_turn
  else:
    print ""
    print "ERROR: occupied position, please retry in a new position"
    print ""

print "Player %s is the winner!" % (1 if winner(board) == 1 else 2)
