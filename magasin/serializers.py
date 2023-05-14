from rest_framework import serializers
from .models import Produit, Categorie, Fournisseur, Commande


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = '__all__'


class ProduitSerializer(serializers.ModelSerializer):
    catégorie_id = serializers.PrimaryKeyRelatedField(source='catégorie', queryset=Categorie.objects.all())
    
    class Meta:
        model = Produit
        fields = ['id', 'libellé', 'description', 'catégorie_id']



class CommandeSerializer(serializers.ModelSerializer):
    produits = ProduitSerializer(many=True)

    class Meta:
        model = Commande
        fields = '__all__'
