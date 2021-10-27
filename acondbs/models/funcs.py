def shorten(text, width, placeholder="..."):
    """Truncate text

    used for repr() of models
    """

    width = max(width, len(placeholder))
    if len(text) <= width:
        return text
    return placeholder + text[-(width - len(placeholder)) :]
