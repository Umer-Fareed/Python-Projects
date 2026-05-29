# first price sealed bid auction
from clearscreen import clear
from art import logo
print(logo)


bids= {}
bidding_finish = False

def find_highest_bidder(bidding_record):
    #{"angla" :232,
    #   "james": 3443
    # }
    for bidder in bidding_record:
        heighset_bid = 0
        bid_amount = bidding_record[bidder]
        if bid_amount>heighset_bid:
            heighset_bid=bid_amount
            winner = bidder
    print(f"the winner is {winner} withe a bid of {heighset_bid}")

while not bidding_finish:
    name = input("What is your name?:  ")
    price = int(input("What is your bid?:  $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'No'.\n ")
    if should_continue == "no":
        bidding_finish = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()

