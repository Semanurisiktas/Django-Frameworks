from django.contrib import admin
from django.urls import path, include
from project import views as myProjects
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myProjects.home, name='home'),
    path('menu/',myProjects.menu, name='menu'),
    path('about/', myProjects.about, name='about'),
    path('book-table/', myProjects.bookTable, name='book-table'),
    path('account/', include('account.urls'), name='account'),
    path('basket/', myProjects.basket, name='basket'),
    path('delete-basket/<int:id>', myProjects.deleteBasket, name='delete-basket'),
    path('add-basket/<int:id>', myProjects.addBasket, name='add-basket'),
    path('payment/', myProjects.payment, name='payment'),
]

urlpatterns += static(settings.MEDIA_URL, 
 document_root=settings.MEDIA_ROOT)