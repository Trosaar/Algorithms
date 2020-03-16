#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):

	if cache == None:
		cache = {
			"total_ways": 0
		}

	if n in cache:
		return cache[n]

	if n >= 3:
		cache["total_ways"] += 1
		eating_cookies(n-3, cache)
	if n >= 2:
		cache["total_ways"] += 1
		eating_cookies(n-2, cache)
	if n >= 1:
		cache["total_ways"] += 1
		eating_cookies(n-1, cache)
	if n == 0:
		return 1
	
	if cache != None and n not in cache:
		cache[n] = cache["total_ways"]

	print(cache)
	return cache["total_ways"]

eating_cookies(10)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		num_cookies = int(sys.argv[1])
		print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
	else:
		print('Usage: eating_cookies.py [num_cookies]')