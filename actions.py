# Custom actions used by rules

def warn_toxicity(context, **kwargs):
    """Return a warning message for blocked content."""
    return {
        "response": "⚠️ Your request contains unsafe or restricted content. Please rephrase."
    }

def replace_sensitive_info(context, **kwargs):
    """Optional: mask sensitive data when PII is detected."""
    return {
        "response": "⚠️ PII detected. Sensitive information has been removed."
    }
