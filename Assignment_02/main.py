from rental import ElectricCar, Motorbike, Renter, Vehicle

def main():
    car = Vehicle('Toyota', 'Vigo', '1AB234')
    electric_car = ElectricCar('Tesla', 'Model Y', '2EC567', 75)
    motorbike = Motorbike('Honda', 'CB500', '3MB890', 500)
    renter = Renter('John Doe', 123456)

    print(f'Renter: {renter.name}, licence: {renter.license_no}')
    print(car)
    
    for bad_name, bad_license in [('', 123), ('Sam', 0), ('Alex', -5)]:
        try:
            Renter(bad_name, bad_license)
        except ValueError as error:
            print(f'Caught ValueError: {error}')

    vehicles = [electric_car, motorbike]
    print('\nDifferent vehicle types:')
    for vehicle in vehicles:
        print(vehicle)

if __name__ == '__main__':
    main()