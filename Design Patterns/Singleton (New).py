class Player(object):
    instance = None  # Record First object instance

    init_flag = False

    def __new__(cls, *args, **kwargs):
        # Verify if the object is None
        if cls.instance is None:
        # Allocate memory Space to the instance
            cls.instance = super().__new__(cls)
        # return the attribute of class
        return cls.instance

    def __init__(self):
        # Verify if proceed the Init
        if Player.init_flag:
            return
        # if not, proceed the init
        print('Media Player')
        Player.init_flag = True
        # init being called twice by object


# create Two objects
player1 = Player()
print(player1)

player2 = Player()
print(player2)

print(id(player1) == id(player2))



