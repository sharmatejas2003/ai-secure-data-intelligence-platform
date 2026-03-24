import re

def mask_data(content):
    content = re.sub(r'password\s*=\s*\S+', 'password=****', content)
    content = re.sub(r'api_key\s*=\s*\S+', 'api_key=****', content)
    content = re.sub(r'sk-[a-zA-Z0-9]+', 'sk-****', content)
    return content