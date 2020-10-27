from spell_checker import spell_checker


words = ['lgica', 'qaundo', 'enqaunto', 'algoriimo', 'sejéa',
         'prhojeto', 'trabalàho', 'precisamops', 'ûconteúdo']

for word in words:
    print(f'{word} --> Do you mean {spell_checker(word).upper()}?')