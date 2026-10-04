import json
import unittest
from http.server import HTTPServer
from threading import Thread
from urllib.error import HTTPError
from urllib.request import urlopen

from factorial_server import FactorialHandler, calculate_factorial


class FactorialTests(unittest.TestCase):
    def test_calculate_factorial_big_integer(self):
        value = calculate_factorial(50)
        self.assertEqual(
            value,
            30414093201713378043612608166064768844377641568960512000000000000,
        )

    def test_calculate_factorial_negative_raises(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)


class FactorialApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), FactorialHandler)
        cls.port = cls.server.server_port
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def test_factorial_endpoint_success(self):
        with urlopen(f"http://127.0.0.1:{self.port}/factorial?n=20") as response:
            self.assertEqual(response.status, 200)
            payload = json.loads(response.read().decode("utf-8"))
            self.assertEqual(payload["n"], "20")
            self.assertEqual(payload["factorial"], "2432902008176640000")

    def test_factorial_endpoint_missing_n(self):
        with self.assertRaises(HTTPError) as ctx:
            urlopen(f"http://127.0.0.1:{self.port}/factorial")
        self.assertEqual(ctx.exception.code, 400)

    def test_factorial_endpoint_negative(self):
        with self.assertRaises(HTTPError) as ctx:
            urlopen(f"http://127.0.0.1:{self.port}/factorial?n=-10")
        self.assertEqual(ctx.exception.code, 400)


if __name__ == "__main__":
    unittest.main()
