import random
import string
import csv
import timeit
import matplotlib.pyplot as plt
from sha1 import *


def trackTime():
    #create a list of all of the lengths you would like to test
    lengths = [10, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 100000, 500000, 1000000]
    messages = []
    #for each length, generate 500 random messages of that length
    for length in lengths:
        file_name = 'runtime' + str(length) + '.csv'
        with open(file_name, 'w') as file:
            writer = csv.writer(file)
            messages = generateMessages(length)
            #for each message, time how long it takes to hash
            for message in messages:
                message = message.encode()
                result = timeit.timeit(SHA1(message).hexdigest)
                writer.writerow([result])

def averageTimes():
    #create a list of all of the lengths you would have tested
    lengths = [10, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 100000, 500000, 1000000]
    averages = []
    #for each length, open the file of 500 runtimes and average them
    for length in lengths:
        file_name = 'runtime' + str(length) + '.csv'
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            total = 0
            for row in reader:
                total += float(row[0])
            average = total / 500
            averages.append(average)
            print(average)
    #plot the averages
    plt.ylim(.5, 1.5)
    plt.xlabel('Length of Message (number of characters)')
    plt.ylabel('Average Runtime (s)')
    plt.title('Average Runtime vs Length')
    x = lengths
    y = averages
    plt.scatter(x, y)
    plt.show()

def generateMessages(length):
    messages = []
    #generate 500 random messages of the given length
    for i in range(0, 500):
        message =''.join(random.choice(string.printable) for i in range(length))
        messages.append(message)
    return messages

def main():
    #trackTime()
    averageTimes()

if __name__ == '__main__':
    main()