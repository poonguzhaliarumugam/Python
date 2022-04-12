def display_board(val):
    l1="+-------"*3+"+"
    print(l1)
    l2="|       "*3+"|"
    print(l2)
    print("|  ",val[1],"  "+"|  ",val[2],"  "+"|  ",val[3],"  "+"|")
    print(l2)
    print(l1)
    print(l2)
    print("|  ",val[4],"  "+"|  ",val[5],"  "+"|  ",val[6],"  "+"|")
    print(l2)
    print(l1)
    print(l2)
    print("|  ",val[7],"  "+"|  ",val[8],"  "+"|  ",val[9],"  "+"|")
    print(l2)
    print(l1)

def game_result(val,move):
    comp_win=False
    player_win=False
    global end_game
    if move==1 or move==7 or move==9 or move==3:
       if (move==1 or move==7) and val[move]==val[move+1] and val[move+1]==val[move+2]:#[123][789]
          if val[move]=='x':
             comp_win=True
          elif val[move]=='o':
             player_win=True 
       elif move==1 or move==9:
            if val[1]==val[5] and val[1]==val[9]:#[159][951]
               comp_win=True    
            elif move==7 or move==3:
                 if val[7]==val[5] and val[7]==val[3]:#[753][357]
                    comp_win=True
       if move==1 or move==3 or move==9 or move==7:
          if move==1 or move==3:
             if val[move]==val[move+3] and val[move]==val[move+6]:#[147][369]
                if val[move]=='x':
                   comp_win=True
                elif val[move]=='o':
                   player_win=True  
          if move==7 or move==9:
             if val[move]==val[move-3] and val[move]==val[move-6]:#[741][963]  
                if val[move]=='x':
                   comp_win=True
                elif val[move]=='o':
                   player_win=True      
    if move==2 or move==8:
       if val[move]==val[move-1] and val[move]==val[move+1]:#[123][789]
          if val[move]=='x':
             comp_win=True
          elif val[move]=='o':
             player_win=True        
       if val[5]==val[2] and val[5]==val[8]:#[258][852]
          comp_win=True
    if move==4 or move==6:
       if val[move]==val[move-3] and val[move]==val[move+3]:#[147][369]
          if val[move]=='x':
             comp_win=True
          elif val[move]=='o':
             player_win=True 
       if val[5]==val[4] and val[5]==val[6]:#[456][654]
           comp_win=True

    if comp_win:
       print("Computer wins!")
       end_game=True
    elif player_win:          
       print("You win!")
       end_game=True
    return   

    
def playermove(val):
    
    player_move=int(input("Enter your move: "))
    move=player_move

    if player_move in range(1,10):  
       if val[player_move]=='x' or val[player_move]=='o':
          print("already occupied, please enter different move") 
          playermove(val)
       if val[player_move]==player_move:
          val[player_move]='o'
          game_result(val,move)
          return

    if player_move < 1 or player_move >9:
       print("Invalid move, please enter between 1 to 9")
       print("entered invalid: ",player_move)
       playermove(val)   
       
def comp_turn(val):
    
    from random import randrange
    for i in range(9):
        num=randrange(9)
    
        if num==0 or num > 9:
           continue
        if num > 0 and num < 10:
           if val[num]=='x' or val[num]=='o':
              continue
           if val[num]==num:
              val[num]='x'
              game_result(val,num)
              return

               
       
        
val={1:1,2:2,3:3,4:4,5:'x',6:6,7:7,8:8,9:9}
display_board(val)  #to display the game board
end_game=False
move=""
while not end_game:
   playermove(val)
   display_board(val)
   comp_turn(val)
   display_board(val)
else:
   print("Game Over")   
