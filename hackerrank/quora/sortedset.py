# python3

SERVER_SOCKET_PATH = _s = 'socket'

import socket, sys, os, threading, struct

def pe(s):
	print(s, file=sys.stderr)

def th(b):
	# network is big endian
	return int.from_bytes(b, 'big', signed=False)

def trans(b):
	msg = b''
	for x in b:
		msg += struct.pack('!I', x)
	return msg

l = threading.Lock()
t = {}
def proc(s):
	global l, t
	l.acquire()
	cmd = s[0]
	msg = []
	if cmd == 1:
		(set, key, score) = s[1:]
		if set not in t:
			t[set] = {}
		if key not in t[set]:
			t[set][key] = 0
		t[set][key] = score
		msg.append(0)
	elif cmd == 2:
		(set, key) = s[1:]
		if set in t:
			t[set].pop(key, None)
		msg.append(0)
	elif cmd == 3:
		set = s[1]
		size = 0
		if set in t:
			size = len(t[set])
		msg += [ 1, size ]
	elif cmd == 4:
		(set, key) = s[1:]
		score = 0
		if set in t and key in t[set]:
			score = t[set][key]
		msg += [ 1, score ]
	elif cmd == 5:
		results = []
		(lo, hi) = s[-2:]
		for set in s[1:-3]:
			if set in t:
				for k, v in t[set]:
					if lo <= k <= hi:
						results.append((k, v))
		results.sort(key=lambda x: (x[0], x[1]))
	# disconn
	elif cmd == 6:
		msg = None

	l.release()
	return msg

def thd(conn):
	flag = 1
	q = []
	while flag:
		s = conn.recv(4) # good enough
		l = th(s)
		q.append([])
		for i in range(l):
			q[-1].append(th(conn.recv(4)))
		msg = proc(q[-1])
		if msg:
			msg = trans(msg)
			try:
				conn.send(msg)
			except Exception:
				flag = 0
		# disconn
		else:
			flag = 0
	conn.close()

def server_run():
	try:
		os.unlink(_s)
	except OSError:
		if os.path.exists(_s):
			raise
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	sock.bind(_s)

	sock.listen(1)
	while True:
		(conn, addr) = sock.accept()
		threading.Thread(target=thd, args=(conn, ), daemon=True).start()
	sock.close()

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	pass

def wait():
	for x in range(10 ** 6):
		pass

def client_run(args, verbose=False):
	wait()
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	sock.connect(_s)
	r = []
	for x in args:
		sock.send(trans(x))
		r.append(sock.recv(1024)) # good enough for test purposes
	if verbose:
		for x in r:
			print(x)
	wait()
	return r

def test():
	threading.Thread(target=server_run, daemon=True).start()
	client_run([ (4, 1, 0, 1, 10), (2, 3, 0), (3, 4, 0, 1) ], verbose=True)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		server_run()
