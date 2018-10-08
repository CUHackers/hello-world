# example of importing stuff in Python
import matplotlib.pyplot as plt # matplotlib plotter
import numpy as np              # access to numpy

# Dictionaries map a key to a value. i.e. Foods['potato'] = 4 where
# potato is the key and 4 is the value.
Foods = dict()
Locs = dict()

# datapoint
class entry:
    # setting the variables for an 'entry' object
    def __init__(self, food, price, quantity, loc): # Note: Python requires you to pass in the 'self' variable
        self.food = food                            # This allows you to call the function on the object. i.e. object.function()
        self.price = float(price)
        self.quantity = int(quantity)
        self.loc = loc
        self.tot_cost = self.price * self.quantity
    def __repr__(self):
        return 'entry({},{},{},{},{})'.format(self.food,self.price,self.quantity,self.loc,self.tot_cost)

# Declaration of function: no return type needed :)
def plot():
    # Lets plot Food!
    keys = Foods.keys()
    index = np.arange(len(keys))

    yvals = [Foods[key] for key in Foods]

    plt.bar(index, yvals)
    plt.xticks(index, keys)

    plt.show()


# Passing in 'data' as a parameter
def plot(data):
    '''
    You should try to plot something!
    '''
    pass

# This loads our data from our file
def load(filename):
    data = list()
    with open(filename, "r") as f:
        for line in f:
            array = line.split(",")

            # Getting all the ocurrences of a certain food
            if not array[0] in Foods:
                Foods[array[0]] = 1
            else:
                Foods[array[0]] += 1

            # Getting all the occurences of certain locations
            if not array[3] in Locs:
                Locs[array[3]] = 1
            else:
                Locs[array[3]] += 1

            data.append(entry(array[0], # Food
                array[1], # Price
                array[2], # Quantity
                array[3]  # Location
                ))
    return data


# This is the equivalent of int main() {} in C/C++
if __name__ == "__main__":
    data = load("data.dat")
    plot(data)
