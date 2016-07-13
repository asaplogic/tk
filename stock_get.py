import urllib2
import time

#name of stock to pull
stock_to_pull= "AAPL"

#function pull data of 'stock' from URL
def pull_data(stock):
    try:
        file_line = stock+ '.txt'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1m/csv'
        sourceCode = urllib2.urlopen(urlToVisit).read()
        split_source = sourceCode.split('\n')

        for each_line in split_source:
            split_line = each_line.split (',')
            if len(split_line)==6:
                if 'values' not in each_line:
                    save_file = open(file_line, 'a')
                    line_to_write = each_line+'\n'
                    save_file.write(line_to_write)

        print 'pulled',stock
        print 'sleeping'
        time.sleep(5)

    except Exception,e:
        print "main loop", str(e)

pull_data(stock_to_pull)
