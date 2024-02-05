import app
from model.library import Library
from resource.library_resource import LibraryResource

def test_get_booklist():
    library_resource = LibraryResource()
    print (library_resource.get())
def test_read():
    library = Library()
    print(library.book_list)

def test_write():
    library = Library()
    books = library.book_list
    books[1].title = 'foobar'
    library.save_books()