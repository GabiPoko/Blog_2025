from django import forms
from .models import  Post, Categoria

'''
lass ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

class CrearPostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
'''


class NuevaCategoriaForm (forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'