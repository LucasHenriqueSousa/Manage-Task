from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    """
    Formulário personalizado para registro de usuário, baseado em UserCreationForm.
    Inclui campos adicionais (e-mail, nome e sobrenome) e aplica estilos com classes CSS.
    """

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'E-mail'
        })
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )

    class Meta:
        """
        Define o modelo de usuário utilizado e os campos do formulário.
        """
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        """
        Inicializa o formulário com atributos personalizados e textos de ajuda para os campos.
        """
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        # Personaliza o campo de nome de usuário
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '''
            <span class="form-text text-muted">
                <small>Obrigatório. 150 caracteres ou menos. Letras, dígitos e alguns caracteres</small>
            </span>
        '''
        
        # Personaliza o campo de senha
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '''
            <ul class="form-text text-muted small">
                <li>Senha deve ser única.</li>
                <li>Senha deve conter pelo menos 8 caracteres.</li>
                <li>Senha não deve ser totalmente numérica.</li>
            </ul>
        '''
        
        # Personaliza o campo de confirmação de senha
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '''
            <span class="form-text text-muted">
                <small>Digite a mesma senha.</small>
            </span>
        '''
