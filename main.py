from django.db import models
from django.http import JsonResponse


class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        print()


def add(request):
    response = {}
    try:
        book_name = request.Get.get('book_name')
        book = Book(book_name=book_name)
        book.save()

        response['msg'] = 'success'
        response['error_num'] = 0

    except Exception as e:

        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
