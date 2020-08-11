class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return "Name: " + self.name + "\n" "Description: " + self.description
    def on_take(self):
        print("\nYou have picked up " + self.name)

    def on_drop(self):
        print("\nYou have dropped the " + self.name)
