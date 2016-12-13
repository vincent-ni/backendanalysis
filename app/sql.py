
from .models import Book, Stats

# Returns the stats for a particular book
def getBookStats(data):
	try:
		b = Book.objects.get(title=data)
	except Book.DoesNotExist:
		raise Http404("Book does not exist!")
	return b.book_stats()

# Returns a list of books #
def getBookList():
	return Book.objects.values_list('title', flat=True)

# Get all nearby locations for this book
def getLocationsNearby(data, latitude, longitude, radius):
	latitudeNeg = latitude - radius
	latitudePos = latitude + radius
	longitudeNeg = longitude - radius
	longitudePos = longitude + radius

	s = getBookStats(data)
	filter_s = s.filter(longitude__gte=longitudeNeg, longitude__lte=longitudePos).filter(latitude_gte=latitudeNeg, latitude__lte=latitudePos)
	return filter_s

#Get number of people reading a book near me
def getNumPpleNearMe(data, latitude, longitude, radius):
	return getLocationsNearby(data, latitude, longitude, radius).count()

#Get list of all books in given radius by seller
#def getSellerBookInfo(seller, book, latitude, longitude, radius):
