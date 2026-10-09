import time
import platform
import os
import sys

while True:

    print("Copyright 2026 Florescent Games")
    time.sleep(7)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)

    pizzaSlices = float(input("Pizza Slices:")) # float allows "1.2" or "3.7" and things like that
    banana = float(input("bananas:"))
    tomatoes = float(input("tomatoes (cherry tomatoes, not big ones.):"))
    cakeSlices = float(input("Cake Slices:"))
    mysteriousSubstance = float(input("Mysterious Substance:"))
    ouncesOfBlood = float(input("OZ of Blood:"))
    floppyDiscs = float(input("Floppy Discs:"))
    ornge = float(input("ornges:"))
    milkCartons = float(input("Milk Cartons:"))
    computerProcessers = float(input("CPUs:"))
    dinoNuggies = float(input("Dino Nuggies:"))
    macNCheeseBoxes = float(input("Boxes of Mac N' Cheese:"))
    smolPizza = float(input("Smol Pizzas:"))
    miniPretzels = float(input("Mini Pretzels:"))

    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)

    totalFood = pizzaSlices + banana + tomatoes + cakeSlices + mysteriousSubstance + ornge + milkCartons + dinoNuggies + macNCheeseBoxes + smolPizza

    print("The plate has", totalFood, "food items on it.")
    if pizzaSlices < 3:
        print("Less Pizza Ending:There are less than 3 pizza slices on the plate.") # Italia
    elif pizzaSlices > 3:
        print("Implode.")
    elif pizzaSlices < 0:
        print("Fraud.")
    if banana > 1:
        print("Bad Ending:There is too much Potassium, you will get Acute Radiation Poisoning and die.") # p o t a s s i u m
    elif banana < 0:
        print("Fraud.")
    if tomatoes > 6:
        print("Good Ending: The more the merrier :)") # I ran out of ideas.
    elif tomatoes > 1 and tomatoes < 6:
        print("less tomatons :[")
    elif tomatoes < 1:
        print("Fraud.")
    if cakeSlices > 0:
        print("Portal Ending: The cake is a lie.") # I WANT PORTAL 3 (and Half-Life 3) please big Gaben :]
    elif cakeSlices < 0:
        print("Portal Fraud. It is a lie, but fraud edition.") # Layer Nine When?
    if mysteriousSubstance > 0.0:
        print("FRAUD///THIRD Disintegration Loop") # Layer Nine When?
    elif mysteriousSubstance < 0.0:
        print("Mysterious Substance Fraud.") # FRAUD///THIRS Disintegration Loop
    elif mysteriousSubstance == 0:
        print("You yearn for the mysterious substance.")
    if ouncesOfBlood > 0.0:
        print("V1 ULTRAKILL???") # Layer Nine When?
    elif ouncesOfBlood < 0.0:
        print("Fraud.")
    if floppyDiscs > 0:
        print("...How would you even consume that???") # Simple: cronch.
    elif floppyDiscs < 0:
        print("Floppy Disc Fraud.")
    if ornge > 0:
        print("ornge.")
    elif ornge < 0:
        print("how do you has negativ ornge?????") # ornge fraud.
    if milkCartons > 1:
        print("milk :].") # go commit tax evasion.
    elif milkCartons < 1:
        print("no milk :[") # :( calcium defieciency. DEATH.
        time.sleep(3)
        print("DEATH.")
    elif milkCartons < 0:
        print("what?") # milk fraud.
    elif milkCartons > 5:
        print("your GREED shall be your downfall you GLUTTON(Y)ous beast.") # two ULTRAKILL references in one line of code. Impressive.
    if computerProcessers > 0:
        print("are you going to eat that the same as you did the floppy discs?") # yes.
        time.sleep(2)
        print("Processer:", platform.processor())
    elif computerProcessers < 0:
        print("how much FRAUD are you going to commit?") # FRAUD///THIRD DISINTEGRATION LOOP. 
    autismSamplerMeal = dinoNuggies + macNCheeseBoxes + smolPizza
    if dinoNuggies == 0:
        print("Fake Autistic.")
    elif dinoNuggies < 0:
        print("Dino Nuggie fraud. Public Execution.")
    elif dinoNuggies > 1:
        print("nuggies :]")
    if macNCheeseBoxes == 0:
        print("Fake Autistic.")
    elif macNCheeseBoxes < 0:
        print("Mac N' Cheese Fraud. Public Execution.")
    elif macNCheeseBoxes > 1:
        print("Mac n' Cheedse :]")
    if smolPizza == 0:
        print("Fake Autistic.")
    elif smolPizza < 0:
        print("Smol Pizza Fraud. Public Execution.")
    elif smolPizza > 1:
        print("smol pitza :]")
    if miniPretzels == 0:
        print("Fake Autistic.")
    elif miniPretzels < 0:
        print("Mini Pretzel Fraud. Public Execution.")
    elif miniPretzels > 1:
        print("mini pretszels :]")

    time.sleep(10)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    user_choice = input("Do you wish to exit?").strip().lower()
    if user_choice == "yes" or user_choice == "y":
        break
    elif user_choice == "no:" or user_choice == "n":
        print("Restarting...")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(1)
    

time.sleep(15)