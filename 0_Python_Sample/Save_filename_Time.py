from datetime import datetime
time = datetime.now().strftime('%Y-%m-%d_%H-%M')

print(time)
car_dictionary = {"Car name" : "baleno"  , "year" : 2009}

file = open("e:/Github/DEVASC/2_Python_Test_Code/Word_Document/Result_Template/{0}_car.txt".format(time), "w")
file.write("Car = " + repr(car_dictionary) + "\n")
file.close