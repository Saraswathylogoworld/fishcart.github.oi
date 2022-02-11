from django.urls import path
from . import views

urlpatterns = [
       path('fun',views.fun,name='fun'),
       path('cat',views.cat,name='cat'),
       path('display',views.display,name='display'),
       path('tablec1',views.tablec1,name='tablec1'),
       path('pro',views.pro,name='pro'),
       path('display1',views.display1,name='display1'),
       path('ptable',views.ptable,name='ptable'),
       path('edit/<int:pid>/',views.edit,name='edit'),
       path('update/<int:uid>/',views.update,name='update'),
       path('delete/<int:did>/',views.delete,name='delete'),
       path('catedit/<int:cpid>/',views.catedit,name='catedit'),
       path('catupdate/<int:cuid>/',views.catupdate,name='catupdate'),
       path('catdelete/<int:cdid>/',views.catdelete,name='catdelete'),
       path('',views.alogin,name='alogin'),
       path('adlogin',views.adlogin,name='adlogin'),
       path('Flogout',views.Flogout,name='Flogout'),
       path('recipe',views.recipe,name='recipe'),
       path('display2',views.display2,name='display2'),
       path('rtable',views.rtable,name='rtable'),
       path('redit/<int:rid>/',views.redit,name='redit'),
       path('rupdate/<int:ruid>/',views.rupdate,name='rupdate'),
       path('rdelete/<int:rdid>/',views.rdelete,name='rdelete'),
       path('tablecontact',views.tablecontact,name='tablecontact'),
       path('tablecheckout',views.tablecheckout,name='tablecheckout'),
       path('cartview',views.cartview,name='cartview'),
       path('Messagebox',views.Messagebox,name='Messagebox'),
       path('cdelete/<int:coid>/',views.cdelete,name='cdelete')
]