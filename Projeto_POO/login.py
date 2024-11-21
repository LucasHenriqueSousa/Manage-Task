import unittest

class Auth:
    def __init__(self):
        self.username = 'admin'
        self.password = 'admin'
        
    def login(self, username, password):
        return username == self.username and password == self.password
    
def main():
    auth = Auth()
    username = input('Digite seu usuário: ')    
    password = input('Digite sua senha: ')
    
    if auth.login(username, password):
        print('Login bem-sucedido!!')
    else:
        print('Login falhou! Verifique usuário ou senha:')
            
class testAuth(unittest.TestCase):
    def setUp(self):
        self.auth = Auth()
        
    def test_login_True(self):
        self.assertTrue(self.auth.login('admin','admin'))
    
    def test_login_False(self):
        self.assertFalse(self.auth.login('admin','****'))

if __name__ == "__main__":
    main()
    unittest.main()

