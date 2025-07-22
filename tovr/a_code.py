"""A-Code ethical execution validator."""

def apply_a_code(data: str) -> str:
    """Apply A-Code transformations to the input data."""
    if "begin" in data.lower():
        return data.replace("Begin", "\u21b3 Initiating (A-Code):")
    return data
