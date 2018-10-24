from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'order'

urlpatterns = [
    # 判断用户是否购买这门课程
    url(r'isBuy/(?P<courid>\d+)/(?P<usertel>\d+)', views.isBuy, name='isBuy'),
    # 加入购物车
    url(r'joinCart/(?P<courid>\d+)/(?P<usertel>\d+)', views.joincart, name='joincart'),
    # 查询购物车
    url(r'getCourCarts/(?P<usertel>\d+)', views.getCourCarts, name='getCourCarts'),
    # 得到订单信息
    url(r'getStatusOrder/(?P<usertel>\d+)/(?P<status>\d+)', views.getStatusOrder, name='getStatusOrder'),
    # 删除订单
    url(r'deleteOrder/(?P<orderid>\d+)/', views.deleteOrder, name='deleteOrder'),

]
