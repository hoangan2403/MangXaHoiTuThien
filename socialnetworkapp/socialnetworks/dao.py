from django.db.models import Count
from .models import Auction, Category, Product


def load_Auction(params={}):
    q = Auction.objects.filter(active = True)

    kw = params.get('kw')
    if kw:
        q = q.filter(product__icontains=kw)

    cate_id = params.get('product_cate_id')
    if cate_id:
        q = q.filter(product__category_id=cate_id)

    return q


def count_Auction_By_CateOfProduct():
    return (Category.objects.annotate(count1=Count('product__auction__user_care__id'))
            .values("id", "name", "count1").order_by('count1'))


def count_CmmAuction_By_CateOfProduct():
    return (Category.objects.annotate( count2=Count('product__auction__participateauction__id'))
            .values("id","name","count2").order_by('count2'))