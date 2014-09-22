# SEC website that offers RSS feeds to all XBRL filings ever received:
# http://www.sec.gov/spotlight/xbrl/filings-and-feeds.shtml

# monthly, historical archive of all filings with XBRL exhibits submitted to the SEC, beginning with the inception of the voluntary program in 2005:
# http://www.sec.gov/Archives/edgar/monthly/


# Packages needed: urllib (maybe urllib2)

# Downloading the data - loading the RSS feeds
def SECdownload(year, month):
	root = None
	feedFile = None
	feedData = None
	good_read = False
	itemIndex = 0
	edgarFilingsFeed = 'http://www.sec.gov/Archives/edgar/monthly/xbrlrss-' + str(year) + '-' str(month).zfill(2) + '.xml'
	print( edgarFilingsFeed )
	if not os.path.exists( "sec/" + str(year) ):
		os.makedirs( "sec/" + str(year) )
	if not os.path.exists( "sec/" + str(year) + '/' + str(month).zfill(2) ):
		os.makedirs( "sec/" + str(year) + '/' + str(month).zfill(2) )
	target_dir = "sec/" + str(year) + '/' + str(month).zfill(2) + '/'
	try:
		feedFile = urlopen( edgarFilingsFeed )
		try:
			feedData = feedFile.read()
			good_read = True
		finally:
			feedFile.close()
	except HTTPError as e:
		print( "HTTP Error:", e.code )