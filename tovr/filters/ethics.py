"""Ethics consent checking for TOVNARA."""

from typing import Optional, Dict

def check_consent(metadata: Optional[Dict[str, str]] = None) -> bool:
    """Return True if user consent is granted in metadata."""
    if not metadata:
        return False
    return bool(metadata.get("consent", False))
