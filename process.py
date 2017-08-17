from yahoo_finance import Share

def main():
  
  outfile = open ('process.txt', 'w')
 

  ticker = []
  infile = open ('NASDAQ.txt', 'r')
  for line in infile:
  	line.rstrip('\n')
  	share = Share(line)
  	price = share.get_price()
  	if price != None:
  	  if float(share.get_price()) > 10:
  	    outfile.write(line)

  infile.close()
  outfile.close()


main()