import sys 
sys.path.append('..')
from models import Matakuliah, db
from flask_restful import Resource, abort, reqparse
from flask import jsonify

def abort_empty_data(id):
    data = Matakuliah.query.filter_by(kode=id).first()
    if data is None:
        abort(404, message=f"kode {id} tidak dapat ditemukan")

def abort_empty_args(arg, args):
    if not args[arg]:
        abort(400, message=f"Please check your args")

def get_data(id):
    data = Matakuliah.query.filter_by(kode=id).first()
    return jsonify({
        'kode': data.kode,
        'matakuliah': data.nama_mk,
        'sks': data.sks,
    })

class MatakuliahO(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nama_mk')
        self.parser.add_argument('sks')

    def get(self, id):
        data = Matakuliah.query.filter_by(kode=id).first()
        abort_empty_data(id)
        return get_data(id)

    def put(self, id):
        args = self.parser.parse_args()
        mk = args['nama_mk']
        sks = args['sks']
        abort_empty_data(id)
        data = Matakuliah.query.filter_by(kode=id).first()
        if data is not None:
            data.nama_mk = mk
            data.sks = sks
            db.session.add(data)
            db.session.commit()
        return get_data(id)
    
    def delete(self, id):
        abort_empty_data(id)
        data = Matakuliah.query.filter_by(kode=id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({
            'success': f'kode matakuliah {id} sukses dihapus'
        })

class MatakuliahI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nama_mk')
        self.parser.add_argument('sks')

    def get(self):
        provide = []
        data = Matakuliah.query.all()
        for x in range(len(data)):
            dictdata= {
                'kode': data[x].kode,
                'matakuliah': data[x].nama_mk,
                'sks': data[x].sks,
            }
            provide.append(dictdata)
        return provide
    
    def post(self):
        args = self.parser.parse_args()
        abort_empty_args('nama_mk', args)
        mk = args['nama_mk']
        sks = args['sks']
        input = Matakuliah(nama_mk=mk, sks=sks)
        db.session.add(input)
        db.session.commit()
        return jsonify({
            'success': f'matakuliah {mk} ditambahkan'
        })

config = {
    'name': 'Matakuliah',
    'routes': {
        '': MatakuliahI,
        '/<int:id>': MatakuliahO
    }
}




        


