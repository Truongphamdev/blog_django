from django.contrib import admin
from .models import Post,Comment



# Register your models here.
class CommentInLine(admin.StackedInline):
	model = Comment
class PostAdmin(admin.ModelAdmin):
	list_display = ['title','date']
	list_filter = ['date']
	search_fields = ['id']
	inlines = [CommentInLine]
admin.site.register(Post,PostAdmin)
