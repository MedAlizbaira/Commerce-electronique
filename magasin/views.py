from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render , get_object_or_404
from .models import Produit
from .models import Fournisseur
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Categorie
from .serializers import CategorieSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Produit
from .serializers import ProduitSerializer
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

class ProductViewset(ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class ProduitAPIView(APIView):
    def get(self, request):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)


class CategorieAPIView(APIView):
    def get(self, request):
        categories = Categorie.objects.all()
        serializer = CategorieSerializer(categories, many=True)
        return Response(serializer.data)

def index(request):
       if request.method == "POST" :
         form = ProduitForm(request.POST,request.FILES)
         if form.is_valid():
              form.save() 
              list=Produit.objects.all()
              return render(request,'magasin/vitrine.html',{'list':list})
       else : 
            form = ProduitForm()  
            list=Produit.objects.all()
            return render(request,'magasin/majProduits.html',{'form':form,'list':list})

def acc(request):
     return render(request,'magasin/acceuil.html' )

def contact(request):
     return render(request,'magasin/contact.html' )
def indexF(request):
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs': fournisseurs}
    return render(request, 'magasin/mesFournisseurs.html', context)



@user_passes_test(lambda u: u.is_superuser)
def supprimerFournisseur(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    fournisseur.delete()
    return redirect('fournisseurs')

@login_required
def nouveauFournisseur(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            nouvFournisseur = Fournisseur.objects.all()
            return render(request, 'magasin/vitrineF.html', {'nouvFournisseur': nouvFournisseur})
    else:
        form = FournisseurForm()
        nouvFournisseur = Fournisseur.objects.all()
        return render(request, 'magasin/fournisseur.html', {'form': form, 'nouvFournisseur': nouvFournisseur})

     
def Catalogue(request):
        products= Produit.objects.all()
        context={'products':products}
        return render( request,'magasin/mesProduits.html',context )

def register(request):
     if request.method == 'POST' :
          form = UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password1')
               user = authenticate(username=username, password=password)
               login(request,user)
               messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
               return redirect('home')
     else :
          form = UserCreationForm()
     return render(request,'registration/register.html',{'form' : form})

def edit_product(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            produit = form.save(commit=False)
            nouvelle_image = form.cleaned_data['img']
            if nouvelle_image:
                produit.img = nouvelle_image
            produit.save()
            return redirect('Catalogue')
    else:
        form = ProduitForm(instance=product)
    return render(request, 'magasin/edit_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Catalogue')
    return render(request, 'magasin/delete_product.html', {'product': product})

def detail_product(request, product_id):
    produit = get_object_or_404(Produit, id=product_id)
    context = {'produit': produit}
    return render(request, 'magasin/detail_product.html', context)
