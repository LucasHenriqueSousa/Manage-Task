from django.test import TestCase
from django.contrib.auth.models import User
from .forms import SignUpForm

class SignUpFormTest(TestCase):

    def test_signup_form_valid_data(self):
        """
        Testa se o formulário é válido com dados corretos.
        """
        form = SignUpForm(data={
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'complex_password123',
            'password2': 'complex_password123'
        })
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid_data(self):
        """
        Testa se o formulário é inválido quando as senhas não coincidem.
        """
        form = SignUpForm(data={
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'complex_password123',
            'password2': 'different_password'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)  # Verifica se o erro está no campo 'password2'

    def test_signup_form_empty_fields(self):
        """
        Testa se o formulário é inválido com campos obrigatórios vazios.
        """
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)

    def test_signup_form_field_placeholders(self):
        """
        Testa se os placeholders personalizados estão configurados corretamente.
        """
        form = SignUpForm()
        self.assertEqual(form.fields['email'].widget.attrs['placeholder'], 'E-mail')
        self.assertEqual(form.fields['first_name'].widget.attrs['placeholder'], 'First Name')
        self.assertEqual(form.fields['last_name'].widget.attrs['placeholder'], 'Last Name')
        self.assertEqual(form.fields['username'].widget.attrs['placeholder'], 'User Name')
        self.assertEqual(form.fields['password1'].widget.attrs['placeholder'], 'Password')
        self.assertEqual(form.fields['password2'].widget.attrs['placeholder'], 'Confirm Password')

    def test_signup_form_help_texts(self):
        """
        Testa se os textos de ajuda personalizados estão configurados corretamente.
        """
        form = SignUpForm()
        self.assertIn('<small>Obrigatório. 150 caracteres ou menos.', form.fields['username'].help_text)
        self.assertIn('<li>Senha deve ser única.</li>', form.fields['password1'].help_text)
        self.assertIn('<small>Digite a mesma senha.', form.fields['password2'].help_text)

    def test_signup_form_creates_user(self):
        """
        Testa se o formulário cria um novo usuário quando os dados são válidos.
        """
        form = SignUpForm(data={
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com',
            'password1': 'complex_password123',
            'password2': 'complex_password123'
        })
        if form.is_valid():
            form.save()
            user = User.objects.get(username='newuser')
            self.assertEqual(user.first_name, 'New')
            self.assertEqual(user.last_name, 'User')
            self.assertEqual(user.email, 'newuser@example.com')
