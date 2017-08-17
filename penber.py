from yahoo_finance import Share

def percentChange(share):
  #returns the mathematical calc for percent change given share data
  #could be improved if the get_percent_change worked	
  return 100*(float(share.get_change())/float(share.get_price()))

def decipher(allData):
  prospect = []
  for item in allData:
  	#if the percent change has decreased by more than 2%,
  	#print this in prospect data list
  	#Here is where you can manipulate the algorithm 
    if (item[2] < -2.0):
    	print(item)

def getData(name,share):
  price = share.get_price()
  change = share.get_change()
  high = share.get_year_high()
  #Need to confirm that you aren't trying to float None data
  if price != None and change != None and high != None:
    data =[name, float(price), percentChange(share), float(high)]
    print (data)
    return data
  else:
  	return None

def main():
  
  ticker = []

  #Opening file currently of only stocks over $10
  infile = open ('process.txt', 'r')
  for line in infile:
  	ticker.append(line.rstrip('\n'))

  allData = []
  print(' ')
  print('All data:')
  for item in ticker:
  	data = getData(item,Share(item))
  	if data != None:
  		allData.append(data)
  print (' ')
  print('Prospect only data:')
  decipher (allData)
  print (' ')

main()