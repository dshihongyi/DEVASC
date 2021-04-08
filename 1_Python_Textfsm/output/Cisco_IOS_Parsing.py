import sys
import textfsm
from tabulate import tabulate

template = sys.argv[1]
output_file = sys.argv[2]

with open(template) as f, open(output_file) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    # print(result)
    print(tabulate(result, headers=header))

## Print the result ##
##  $ python output/Cisco_IOS_Parsing.py output/cisco_ios_show_interfaces.template output/show_int  ##
##  $ python output/Cisco_IOS_Parsing.py output/cisco_ios_show_interfaces.template output/show_int > parse.csv ##
## https://pyneng.readthedocs.io/en/latest/book/21_textfsm/textfsm_examples.html ##