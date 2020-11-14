#Coding: UTF-8
#!/usr/local/bin/python3
#Coded By Ghosty / xEmotional
#https://github.com/xEmotional
#Ghosty~ᵛᵇ 🥀#2554

import os, sys, threading, socket, queue
from queue import *

if len(sys.argv) !=4:
    print (f"\nUsa: Python3 Simple_Port_Scanner.py <target> <start port> <end port>\n")
    sys.exit(1)
target = str(sys.argv[1])
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print_lock = threading.Lock()
print("")
def portscan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		con = s.connect((target,port))
		with print_lock:
		    print(f"{target}:{port}")
		con.close()
	except:
		pass

def threader():
	while  True:
		worker = q.get()
		portscan(worker)
		q.task_done()

q = Queue()

for x in range(500):
	t = threading.Thread(target=threader)
	t.daemon = True
	t.start()

for worker in range(start_port,end_port):
	q.put(worker)

q.join()
