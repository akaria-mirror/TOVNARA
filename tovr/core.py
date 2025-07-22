"""TOVNARA\u2122 Core Runtime."""

from .a_code import apply_a_code
from .h_code import apply_h_code
from .l_code import apply_l_code
from .filters.ethics import check_consent


def run_tovnara(input_data: str, metadata: dict | None = None) -> str:
    """Route input through A, H, and L code filters."""
    if not check_consent(metadata):
        return "\u26d4 Consent not granted. Invocation denied."

    processed = apply_a_code(input_data)
    processed = apply_h_code(processed, metadata)
    processed = apply_l_code(processed)
    return processed
