
class Building(object):
    avg_sqft = 12500
    avg_bedrooms = 3
    avg_bathrooms = 2

    def describe_building(self):
        print(f"Avg. Bedrooms: {self.avg_bedrooms}")
        print(f"Avg. Bathrooms: {self.avg_bathrooms}")
        print(f"Avg. Sq. Ft.: {self.avg_sqft}")

    def get_avg_price(self):
        price = self.avg_sqft * 5 + self.avg_bedrooms * 15000 + self.avg_bathrooms * 15000
        return price

# Instantiate a Building()
avg_bldg = Building()
avg_bldg.describe_building()
print(f"Average price: {avg_bldg.get_avg_price()}")
print("\n\n")

print("INHERITANCE")
# Define a class Mansion which inherits from Building class
class Mansion(Building):
    avg_sqft = 125000
    avg_bedrooms = 8
    avg_bathrooms = 10

    # Create a function specific to the child only.  This is not accessible to instances of Building
    def how_big(self, size = 'very big'):
        print('The mansion is', size)

    # Create a method for Mansion class will override the method with the same name in Building class
    def get_avg_price(self):
        return "RIDICULOUS"

# Since Mansion inherits from Building class, we can access the methods defined for the Building class
avg_mansion = Mansion()
avg_mansion.describe_building()
print(f"Average price: {avg_mansion.get_avg_price()}")
avg_mansion.how_big()
avg_mansion.how_big('massive')
