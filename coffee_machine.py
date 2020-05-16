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
