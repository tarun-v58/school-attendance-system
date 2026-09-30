def clean_name(name: str) -> str:
    """
    Utility helper:
    Removes unwanted leading/trailing whitespace and converts to Title Case.
    Example: '   john doe  ' -> 'John Doe'
    """
    return name.strip().title()