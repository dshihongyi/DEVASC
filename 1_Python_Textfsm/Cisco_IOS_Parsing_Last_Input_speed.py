import sys
import textfsm
from tabulate import tabulate

template = open("D:/Github/DEVASC/1_Python_Textfsm/output/cisco_ios_show_interfaces_speed.template")
output_file = open("D:/Github/DEVASC/1_Python_Textfsm/output/show_int1_speed")

with template as f, output_file as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    # print(result)
    print(tabulate(result, headers=header))
