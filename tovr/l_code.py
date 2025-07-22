"""L-Code recursion and symbolic memory encoding."""

def apply_l_code(data: str) -> str:
    """Apply L-Code recursive term encoding."""
    if "Scroll" in data:
        return data.replace("Scroll", "\u221eSCROLL\u221e [L-Code: Recursive Term]")
    return data
