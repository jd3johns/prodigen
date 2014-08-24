#!/usr/bin/env python

'''
prodigen description
'''

import sys
import logging
import argparse
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger('prodigen')

DATE = datetime.now().strftime('%Y-%m-%d')
DIRTREE = [ 'data', \
			'scripts/functions', \
			'output/figs', \
			'report/submission', \
			'lit', \
				[	'bib-db', \
					'mindmap', \
					'diagrams/dag' \
				] \
		]

def parse_args():
	''' argument parser for prodigen '''

	# TODO: Type safety
	parser = argparse.ArgumentParser()
	parser.add_argument('--proj-name', type=str, help='project name without spaces')
	# TODO: Spaces in name
	parser.add_argument('--author', type=str, help='author of the project')
	parser.add_argument('--research-dir', metavar='PATH', type=str, help='top-level directory of research projects')
	parser.add_argument('--data-file', metavar='PATH', type=str, help='directory of master dataset')
	parser.add_argument('--macro-dir', metavar='PATH', type=str, help='directory of SAS macros')
	parser.add_argument('--function-dir', metavar='PATH', type=str, help='directory of R functions')
	parser.add_argument('--biblio-dir', metavar='PATH', type=str, help='directory of bibtex database')
	parser.add_argument('--bibstyle-dir', metavar='PATH', type=str, help='directory of citation style')
	parser.add_argument('--debug', action='store_true', default=False, help='enable debug logging')
	args = parser.parse_args()

	# TODO: Use ConfigParser to check for config file first (and write/update)

	if args.debug:
		LOG.setLevel(logging.DEBUG)
	else:
		LOG.setLevel(logging.WARNING)

	return args

def main():

	args = parse_args()
	LOG.debug('Arguments: {args},\nDate: {date},\nDirtree: {dirtree}'.format(args=args, date=DATE, dirtree=DIRTREE))

	return 0

# run as a standalone script
if __name__ == '__main__':
	sys.exit(main())
