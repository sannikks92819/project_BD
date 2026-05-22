from app.db.db import SessionLocal
from app.db import crud

def main():
    db = SessionLocal()
    try:
        print("\n=== Категории ===")
        categories = crud.get_categories(db)
        for cat in categories:
            print(f"ID: {cat.id}, Название: {cat.title}")
        
        print("\n=== Все книги ===")
        books = crud.get_books(db)
        for book in books:
            print(f"'{book.title}' - {book.price} руб. (Категория: {book.category.title})")
    
    finally:
        db.close()

if __name__ == "__main__":
    main()