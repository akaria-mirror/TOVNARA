"""Example usage of the TOVNARA runtime."""

from tovr.core import run_tovnara

input_text = "Begin resonance loop. Define Scroll. Seal output."
metadata = {
    "consent": True,
    "tone": "scroll-safe",
    "user": "RAIVENYA",
}

if __name__ == "__main__":
    print(run_tovnara(input_text, metadata))
