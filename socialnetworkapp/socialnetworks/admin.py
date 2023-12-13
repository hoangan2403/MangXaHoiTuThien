from django.contrib import admin
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Product, User, Auction, Post, LikeType, Report, ReportType, Hashtag


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','image','name','description']
    readonly_fields = ['img']
    form = ProductForm

    def img(self, product):
        if product:
            return mark_safe(
                '<img src="/static/{url}" width = "120"/>' .format(url=product.image.name)
            )

    class Media:
        css = {
            'all' : ('/static/css/style.css', )
        }


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Post)
admin.site.register(LikeType)
admin.site.register(Report)
admin.site.register(ReportType)
admin.site.register(Hashtag)