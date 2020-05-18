import yaml

with open('languages.yml', 'r') as f:
    data = yaml.safe_load(f)

for language, attributes in data.items():
    file_name = None

    print(f'Mocking the language "{language}"...')

    if attributes.get('group'):
        continue

    extensions = attributes.get('extensions')
    if extensions:
        file_name = f'{language}{extensions[0]}'

    file_names = attributes.get('filenames')
    if file_names:
        file_name = file_names[0]

    if not file_name:
        continue

    template = 'Hi! I am a mocked file.'

    with open(file_name, 'w') as f:
        f.write(template)
