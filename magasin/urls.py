from django.urls import path
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

from .views import CategorieAPIView, ProduitAPIView
from rest_framework import routers
from magasin.views import ProductViewset
from django.urls import include, path
# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('produit', ProductViewset, basename='produit')
from django.urls import path, include
from rest_framework import routers
from magasin.views import ProductViewset

router = routers.SimpleRouter()
router.register('produit', ProductViewset, basename='produit')
urlpatterns = [
    path('api/category/', CategorieAPIView.as_view(), name='categories'),
    path('api/produits/', ProduitAPIView.as_view(), name='produits'),
    path('api/', include(router.urls)),
    
    # path('api/category/', CategorieAPIView.as_view(), name='categories'),
    path('http://127.0.0.1:9000/admin/', include('admin_material.urls')),
    
    path('products/', views.index, name='index'),
    path('', views.acc, name='acc'),
    path('fournisseurs/', views.indexF, name='fournisseurs'),
    path('Catalogue/', views.Catalogue, name='Catalogue'),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouvFournisseur'),
    path('fournisseurs/supprimer/<int:fournisseur_id>/', views.supprimerFournisseur, name='supprimerFournisseur'),
    path('register/',views.register, name = 'register'), 
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('produit/<int:product_id>/', views.detail_product, name='detail_product'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)