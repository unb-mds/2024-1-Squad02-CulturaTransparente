import unittest
from unittest.mock import patch
import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.functions.principal import principal 

diretorio_arquivos_relativo = os.path.join('..', '.gitignore', 'arquivos_renomeados')



class TestPrincipal(unittest.TestCase):

    @patch('backend.functions.principal.salvarSomas')
    @patch('backend.functions.principal.agrupar')
    def test_principal(self, mock_agrupar, mock_salvarSomas):
   
        mock_agrupar.return_value = {
            'Municipio1': {
                '2023': {
                    '07': 300.0
                }
            },
            'Municipio2': {
                '2024': {
                    '01': 700.0
                }
            }
        }

       
        principal()

        
        mock_agrupar.assert_called_once_with(diretorio_arquivos_relativo)

        
        mock_salvarSomas.assert_called_once_with(diretorio_arquivos_relativo, mock_agrupar.return_value)

if __name__ == '__main__':
    unittest.main()