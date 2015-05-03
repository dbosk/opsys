#!/usr/bin/env python3

# Author:  Daniel Bosk <daniel.bosk@miun.se>
# Date:    15 May 2012

import sys, threading, time

# function to be run in each separate thread
def test(thread_id, delay):
	for i in range(2):
		for j in range(5):
			# critical section
			# print values of i and j
			print( str(thread_id) + ": i=" + str(i) + ", j=" + str(j) )
			# remainder section
			# sleep for delay seconds
			time.sleep( float(delay) )

def main():
	# default to using two threads.  this can be overridden by passing a number 
	# as argument from the command line.
	# usage: race.py <nthreads>
	nthreads = 2
	if len(sys.argv) > 1:
		nthreads = int( sys.argv[1] )

	threads = []
	for n in range( nthreads ):
		# create a thread which runs the test-function above, documentation: 
		# http://docs.python.org/library/threading.html?highlight=threading.thread#threading.Thread
		t = threading.Thread( target=test,
				args=("thread"+str(n), 1+float(n)/10) )
		t.start()
		threads.append( t )

	print( "waiting ..." )
	# wait for all threads to finish
	for t in threads:
		t.join()
	print( "done" )

if __name__ == "__main__":
	main()
