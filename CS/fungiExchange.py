# Author: Jacob Beckley
# Date: 4-22-2019
# CSCI 141 Assignment 2

#Determine how many Shiitake mushrooms were found
shiitakeFound = input("How many Shiitake did you find? ")
shiitakeFound = int(shiitakeFound)

#Determine how many Portobello mushrooms were found
portobelloFound = input("How many Portobello did you find? ")
portobelloFound = int(portobelloFound)

#Story narrative
story = "";
print(story)

#Trade
shiitakeTrade = input("How many Shiitakes are you willing to trade? ")
shiitakeTrade = int(shiitakeTrade)

portobelloTrade = input("How many Portobellos are you willing to trade? ")
portobelloTrade = int(portobelloTrade)

if shiitakeTrade > shiitakeFound or portobelloTrade > portobelloFound:
    print("Trade not valid")
elif shiitakeTrade + portobelloTrade == 0:
    print("Trade not valid")
else:
    if shiitakeTrade < 10:
        if portobelloTrade < 5:
            rubies = 2 * shiitakeTrade
            print("I'll offer you", rubies, "rubies")
        else:
            rubies = 3 * portobelloTrade
            print("I'll offer you", rubies, "rubies")
    else:
        if shiitakeTrade % 12 == 0 and shiitakeTrade % 24 != 0:
            if portobelloTrade >= 20:
                rubies = 4 * portobelloTrade
                print("I'll offer you", rubies, "rubies")
            else:
                rubies = portobelloTrade
                print("I'll offer you", rubies, "rubies")
        else:
                rubies = 5 * shiitakeTrade
                print("I'll offer you", rubies, "rubies")

    response = input("Will you accept the offer? (Y/N) ")
    if response == "Y" or response == "y" or response == "Yes" or response == "yes":
        
        shiitakeCurrent = shiitakeFound - shiitakeTrade
        portobelloCurrent = portobelloFound - portobelloTrade
    else:
        print("The offer was not accepted")
        shiitakeCurrent = shiitakeFound
        portobelloCurrent = portobelloFound
        rubies = 0
    print("You now have", rubies, "rubies,", shiitakeCurrent, "Shiitake mushrooms, and", portobelloCurrent, "Portobello mushrooms")
