#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import socket
 
sock = socket.socket()
sock.connect(('localhost', 8080))
print(f'Соединение с сервером')

while True:
	mes = input()
	sock.send(mes.encode())
	print('Отправка сообщения')
	data = sock.recv(1024)
	print('Сообщение отправлено')
	if mes == 'exit':
		print(f'Разрыв соединения с сервером')
		sock.close()
		break
