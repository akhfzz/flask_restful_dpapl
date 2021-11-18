import sys 
sys.path.append('..')
from models import Mahasiswa, db
from flask_restful import Resource, abort, reqparse
from flask import jsonify

def abort_empty_data(nim):
    data = Mahasiswa.query.filter_by(NIM=nim).first()
    if data is None:
        abort(404, message=f"NIM {nim} tidak dapat ditemukan")

def abort_empty_args(arg, args):
    if not args[arg]:
        abort(400, message=f"Please check your args")

def get_data_nim(nim):
    data = Mahasiswa.query.filter_by(NIM=nim).first()
    return jsonify({
        'NIM': data.NIM,
        'nama': data.nama,
        'prodi': data.prodi,
        'gender': data.gender,
        'angkatan': data.angkatan
    })

class MahasiswaO(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('NIM')
        self.parser.add_argument('nama')
        self.parser.add_argument('prodi')
        self.parser.add_argument('gender')
        self.parser.add_argument('angkatan')

    def get(self, id):
        data = Mahasiswa.query.filter_by(NIM=id).first()
        abort_empty_data(id)
        return get_data_nim(id)
    
    def put(self, id):
        args = self.parser.parse_args()
        nama = args['nama']
        prodi = args['prodi']
        gender = args['gender']
        angkatan = args['angkatan']
        abort_empty_data(id)
        data = Mahasiswa.query.filter_by(NIM=id).first()
        if data is not None:
            data.nama = nama
            data.prodi = prodi 
            data.gender = gender 
            data.angkatan = angkatan 
            db.session.add(data)
            db.session.commit()
        return get_data_nim(id)
    
    def delete(self, id):
        abort_empty_data(id)
        data = Mahasiswa.query.filter_by(NIM=id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({
            'success': f'nim {id} sukses dihapus'
        })

class MahasiswaI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('NIM')
        self.parser.add_argument('nama')
        self.parser.add_argument('prodi')
        self.parser.add_argument('gender')
        self.parser.add_argument('angkatan')

    def get(self):
        prov = []
        data = Mahasiswa.query.all()
        for x in range(len(data)):
            dicdata={
                'NIM': data[x].NIM,
                'nama': data[x].nama,
                'prodi': data[x].prodi,
                'gender': data[x].gender,
                'angkatan': data[x].angkatan
            }
            prov.append(dicdata)
        return prov
    
    def post(self):
        args = self.parser.parse_args()
        abort_empty_args('NIM', args)
        nim = args['NIM']
        nama = args['nama']
        prodi = args['prodi']
        gender = args['gender']
        angkatan = args['angkatan']
        input = Mahasiswa(NIM=nim, nama=nama, prodi=prodi, gender=gender, angkatan=angkatan)
        db.session.add(input)
        db.session.commit()
        return jsonify({
            'success': f'nim {nim} ditambahkan'
        })

config = {
    'name': 'Mahasiswa',
    'routes': {
        '': MahasiswaI,
        '/<int:id>': MahasiswaO
    }
}




        


