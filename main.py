from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"},
]


@app.get("/books")
def list():
    return books

@app.post("/books")
def create(book: dict):
    book["id"] = len(books) + 1
    books.append(book)
    return book



@app.get("/books/{book_id}")
def read(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@app.delete("/books/{book_id}")
def delete(book_id: int):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            del books[i]
            return {"message": "Book deleted"}
    return {"error": "Book not found"}


@app.put("/books/{book_id}")
def update(book_id: int, book: dict):
    for i, existing_book in enumerate(books):
        if existing_book["id"] == book_id:
            books[i] = {**existing_book, **book}
            return books[i]
    return {"error": "Book not found"}