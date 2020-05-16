# Description
#
# Let's write a class that represents a coffee machine.
# The class should have a method that takes a string as input. Every time the user inputs a string to the console,
# the program invokes this method with one argument: the line that user input to the console. This system simulates
# pretty accurately how real-world electronic devices work. External components (like buttons on the coffee machine or
# tapping on the screen) generate events that pass into the single interface of the program.
#
# The class should not use system input at all; it will only handle the input that comes to it via this method and
# its string argument.
#
# The first problem that comes to mind: how to write that method in a way that it represents all that coffee machine
# can do? If the user inputs a single number, how can the method determine what that number is: a variant of coffee
# chosen by the user or the number of the disposable cups that a special worker added into the coffee machine?
#
# The right solution to this problem is to store the current state of the machine. The coffee machine has several
# states it can be in. For example, the state could be "choosing an action" or "choosing a type of coffee". Every time
# the user inputs something and a program passes that line to the method, the program determines how to interpret this
# line using the information about the current state. After processing this line, the state of the coffee machine can
# be changed or can stay the same.
#
# Objective
#
# Your final task is to refactor the program. Make it so that you can communicate with the coffee machine through a
# single method. Good luck!
#
# Example
#
# Your coffee machine should have the the same initial resources as in the example (400 ml of water, 540 ml of milk,
# 120 g of coffee beans, 9 disposable cups, $550 in cash.
# The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.
#
# Example 1:
#
# Write action (buy, fill, take, remaining, exit):
# > remaining
#
# The coffee machine has:
# 400 of water
# 540 of milk
# 120 of coffee beans
# 9 of disposable cups
# $550 of money
#
# Write action (buy, fill, take, remaining, exit):
# > buy
#
# What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
# > 2
# I have enough resources, making you a coffee!
#
# Write action (buy, fill, take, remaining, exit):
# > remaining
#
# The coffee machine has:
# 50 of water
# 465 of milk
# 100 of coffee beans
# 8 of disposable cups
# $557 of money
#
# Write action (buy, fill, take, remaining, exit):
# > buy
#
# What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
# > 2
# Sorry, not enough water!
#
# Write action (buy, fill, take, remaining, exit):
# > fill
#
# Write how many ml of water do you want to add:
# > 1000
# Write how many ml of milk do you want to add:
# > 0
# Write how many grams of coffee beans do you want to add:
# > 0
# Write how many disposable cups of coffee do you want to add:
# > 0
#
# Write action (buy, fill, take, remaining, exit):
# > remaining
#
# The coffee machine has:
# 1050 of water
# 465 of milk
# 100 of coffee beans
# 8 of disposable cups
# $557 of money
#
# Write action (buy, fill, take, remaining, exit):
# > buy
#
# What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
# > 2
# I have enough resources, making you a coffee!
#
# Write action (buy, fill, take, remaining, exit):
# > remaining
#
# The coffee machine has:
# 700 of water
# 390 of milk
# 80 of coffee beans
# 7 of disposable cups
# $564 of money
#
# Write action (buy, fill, take, remaining, exit):
# > take
#
# I gave you $564
#
# Write action (buy, fill, take, remaining, exit):
# > remaining
#
# The coffee machine has:
# 700 of water
# 390 of milk
# 80 of coffee beans
# 7 of disposable cups
# $0 of money
#
# Write action (buy, fill, take, remaining, exit):
# > exit


class CoffeeMachine:
    def __init__(self):
        self.GREETING = 'Write action (buy, fill, take, remaining, exit):\n> '
        self.ACTIONS = ['buy', 'fill', 'take', 'remaining', 'exit', 'back']
        self.MONEY = 'money'
        self.CUPS = 'cups'
        self.COST = 'cost'
        self.BEANS = 'beans'
        self.MILK = 'milk'
        self.WATER = 'water'
        self.BASE_AMOUNTS = {'1': {'name': 'espresso', self.WATER: 250, self.MILK: 0, self.BEANS: 16, self.COST: 4},
                             '2': {'name': 'latte', self.WATER: 350, self.MILK: 75, self.BEANS: 20, self.COST: 7},
                             '3': {'name': 'cappuccino', self.WATER: 200, self.MILK: 100, self.BEANS: 12, self.COST: 6}}
        # Initial inventory of the machine
        self.inventory = {self.WATER: 400, self.MILK: 540, self.BEANS: 120, self.CUPS: 9, self.MONEY: 550}
        self.STATES = ['standby', 'choosing', 'refilling']
        self.state = self.STATES[0]

    def set_state(self, state):
        self.state = self.STATES[state]

    def get_state(self):
        return self.state

    def get_inventory(self):
        return f'The coffee machine has:\n' \
               f'{self.inventory[self.WATER]} of water\n' \
               f'{self.inventory[self.MILK]} of milk\n' \
               f'{self.inventory[self.BEANS]} of coffee beans\n' \
               f'{self.inventory[self.CUPS]} of disposable cups\n' \
               f'{self.inventory[self.MONEY]} of money'

    def are_resources_enough(self, product_type):
        result = [False, 'Sorry, not enough {}!']
        if self.inventory[self.WATER] < self.BASE_AMOUNTS[product_type][self.WATER]:
            result[1] = result[1].format(self.WATER)
        elif self.inventory[self.MILK] < self.BASE_AMOUNTS[product_type][self.MILK]:
            result[1] = result[1].format(self.MILK)
        elif self.inventory[self.BEANS] < self.BASE_AMOUNTS[product_type][self.BEANS]:
            result[1] = result[1].format(self.BEANS)
        elif self.inventory[self.CUPS] == 0:
            result[1] = result[1].format(self.CUPS)
        else:
            result[0] = True
            result[1] = 'I have enough resources, making you a coffee!'
        return result

    def perform_buy_action(self, product_type):
        self.inventory[self.WATER] -= self.BASE_AMOUNTS[product_type][self.WATER]
        self.inventory[self.MILK] -= self.BASE_AMOUNTS[product_type][self.MILK]
        self.inventory[self.BEANS] -= self.BASE_AMOUNTS[product_type][self.BEANS]
        self.inventory[self.CUPS] -= 1
        self.inventory[self.MONEY] += self.BASE_AMOUNTS[product_type][self.COST]

    def perform_fill_action(self, water, milk, beans, cups):
        self.inventory[self.WATER] += water
        self.inventory[self.MILK] += milk
        self.inventory[self.BEANS] += beans
        self.inventory[self.CUPS] += cups

    def perform_take_action(self):
        given = self.inventory[self.MONEY]
        self.inventory[self.MONEY] = 0
        return 'I gave you ${}'.format(given)

    def run(self, _input):
        current_state = self.get_state()
        if _input not in self.ACTIONS and not _input.isnumeric() and current_state != self.STATES[1]:
            return self.GREETING
        elif current_state == self.STATES[0]:  # standby
            # Ask the desired action
            if _input == 'buy':
                self.set_state(1)
                return 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> '
            elif action == 'remaining':
                return self.get_inventory() + '\n\n' + self.GREETING
            elif action == 'take':
                return self.perform_take_action() + '\n\n' + self.GREETING
            elif action == 'fill':
                self.perform_fill_action(int(input('Write how many ml of water do you want to add:\n> ')),
                                         int(input('Write how many ml of milk do you want to add:\n> ')),
                                         int(input('Write how many grams of coffee beans do you want to add:\n> ')),
                                         int(input('Write how many disposable cups of coffee do you want to add:\n> ')))
                return self.GREETING
            elif action == 'exit':
                exit(0)
        elif current_state == self.STATES[1]:  # choosing
            if _input == 'back':
                self.set_state(0)
                return self.GREETING
            elif _input in ['1', '2', '3']:
                result = self.are_resources_enough(_input)  # Check the resources and give feedback
                if result[0]:  # Check result, if True, brew
                    self.perform_buy_action(_input)
                self.set_state(0)
                return result[1] + '\n' + self.GREETING  # Return the result of the resource check
            else:
                return 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> '


machine = CoffeeMachine()
input_message = machine.GREETING
while True:
    action = input(input_message)
    input_message = machine.run(action)
