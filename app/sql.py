
from .models import Book, Stats

def getBookStats(data):
	b = Book.objects.get(title=data)
	return b.book_list()
