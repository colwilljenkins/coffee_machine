from menu import MENU, resources

print(resources)
resources['money'] = 0

def machine():
    choice = input("What would you like? espresso/latte/cappucino\n")
    #giving report
    if choice == 'report':
        print(f"Water: {(resources['water'])}")
        print(f"Milk: {(resources['milk'])}")
        print(f"Coffee: {(resources['coffee'])}")
        print(f"Money: ${(resources['money'])}")
        machine()
    #Chechking resources vs recipes
    if resources['water'] < MENU[choice]['ingredients']['water']:
        print('Sorry, not enough water')
        machine()
    if resources['milk'] < MENU[choice]['ingredients']['milk']:
        print('Sorry, not enough milk')
        machine()
    if resources['coffee'] < MENU[choice]['ingredients']['coffee']:
        print('Sorry, not enough coffee')
        machine()

    quarters = int(input("How many quarters are you entering?\n"))
    dimes = int(input("How many dimes are you entering?\n"))
    total = quarters*0.25 + dimes*0.1
    #checking is enough money is entered:
    if total < MENU[choice]['cost']:
        print("Sorry that's not enough money. Your money is refunded")
        machine()
    else:
        resources['money'] += total
        resources['water'] = resources['water'] - MENU[choice]['ingredients']['water']
        resources['milk'] = resources['milk'] - MENU[choice]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - MENU[choice]['ingredients']['coffee']
        print(f'Here is your {choice} ☕ enjoy!')
        print(f"Here is your change of ${total - MENU[choice]['cost']}")
        machine()
machine()
