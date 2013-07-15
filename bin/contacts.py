#!/usr/bin/python
import csv
import optparse
import re         
from itertools import izip

def print_contacts(contact,column):
	result=""	
	if column==None:
		for key in contact.keys():
			value = contact[key]
			if value!=None and value != "":
				result+="\n"
				result+= key+" :"+value
		result +="\n"		
		result +="*****************************"
		result +="\n"		

	else:
                result=contact[column]
	return result

def search(pattern,sfeild,contacts):
	res=[]
	for contact in contacts:
		if (pattern.match(contact[sfeild])):
			res.append(contact)
	return res


def loadcsv(csvfile):
	contacts= csv.DictReader(csvfile, delimiter = ',', quotechar = '"')
	return contacts

def main():
	p = optparse.OptionParser()
        p.add_option('--query', '-q',default=["Last Name","First Name"])
        p.add_option('--file', '-f')
        p.add_option('--columns', '-c')

        options, arguments = p.parse_args()

	csvfile= open(options.file, 'rb')
	if (len(arguments)<1):
		return -1
	results = loadcsv(csvfile)
	for query,arg in zip(options.query,arguments):
		prog = re.compile(arg)
	       	results=search(prog,query,results)
	if results==None:
		return -1
	if options.columns!=None:
		columns = options.columns.split(",")
	else:
		columns =[None]
	resultstr=[]
	for result in results:
		tmp=[]
		for column in columns:
			tmp.append(print_contacts(result,column))
		resultstr.append(" ".join(tmp))
			
	print "\n".join(resultstr)
if __name__ == '__main__':
	main()

