#!/usr/bin/python
import urllib
import simplejson as sj
username = 'apnerve'
url = 'http://api.twitter.com/1/statuses/followers/' + username + '.json?cursor=-2'
result = sj.load(urllib.urlopen(url))
result_length = len(result['users'])
for followers in reversed(result['users'][result_length-10:result_length]):
	print followers['name']
