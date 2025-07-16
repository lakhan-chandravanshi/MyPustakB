from rest_framework.response import Response
from rest_framework.decorators import api_view

BOOKS = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 3, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
]

@api_view(['GET'])
def get_books(request):
    return Response(BOOKS)

@api_view(['POST'])
def place_order(request):
    book_id = request.data.get("book_id")
    customer_name = request.data.get("customer_name")
    book = next((b for b in BOOKS if b["id"] == book_id), None)
    if not book:
        return Response({"error": "Book not found"}, status=404)

    return Response({
        "message": "Order placed successfully!",
        "customer": customer_name,
        "book": book
    })