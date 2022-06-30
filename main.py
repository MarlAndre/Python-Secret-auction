from art import logo
from replit import clear
print(logo)

auction = {}
finished_program = False

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not finished_program:
  name = input("What's your name?\n")
  amount = int(input("How much $ do you want to bid?\n"))
  auction[name] = amount  
  continue_bidding = input("Is there any other bidders? 'y' for yes, 'n' for no.\n")  
  if continue_bidding == "n":
    finished_program = True
    highest_bidder(auction)
  elif continue_bidding == "y":
    clear()
   
    
  
