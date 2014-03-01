#!/usr/bin/python

from ML import ML, parse_url
import argparse, sys
import json

parser = argparse.ArgumentParser()
parser.add_argument('url', metavar='url', type=str,
                help='http[s]://username:password@server.')
parser.add_argument('object', metavar='object', 
                help='Interfaces|LSPs|Nodes|Demands')
parser.add_argument('-filter', help='MATE Live filter')

args = vars(parser.parse_args())
try:
    (username, password, server) = parse_url(args['url'])
except (ValueError,TypeError) as e:
    print "invalid url"
    sys.exit(1)

ml = ML(server, {'username': username, 'password': password})
r =  ml.explore(args['object'], args['filter'], 100)
r.print_csv()
