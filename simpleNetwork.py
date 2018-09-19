# Network that determines weather the input is 0 or not, and if so outputs 1 

import math, random

def sigmoid(z):

    return 1 / (1 + math.exp(-z))

def sigmoid_prime(z):

    return sigmoid(z)*(1-sigmoid(z))

w = random.randint(-100, 100)/100
b = random.randint(-100, 100)/100

def activation(x):

    return sigmoid(w*x-b)

def evaluate():

    print("w = {0}, b = {1}".format(w,b))

    xs = [random.randint(-3, 3) for i in range(30)]

    for x in xs:

        print("Input: {0}, Output: {1}".format(x, activation(x)))


def generate_data():

    data=[]
    for i in range(100):
        x=random.randint(-3, 3)
        y=1 if x>0 else 0
        data.append((x, y))
    return data

def train():

    global b, w

    for example in generate_data():

        x, y = example
        delta = (activation(x)-y) * sigmoid_prime(activation(x))
        nabla_b = delta
        nabla_w = delta * x

        b -= nabla_b
        w -= nabla_w



def main():

    running=True
    while running:
        choice=input("train (t) or evaluate (e)?")

        if choice=="t":
                train()

        elif choice=="e":
            evaluate()

        else:
            running=False

if __name__ ==  "__main__":
    main()
