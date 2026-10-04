import unittest

from app import app


class FactorialApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_health(self) -> None:
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_factorial(self) -> None:
        response = self.client.get("/factorial?n=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"n": 10, "factorial": "3628800"},
        )

    def test_large_factorial(self) -> None:
        response = self.client.get("/factorial?n=100")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.get_json()["factorial"].startswith("933262154439"))

    def test_requires_n(self) -> None:
        response = self.client.get("/factorial")
        self.assertEqual(response.status_code, 400)

    def test_rejects_non_integer(self) -> None:
        response = self.client.get("/factorial?n=abc")
        self.assertEqual(response.status_code, 400)

    def test_rejects_negative(self) -> None:
        response = self.client.get("/factorial?n=-1")
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
