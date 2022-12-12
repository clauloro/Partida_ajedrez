import chess #utilizo la tabla de ajedrez de la biblioteca "chess"
board = chess.Board()
print(board)

def partida_ajedrez():  

    movimiento = 0

    Empezar = input ("Empezar |S| si, |N| no: ")
    if Empezar == "s" :
        Opcion=True
        f = open("Resgistro_De_Partida.txt","w")
    else:
        print("adiooooos")
        
    while Opcion:
        try:
            Movimientos_legales = board.legal_moves
            jugada=input("jugada:")
            movimiento+=1
            if movimiento ==2:
                f.write("\n")
                movimiento=0
            if jugada == "back":
                board.pop()
            if jugada=="exit":
                f.close
                Opcion = False
            print(board)
            if board.is_checkmate():
                print("---------\nJAQUE MATE \n --------")
                pregunta = input ("Quieres repetir la partida? |S| si,|N| no:")
                if pregunta == "s":
                    board = chess.Board()    
                elif pregunta == "n":
                    print("vale hasta la proxima")
                    f.close()
                else:
                    print("opcion no valida")
                 #si se escribe se reinicia el juego
            if jugada == "restart":
                board = chess.Board()
                print(board) 
        except:
            print("\nJugada invalida\n")
            print("\n{}".format(board))
            