cid = str(input('Digite o nome de uma cidade: ')).strip()
if ('santo' in cid.lower().split()[0]):
    print('A cidade começa com "Santo".')
else:
    print('A cidade não começa com "Santo".')
