from person import Person
from manager import Manager

bob = Person(name='Bob Smith', age=42, pay=10000)
sue = Person(name='Sue Jones', age=45, pay=20000)
tom = Manager(name='Tom Doe', age=50, pay=30000)

db = [bob, sue, tom]

for obj in db:
    obj.giveRaise(.10)

for obj in db:
    print(obj.lastName(), '=>', obj.pay)
    
