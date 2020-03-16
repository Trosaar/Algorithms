#!/usr/bin/python

import argparse

def find_max_profit(prices):
	lowest = 0
	highest = 1
	margin = 0

	for i in range(1, len(prices)):
		for j in range(i, len(prices)):
			if -prices[lowest] + prices[j] > -prices[lowest] + prices[highest]:
				highest = j
				print("sell", j, prices[j])
		if -prices[i] + prices[highest] > -prices[lowest] + prices[highest] and i < highest:
			lowest = i
			print("buy", i, prices[i])

	return -prices[lowest] + prices[highest]


if __name__ == '__main__':
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))