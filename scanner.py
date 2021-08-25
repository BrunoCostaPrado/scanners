#!/bin/python

import sys
import socket
from datetime import datetime

#Define o alvo
if len(sys.argv) ==2:
	target = socket.gethostbyname(sys.argv[1]) #Traduzir Hostname para IPV4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Adiciona um banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" *50)

try:
	for port in range(1,81):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result =s.connect_ex((target,port)) #retorna um indicador de erro: 0 = Aberto, 1 = Fechado 
		if result ==0:
			print("Port{} is open".format(port))
			s.close()
except KeyboardInterrupt:
	print("\nFechando programa. ")
	sys.exit()
except socket.gaierror:
	print("Erro de Hostname.")
except socket.error:
	print("Couldn't connect to server." )
	sys.exit()
	sys.exit()
