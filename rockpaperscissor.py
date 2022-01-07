import sys
class Score:
  win = 0
  loss = 0
  ties = 0
  resp = " "

p1 = Score()
p2 = Score()

elements1 = {
  "p":"paper",
  "st":"stone",
  "sc":"scissor"
}

while True:
  print("Player One:")
  print(f"Win = {p1.win},Loss = {p1.loss},Ties = {p1.ties}")
  print("Player Two:")
  print(f"Win = {p2.win},Loss = {p2.loss},Ties = {p2.ties}")
  p1.resp = input("Enter Player One:")
  p2.resp = input("Enter Player Two:")

  if(p1.resp=="p" and p2.resp=="sc"):
    print("Player 2 won")
    p2.win+=1
    p1.loss+=1

  elif(p1.resp=="p" and p2.resp=="st"):
    print("Player 1 won")
    p1.win+=1
    p2.loss+=1

  elif(p1.resp=="p" and p2.resp=="p"):
    print("tie ")
    p2.ties+=1
    p1.ties+=1

  elif(p1.resp=="st" and p2.resp=="sc"):
    print("Player 1 won")
    p1.win+=1
    p2.loss+=1

  elif(p1.resp=="st" and p2.resp=="p"):
    print("Player 2 won")
    p2.win+=1
    p1.loss+=1

  elif(p1.resp=="st" and p2.resp=="st"):
    print("tie")
    p2.ties+=1
    p1.ties+=1

  elif(p1.resp=="sc" and p2.resp=="sc"):
    print("tie")
    p2.ties+=1
    p1.ties+=1

  elif(p1.resp=="sc" and p2.resp=="p"):
    print("Player 1 won")
    p1.win+=1
    p2.loss+=1
    
  elif(p1.resp=="sc" and p2.resp=="st"):
    print("Player 2 won")
    p2.win+=1
    p1.loss+=1

  else:
    print("Flase response")

    
  
  


  
  
