from django.contrib import admin
from .models import BorrowBook, CheckOutBorrow, ReclaimBook, BookReturn
# Register your models here.
class BorrowBookAdmin(admin.ModelAdmin):
	class Meta:
		model = BorrowBook

admin.site.register(BorrowBook, BorrowBookAdmin)
admin.site.register(CheckOutBorrow)
admin.site.register(ReclaimBook)
admin.site.register(BookReturn)

