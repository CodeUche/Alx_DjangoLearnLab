``markdown

**Command**
```python

from bookshelp.models import Book

retrieved_book = Book.objects.get(id=book.id)

retrieved_book

# output

<Book: The art of cybersecurity>
