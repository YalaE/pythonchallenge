# Creating Object of a car with 4 properties - without using the list
class Car():
    def __init__(self, year_of_release, mileage, name_of_car, doors_status):
        self.name_of_car = name_of_car
        self.year_of_release = year_of_release
        self.mileage = mileage
        self.doors_status = doors_status

# Method 1
    def insurance_price(self):
        # insurance_price = None
        # If we need to declare insurance_price, it works without it, but I thought that we should define every undeclared variable??
        if self.year_of_release < 2010 and self.mileage > 8000:
            insurance_price = self.year_of_release * 0.05
        else:
            insurance_price = self.year_of_release * 0.07
        print('For car model %s insurance price is %s' % (self.name_of_car, insurance_price))

# Method 2
    def door_status(self):
        if self.doors_status == True:
            print('Car model is %s and the doors status is %s' % (self.name_of_car, self.doors_status))
        elif self.doors_status == False:
            print('Car model is %s and the doors status is %s' % (self.name_of_car, self.doors_status))
        else:
            print('Default exit point - Wrong value inserted')

# Method 3
    def print_out_car_data(self):
         print('The car model is %s, it was released at the year %s and it passed %s km' %
               (self.name_of_car, self.year_of_release, self.mileage))


# Creating two instances with execution of three methods
# Ford Focus with passed arguments
ford_focus = Car(2012, 5000, 'Ford Focus', True)

ford_focus.insurance_price()
ford_focus.door_status()
ford_focus.print_out_car_data()

print("\n")

# List for Audi A3 with arguments
audi_a3 = Car(1995, 80000, 'Audi A3', False)

audi_a3.insurance_price()
audi_a3.door_status()
audi_a3.print_out_car_data()


