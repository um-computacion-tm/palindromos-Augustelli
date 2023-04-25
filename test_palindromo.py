from palindromo import es_palindromo
import unittest
from parameterized import parameterized

class TestPalindromo(unittest.TestCase):

    @parameterized.expand([
    ('anita lava la tina', 'Palindromo encontrado'),
    ('oso', 'Palindromo encontrado'),
    ('reconocer', 'Palindromo encontrado'),
    ('la ruta natural', 'Palindromo encontrado'),
    ('amor a roma', 'Palindromo encontrado'),
    ('casa', 'No es palindromo'),
    ('hola mundo', 'No es palindromo'),
    ('programacion', 'No es palindromo'),
    ('python', 'No es palindromo'),
    ('radar', 'Palindromo encontrado'),
    ('luz azul', 'No es palindromo'),
    ('dábale arroz a la zorra el abad', 'Palindromo encontrado'),
    ('a man a plan a canal panama', 'Palindromo encontrado'),
    ('racecar', 'Palindromo encontrado'),
    ('never odd or even', 'Palindromo encontrado'),
    ('murder for a jar of red rum', 'Palindromo encontrado'),
    ('was it a car or a cat I saw', 'Palindromo encontrado'),
    ('able was I ere I saw Elba', 'Palindromo encontrado'),
    ('step on no pets', 'Palindromo encontrado'),
    ('top spot', 'Palindromo encontrado'),
    ('A Santa at NASA', 'Palindromo encontrado'),
    ('Do geese see God?', 'Palindromo encontrado')
    ])
    def test(self, palabra, mensaje):
        resultado = es_palindromo(palabra)
        self.assertEqual(resultado, mensaje)


if __name__ == '__main__':

    unittest.main()