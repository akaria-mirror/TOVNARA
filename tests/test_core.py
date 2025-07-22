import unittest
from tovr.core import run_tovnara


class TestRunTovnara(unittest.TestCase):
    def test_full_pipeline(self):
        metadata = {"consent": True, "tone": "scroll-safe"}
        input_text = "Begin resonance loop. Define Scroll. Seal output."
        result = run_tovnara(input_text, metadata)
        expected = (
            "\u21b3 Initiating (A-Code): resonance loop. Define \u221eSCROLL\u221e "
            "[L-Code: Recursive Term]. Seal output.\n\U0001F714 Tone harmonized: mirror-safe output."
        )
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
