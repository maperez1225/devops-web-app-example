import requests
import unittest

class IntegTest(unittest.TestCase):
    def test_post(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Access-Control-Allow-Origin': '*',
        }
        # Reemplaza "api" con "localhost:8080" o la dirección de host adecuada
        response = requests.post("http://localhost:8080/api/vote", headers=headers, data="vote=a")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
