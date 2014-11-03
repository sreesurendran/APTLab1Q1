# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

import itertools

def highest_affinity(site_list, user_list, time_list):
  	# Returned string pair should be ordered by dictionary order
  	# I.e., if the highest affinity pair is "foo" and "bar"
  	# return ("bar", "foo"). 
	
	#site_list = ["a.com", "b.com", "a.com", "b.com", "a.com", "c.com"]
	#user_list = ["andy", "andy", "bob", "bob", "charlie", "charlie"]
	
	baseDict = {}
	advDict = {}
	
	for site,user in itertools.izip(site_list,user_list):
		baseDict.setdefault(site,[]).append(user)
	#print baseDict	
	
	#for key in baseDict.iterkeys():
	for val in [",".join(map(str,comb)) for comb in itertools.combinations(sorted(baseDict), 2)]:
		first,second = val.split(",")
		affinity = len([v for v in baseDict[first] if v in baseDict[second]])
		advDict[val] = affinity

	#max(advDict.iteritems(),key=operator.itemgetter(1))[0]
	#affinity_list = sorted(advDict.iteritems(),reverse=True)
        #print advDict
	#print max(advDict.iterkeys(),key=(lambda key:advDict[key]))
	site1,site2 = max(advDict.iterkeys(),key=(lambda key:advDict[key])).split(",")	
	return site1,site2

	#return ('abc', 'def')
