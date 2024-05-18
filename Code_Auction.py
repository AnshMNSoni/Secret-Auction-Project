# Secret Auction Program:

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

from rich.console import Console

print("Welcome to the secret Auction program")

dic = {}
while True:
    user = input("What's your name?: ")
    bid = int(input("What's your Bid?: $"))
    
    dic[user] = bid
    
    highest = 0
    if (bid >=  highest):
        highest = bid
        name = user
    
    y_n = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    
    if (y_n == 'no'):
        console = Console()
        console.clear()
        print(logo)
        
        print(f"The winner is {name} with a bid of ${highest}")
        break
    else:
        console = Console()
        console.clear()
        print(logo)