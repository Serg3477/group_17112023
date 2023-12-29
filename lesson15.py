class Auto:
    year_of_manufacture: str = 2020
    mileage = 0
    def __init__(self, manufacturer: str, brand: str, fuel_consume: float):
        self.manufacturer = manufacturer
        self.brand = brand
        self.fuel_consume = fuel_consume
        self.year_of_manufacture: str
        self.mileage: str


    def __str__ (self) -> str:
        return (f'Авто {self.brand}, виробника {self.manufacturer}, {self.year_of_manufacture} року\n'
                f' виготовлення, має середю витрату палива {self.fuel_consume} / 100 км')


    def get_signalling_method(self) -> str:
        return (f'Авто {self.brand}, виробника {self.manufacturer} - подача сигналу.')

audi = Auto('Volkswagen Group', 'Audi Q5', 9.0)
renault = Auto('Renault Group', 'Renault Duster', 10.0)
peugeot = Auto('PSA Peugeot Citroën','Peugeot RCZ Coupe', 6.8)
volvo = Auto('Volvo Personvagnar AB', 'Volvo V90 Cross Country', 5.3)
toyota = Auto('Toyota Motor Corporation', 'Toyota Camry', 8.3)


print(audi.__str__())
print(volvo.get_signalling_method())

