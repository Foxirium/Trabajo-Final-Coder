from django import forms
from .models import Post, Category


#----------------------------------------------Categorias----------------------------------------------------#

#creo un query del modelo para agarrar las categorias

cat_choices = Category.objects.all().values_list('name', 'name')

#Necesito un for para que tome cada objeto los ponga en una lista y yo poder usarlos como una lista de pyhton y que sea dinamico y pueda agregar mas categorias

choices = []

for cat in cat_choices:
    choices.append(cat)


#------------------------------------------------Formulario Posts---------------------------------------------------------#
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'author', 'body']

#Para darle formato al formulario, por cada campo llamo al forms. y quiero cambiarle los atributos=attrs donde creo una clase=class y pasarle css = formcontrol
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choices, attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }