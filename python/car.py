class Car:
    # constructor
    def __init__(self, color, model, year, for_sale):
        self.color = color
        self.model = model
        self.year = year
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}!")

    def stop(self):
        print(f"You stop the car {self.model}!")

    def details(self):
        print(f'{self.year} {self.color} {self.model} {self.for_sale}')