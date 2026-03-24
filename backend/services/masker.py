import re

def mask_sensitive_data(content):
    content = re.sub(r'password=\S+', 'password=****', content)
    content = re.sub(r'(sk-[a-zA-Z0-9]+)', 'sk-****', content)
    return content