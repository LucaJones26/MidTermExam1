def is_valid_url(url):
    if not (url.startswith("http://") or url.startwith("https://")):
        return False
    if "." not in url:
        return False
    if url.rfind(".") == len(url - 1):
        return False
    return True