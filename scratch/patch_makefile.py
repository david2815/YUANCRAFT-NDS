with open('Makefile', 'rb') as f:
    c = f.read()
c = c.replace(b'\tcp $(filter %.grit,$^)', b'\tcp -f $(filter %.grit,$^)')
with open('Makefile', 'wb') as f:
    f.write(c)
print('Makefile updated with cp -f!')

