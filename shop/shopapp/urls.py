from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shopapp'

urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    path('', views.AllCategories, name='all_categories'),
    path('categories/<slug:c_slug>/', views.AllCategories, name='cat_products'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProductDetail, name='product'),
    path('search/', views.SearchView, name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
