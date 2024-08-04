from replit import clear

print('''
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
''')

auction={}
name=input("Enter your name: ")
bid_amount=input("Enter your amount in $: ")
auction={name:bid_amount,}
bidding=input('Do you want to add more bidding: Type "Yes" or "No": ')
clear()
while bidding=="Yes":
    name=input("Enter your name: ")
    bid_amount=input("Enter your amount in $: ")
    bidding=input('Do you want to add more bidding: Type "Yes" or "No"')
    clear()
    auction[name]=bid_amount
print(auction)
Keymax = max(auction, key= lambda x: auction[x])
print(f"The highest bid is of {Keymax}")