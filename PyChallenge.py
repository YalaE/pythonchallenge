# Creating Object of a car with 4 properties - was asked in assignment to use a list
class Car():
    def __init__(self, *list_of_car_instances):
         self.list_of_car_instances = list_of_car_instances

# Method 1
    def insurance_price(self):
        year_of_release = self.list_of_car_instances[0]
        mileage = self.list_of_car_instances[1]
        insurance_price = None

        if year_of_release < 2010 and mileage > 8000:
            insurance_price = year_of_release * 0.05
        else:
            insurance_price = year_of_release * 0.07
        print('For car model %s insurance price is %s' % (self.list_of_car_instances[2], insurance_price))

# Method 2
    def door_status(self):
        doors_status = self.list_of_car_instances[-1]
        if doors_status == True:
            print('Car model is %s and the doors status is %s' % (self.list_of_car_instances[2], doors_status))
        elif doors_status == False:
            print('Car model is %s and the doors status is %s' % (self.list_of_car_instances[2], doors_status))
        else:
            print('Default exit point - Wrong value inserted')

# Method 3
    def print_out_car_data(self):
         print('The car model is %s, it was released at the year %s and it passed %s km' %
               (self.list_of_car_instances[2], self.list_of_car_instances[0], self.list_of_car_instances[1]))


# Creating two instances with execution of three methods
# List for Ford Focus
ford_focus = Car(2012, 5000, 'Ford Focus', True)

ford_focus.insurance_price()
ford_focus.door_status()
ford_focus.print_out_car_data()

print("\n")

# List for Audi A3
audi_a3 = Car(1995, 80000, 'Audi A3', False)

audi_a3.insurance_price()
audi_a3.door_status()
audi_a3.print_out_car_data()




