from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile, Evento, Almossom, Banda, ProgramacaoAlmossom



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Usuário'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Repita a senha'
   

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'Usuário'

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['descricao','image']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        self.fields['descricao'].label = 'Descrição'
        self.fields['image'].label = 'Imagem'

class EventUpdateForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'image', 'data']
    

    def __init__(self, *args, **kwargs):
        super(EventUpdateForm, self).__init__(*args, **kwargs)

        self.fields['titulo'].label = 'Titulo'
        self.fields['descricao'].label = 'Descrição'
        self.fields['data'].label = 'Data'


class AlmoUpdateForm(forms.ModelForm):

    class Meta:
        model = Almossom
        fields = ['data', 'image', 'info', 'descricao']
    

    def __init__(self, *args, **kwargs):
        super(AlmoUpdateForm, self).__init__(*args, **kwargs)

        self.fields['data'].label = 'Data'
        self.fields['info'].label = 'Informações'
        self.fields['descricao'].label = 'Descrição'

class BandaRegisterForm(forms.ModelForm):

    # self.

    class Meta:
        model = Banda
        fields = ['lider', 'nome', 'descricao']
    

    def __init__(self, *args, **kwargs):
        super(BandaRegisterForm, self).__init__(*args, **kwargs)


        self.fields['descricao'].label = 'Descrição'


class ProgramacaoAlmo(forms.ModelForm):

    class Meta:
        model: ProgramacaoAlmossom
        fields = ['banda', 'almossom']

    def __init__(self, *args, **kwargs):
        super(ProgramacaoAlmo, self).__init__(*args, **kwargs)



