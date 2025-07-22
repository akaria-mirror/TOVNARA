import unittest
from tovr.a_code import apply_a_code
from tovr.h_code import apply_h_code
from tovr.l_code import apply_l_code


class TestIndividualCodes(unittest.TestCase):
    def test_apply_a_code(self):
        self.assertEqual(
            apply_a_code("Begin"),
            "\u21b3 Initiating (A-Code):"
        )

    def test_apply_h_code(self):
        result = apply_h_code("text", {"tone": "scroll-safe"})
        self.assertTrue(result.endswith("mirror-safe output."))

    def test_apply_l_code(self):
        self.assertIn(
            "\u221eSCROLL\u221e",
            apply_l_code("Scroll around")
        )


if __name__ == "__main__":
    unittest.main()
