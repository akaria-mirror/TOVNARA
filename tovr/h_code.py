"""H-Code tonal safety layer."""

from typing import Optional, Dict

def apply_h_code(data: str, metadata: Optional[Dict[str, str]] = None) -> str:
    """Apply H-Code tonal safety transformations."""
    tone = metadata.get("tone") if metadata else ""
    if "scroll-safe" in tone:
        return f"{data}\n\U0001F714 Tone harmonized: mirror-safe output."
    return data
