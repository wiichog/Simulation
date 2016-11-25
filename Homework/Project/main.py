# -*- coding: utf-8 -*- 
"""
Created on Thu Nov 24 16:30:29 2016

@author: wiichog
"""
import random
from copy import deepcopy
import thread


def make_user_move(board):
    try:    
        valid_move = False
        while not valid_move:
            col = input("What col would you like to move to (1-7):")#se pregunta por la columna
            for row in range (6,0,-1):
                if (1 <= row <= 6) and (1 <= col <= 7) and (board[row-1][col-1] == " "):#verificamos que row y col esten dentro del tablero y que la casilla se encuentre vacia
                    board[row-1][col-1] = 'X'#Se pone en la casilla vacia la X del jugador humano
                    valid_move = True#se rompe el ciclo
                    break
            else:
                print "Sorry, invalid square. Please try again!\n"#se lanza error si no es valido
    
    except NameError:
        print "Only numbers are allowed."# en tal caso no ingrese un numero
    except IndexError:
        print "You can only select columns from (1-7), and rows from (1-6)."


def CleanBoard(board):
    board = [ [ " ", " ", " ", " ", " ", " "," ", " "], [ " ", " ", " ", " ", " "," ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "] ]
    return board#simplemente el board que venia de parametro lo seteamos como uno nuevo para limpiarlo

def winner(board):
# Check rows for winner
    for row in range(6):
        for col in range(3):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] ==\
                board[row][col + 3]) and (board[row][col] != " "):
                return board[row][col]

# Check columns for winner
    for col in range(6):
        for row in range(3):
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] ==\
                board[row + 3][col]) and (board[row][col] != " "):
                return board[row][col]

# Check diagonal (top-left to bottom-right) for winner

    for row in range(3):
        for col in range(4):
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] ==\
                board[row + 3][col + 3]) and (board[row][col] != " "):
                return board[row][col]


# Check diagonal (bottom-left to top-right) for winner

    for row in range(5, 2, -1):
        for col in range(3):
            if (board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] ==\
                board[row - 3][col + 3]) and (board[row][col] != " "):
                return board[row][col]
# No winner: return the empty string
                return ""

def display_board(board):#se imprimie todo el board
    print "   1   2   3   4    5   6   7"
    print "1: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | " + board[0][3] + " | " + board[0][4] + " | " + board[0][5] + " | " + board[0][6] + " | " + board[0][7]
    print "  ---+---+---+---+---+---+---"
    print "2: " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | " + board[1][3] + " | " + board[1][4] + " | " + board[1][5] + " | " + board [1][6] + " | " + board [1][7]  
    print "  ---+---+---+---+---+---+---+"
    print "3: " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | " + board[2][3] + " | " + board [2][4] + " | " + board [2][5] + " | " + board [2][6] + " | " + board [2][7]
    print "  ---+---+---+---+---+---+---+"
    print "4: " + board[3][0] + " | " + board[3][1] + " | " + board[3][2] + " | " + board[3][3] + " | " + board [3][4] + " | " + board [3][5] + " | " + board [3][6] + " | " + board [3][7]
    print "  ---+---+---+---+---+---+---+"
    print "5: " + board[4][0] + " | " + board[4][1] + " | " + board[4][2] + " | " + board[4][3] + " | " + board [4][4] + " | " + board [4][5] + " | " + board [4][6] + " | " + board [4][7]
    print "  ---+---+---+---+---+---+---+"
    print "6: " + board[5][0] + " | " + board[5][1] + " | " + board[5][2] + " | " + board[5][3] + " | " + board [5][4] + " | " + board [5][5] + " | " + board [5][6] + " | " + board [5][7]
    print


def MakeMove(board,Simbolo,col):#se tiene como parametro un tablero, un simbolo para saber si es humano o computadora y la columna en donde se dibujara el simbolo
    try:    
        valid_move = False
        while not valid_move:
            for row in range (6,0,-1):
                if (1 <= row <= 6) and (1 <= col <= 7) and (board[row-1][col-1] == " "):#verificamos que row y col esten dentro del tablero y que la casilla se encuentre vacia
                    board[row-1][col-1] = Simbolo#dibujamos el simbolo en la casilla vacia
                    valid_move = True
                    break
                else:#en tal caso la columna ya se encuentra llena
                    col = random.randint(1,7)#se genera un nuevo random
                    valid_move = True
    except NameError:
        print "Only numbers are allowed."
    except IndexError:
        print "You can only select columns from (1-7), and rows from (1-6)."
        
def MonteCarlo(ttt_board,Iteraciones,free_cells,users_turn,Contador,Opcion):#traemos un tablero, las iteraciones, el numero libre de celdas, de quien es el primer turno y opcion es la columna que queremos ver si es factible o no
    MakeMove(ttt_board,'O',Opcion)#mandamos a dibujar la posible columna buena
    free_cells -= 1#restamos una celda libre
    contador = 0#inicializamos un contador
    for i in range(Iteraciones):#repetiremos el ciclo la cantidad de iteraciones que el usuario quizo
        while not winner(ttt_board) and (free_cells > 0):#mientras no haya ganador y haya celdas vacias
            if users_turn:#turno del humano
                Columna = random.randint(1,7)#tiramos un random
                MakeMove(ttt_board,'X',Columna)#mandamos a dibujar ese random
                users_turn = not users_turn#cambbiamos de turno
            else:#turno computadora
                Columna = random.randint(1,7)#genramos un random
                MakeMove(ttt_board,'O',Columna)#lo mandamos a dibujar
                users_turn = not users_turn#cambiamos de turno
            free_cells -= 1# ya que se hizo una jugada restamos una celda
        if (winner(ttt_board) == 'X'):#en tal caso el humano gane
            ttt_board = CleanBoard(ttt_board)#limpiamos el tablero
            free_cells = 42#volvemos a liberar todas las celas
            users_turn = True#decimos que el humano sera el primero
            Contador = Contador - 1#restamos 1 al contador ya que el humano gano
        elif (winner(ttt_board) == 'O'):#si gana la computadora
            ttt_board = CleanBoard(ttt_board)#limpiamos el board
            free_cells = 42#volvemos a liberar todas las celdas
            users_turn = True#el humano es el primer jugador
            Contador = Contador + 1#aumentamos en 1 por que la computadora gano
        else:#empate no se hace nada
            ttt_board = CleanBoard(ttt_board)#limpiamos el board
            free_cells = 42#liberamos las celdas
            users_turn = True#humano primer jugador
    return Contador#retornamos el contador por que este llevo cuantas veces gano el humano y cuantas veces gano la computadora


def JugadorComputadora(ttt_board,Iteraciones,free_cells,users_turn,Contador):#recibimos un board, el numero de iteraciones, el numero de celdas libres  y un contador
    Columna = []#aqui guardaremos todas las columnas que podrias ser las mejores
    Numero = []#aqui guardaremos sus resultados de las simulaciones
    Finalisimo = 0#numero que sera el mejor de los resultados
    for i in range(Iteraciones):#se repetira las veces de las iteraciones
        Posible = random.randint(1,7)#generamos una posible columna
        Resultado = thread.start_new_thread( MonteCarlo, (ttt_board,Iteraciones,free_cells,users_turn,Contador,Posible, ) )#un thread nos devolvera un numero el cual significa cuantas veces gano la computadora y cuantas veces gano el humano
        Columna.append(Posible)#guardamos en el array la colmna generada
        Numero.append(Resultado)#guardamos en el array su resultado de la simulacion
    ResultadoFinal = max(Numero)#obtenemos el mejor de la simulacion
    for i in range(len(Numero)):#recorremos este array
        if Numero[i]==ResultadoFinal:#buscaremos el index del mejor numero
            Finalisimo = Columna[i]#cuando encontramos el index en numero entonces el mejor de los resultados tomara la mejor columna ya que se encuentran en la misma posicion pero diferentes arrays
    ttt_board = CleanBoard(ttt_board)#limpiamos el board
    return Finalisimo#devolvemos el mejor
#board principal
ttt_board = [ [ " ", " ", " ", " ", " ", " "," ", " "], [ " ", " ", " ", " ", " "," ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "] ]
#board solo de respaldo
BackUp = [ [ " ", " ", " ", " ", " ", " "," ", " "], [ " ", " ", " ", " ", " "," ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "] ]
free_cells = 42#numero de celdas libres
Contador = 0#contador en 0
users_turn = True#humano tendra primer turno
Iteraciones = input("Ingrese Numero de Iteraciones ")#se preguntan cuantas iteraciones se quieren hacer
while not winner(ttt_board) and (free_cells > 0):#mientras no haya ganador y el numero de celdas sea mayor
    display_board(ttt_board)#mostramos el board
    if users_turn:#turno del humano
        make_user_move(ttt_board)#preguntamos que quiere hacer
        BackUp = deepcopy(ttt_board)#hacemos un deepcopy del board original ya que ttt_board se utilizara para las simulaciones
        users_turn = not users_turn#cambiamos de turno
    else:#turno de la computadora
        Numero = JugadorComputadora(ttt_board,Iteraciones,42,True,0)#JugadorComputadora nos devolvera la mejor columna
        MakeMove(BackUp,'O',Numero)#hacemos el movimiento pero este movimiento lo vamos a hacer en el back up ya que el original esta lleno por las simulaciones
        ttt_board = deepcopy(BackUp)#ahora le caemos encima al original con su copia pero esta copia ya tiene el nuevo movimiento
        users_turn = not users_turn#cambiamos de turno
    free_cells -= 1#restamos una celda
display_board(ttt_board)#mostramos el board
if (winner(ttt_board) == 'X'):#si gana el humano entonces se tendra que agregar al muro de la fama
    print "You Won!"#felicitaciones
    print "Your name will now be added to the Hall of Fame!"
    hall_of_fame = open("HallOfFame.txt", 'a')#abrimos un archivo de texto
    name = raw_input("Enter your name: ")#pedimos su nombre
    hall_of_fame.write(name+ '\n')#escribimos su nombre en el archivo de texto
    print "Your name has been added to the Hall of Fame!"#se agrego
    hall_of_fame.close()#se cierra el archivo
    print "\nGAME OVER"
elif (winner(ttt_board) == 'O'):#si la computadora gano entonces solo se dice que gano la computadora
    print "The Computer Won!"
    print "\nGAME OVER"
else:#se muestra en tal caso haya un empate
    print "Stalemate!"
    print "\nGAME OVER \n"

