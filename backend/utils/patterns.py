import re

EMAIL_PATTERN = re.compile(r'\S+@\S+')
API_KEY_PATTERN = re.compile(r'(sk-[a-zA-Z0-9]+)')
PASSWORD_PATTERN = re.compile(r'password=\S+')
IP_PATTERN = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')