url = input('Write an url: ')
url = url.split('/')
for n in url:
    if '.' in n:
        domain = n
if 'www.' in domain:
    domain = domain.replace('www.', '')
print(domain)

