from enum import Enum
from collections import deque

class PieceType(Enum):
        X='X'
        O='O'
class PlayingPiece:
       def __init__(self,piece_type):
             self.piece_type=piece_type
class Board:
      
      def __init__(self,size):
          self.size=size
          self.board=[[None]*size for _ in range(size)]
          
      def addPiece(self,row,col,playingPiece):
            if self.board[row][col]:
                 return False
            self.board[row][col]=playingPiece
            return True
            
      def getFreeCells(self):
             ans=[]
             
             for i in range(self.size):
                  for j in range(self.size):
                       if not self.board[i][j]:
                                ans.append((i,j))
             return ans
             
      def printBoard(self):
          
          for row in range(self.size):
               elements_row=[]
               for col in range(self.size):
                    if not self.board[row][col]:
                         elements_row.append(' ')
                    else:
                         elements_row.append(self.board[row][col].piece_type.name)
               print(' | '.join(elements_row))
               if row!=self.size-1:
                    print('-'*12)
                    
      def is_there_winner(self,row,col,piece_type):
          
          if all(self.board[row][c] and self.board[row][c].piece_type==piece_type for c in range(self.size)):
                    return True
          if all(self.board[r][col] and self.board[r][col].piece_type==piece_type for r in range(self.size)):
                    return True
          if row==col and all(self.board[i][i] and self.board[i][i].piece_type==piece_type for i in range(self.size)):
                   return True
          if (row+col==self.size-1) and all(self.board[i][self.size-1-i] and self.board[i][self.size-1-i].piece_type==piece_type for i in range(self.size)):
                   return True
          return False
     
               
class Player:
      
      def __init__(self,name,playing_piece):
          self.name=name
          self.playing_piece=playing_piece
class Game:
        
        def __init__(self):
            self.players=deque()
            self.board=Board(3)
            self.initializeGame()
        def initializeGame(self):
            self.players.append(Player('Player1',PlayingPiece(PieceType.X)))
            self.players.append(Player('Player2',PlayingPiece(PieceType.O)))
        
        def current_player(self):
            
            return self.players[0]
            
        def place_move(self,row,col):
            
            return self.board.addPiece(row,col,self.current_player().playing_piece)
        def check_winner(self,row,col):
            return self.board.is_there_winner(
            row, col, self.current_player().playing_piece.piece_type
            )
        def rotate(self):
            self.players.append(self.players.popleft())
def main():
     game=Game()
     while True:
            
            game.board.printBoard()
            playerTurn=game.current_player()
            
            raw = input(f"{playerTurn.name}, enter row,col (0–{game.board.size-1}): ")

            parts = raw.split(',')
            if len(parts) != 2:
                    print("Invalid format. Use: row,col  (e.g. 1,2)")
                    continue
            try:
                    row = int(parts[0].strip())
                    col = int(parts[1].strip())
            except ValueError:
                        print("Please enter two integers separated by a comma.")
                        continue
            
            if not game.place_move(row,col):
                    print("That cell is already occupied. Try a different one.")
                    continue
            if game.check_winner(row,col):
                    game.board.printBoard()
                    print(f"{playerTurn.name} wins!")
                    break
            if len(game.board.getFreeCells())==0:
                    game.board.printBoard()
                    print("Tie!")
                    break
            
            
            game.rotate()


if __name__ == "__main__":
    main()
            
            
        
        
