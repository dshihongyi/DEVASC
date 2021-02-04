from lxml import etree
from ncclient import manager
import xml.dom.minidom
import sys
import json

# def options():
#     print("-" * 65)
#     option = int(input("Choose your Option: ")) + 500
#     print("-" * 80)
#         # if option == 501:
#         # print("\n" + "-" * 80)
#     id = int(input("Input Loopback Number: "))
#     return [option, id]


# def main():
#     number = options()
#     str_number = [str(int) for int in number]
#     print(str_number)
#     print(type(str_number[0]))
#     print(str_number[1])

# if __name__ == '__main__':
#     sys.exit(main())


id = int(input("Remove Loopback Number: "))

print(id)