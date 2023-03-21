from django.urls import path
from . import views
urlpatterns = [
   
   
    path('data/',views.scrape_products,name='data'),
    path('update/',views.scrape_product,name='update')

]
