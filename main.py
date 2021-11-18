from pkgutil import iter_modules
from app import app, api
from models import db

root = 'mahasiswa'
modules = [name for _, name, _ in iter_modules(['rest'])]

for module in modules:
    exec(f'from rest import {module}')
    exec(f'config = {module}.config')
    for key in config['routes']:
        url = '/' + module + key
        if root == module and not key:
            api.add_resource(config['routes'][key], '/', url)
        else:
            api.add_resource(config['routes'][key], url)

if __name__ == '__main__':
    app.run(debug=True)
    # db.create_all()