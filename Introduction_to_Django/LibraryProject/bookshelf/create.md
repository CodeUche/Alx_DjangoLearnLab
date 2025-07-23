# create a Book instance

**Command:**
```python

from bookshelf.models import Book

book = Book.objects.create(
title='The art of cybersecurity',
author='Precious Uche',
publication_year=2025
)

book

# output
<Book: The art of cybersecurity>
