import socket
from clint.textui import colored
print("""
    ####################################
    #       Simple Ip To get ip        #
    #          Twitter:Jppe14          #
    #                                  #
    #                                  #
    #        C0ded By Red Virus        #
    ####################################




""")
print("""1: Get Ip Site 
2: Get Your Ip
""")
x = input(">>> ")
if x == "1":
    f = input("Please Enter Your Site: ")
    print("ip",f," is ",socket.gethostbyname(f))
elif x == "2":
    print(socket.gethostbyname(socket.gethostname()))
else:
    print("False Chose")
