url = input('Write an url: ')
url1 = url.split('/')
for n in url1:
    if '.' in n:
        domain = n
if 'www.' in domain:
    domain = domain.replace('www.', '')
print(domain)

