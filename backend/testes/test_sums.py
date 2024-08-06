import os
import json
import unittest
from unittest.mock import patch, mock_open
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))


def formatar(valor):
    partes = f"{valor:,.2f}".split(".")
    parte_inteira = partes[0].replace(",", ".")
    parte_decimal = partes[1]
    return f"{parte_inteira}.{parte_decimal}"

class TestSalvarSomas(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.join', return_value='fake_path/somasTotais.json')
    @patch('backend.functions.format.formatar', side_effect=formatar)
    def test_salvarSomas(self, mock_formatar, mock_path_join, mock_open_file):
        from backend.functions.sums import salvarSomas 

        
        somasTotais = {
            'Municipio1': {
                2021: {1: 10.0 , 2: 20.0},
                2022: {1: 15.0, 2: 25.0}
            },
            'Municipio2': {
                2021: {1: 30.0, 2: 40.0},
                2022: {1: 35.0, 2: 45.0}
            }
        }

        
        salvarSomas('fake_path', somasTotais)

        
        dados_json_esperados = {
            '2021': {
                'Municipio1': {'1': '10.00', '2': '20.00'},
                'Municipio2': {'1': '30.00', '2': '40.00'}
            },
            '2022': {
                'Municipio1': {'1': '15.00', '2': '25.00'},
                'Municipio2': {'1': '35.00', '2': '45.00'}
            }
        }

        
        mock_path_join.assert_called_once_with('fake_path', 'somasTotais.json')

        
        mock_open_file.assert_called_once_with('fake_path/somasTotais.json', 'w', encoding='utf-8')

        
        handle = mock_open_file()
        written_data = ''.join(call.args[0] for call in handle.write.mock_calls)

        
        self.assertDictEqual(json.loads(written_data), dados_json_esperados)

if __name__ == '__main__':
    unittest.main()