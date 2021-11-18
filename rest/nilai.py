import sys 
sys.path.append('..')
from models import Nilai_mk, db, Mahasiswa, Matakuliah
from flask_restful import Resource, abort, reqparse
from flask import jsonify

def abort_empty_data(nim, kode):
    mhs = Mahasiswa.query.filter_by(NIM=nim).first()
    mk = Matakuliah.query.filter_by(kode=kode).first()
    data = Nilai_mk.query.filter_by(mahasiswa=mhs).filter_by(matakuliah=mk).first()
    if data is None:
        abort(404, message=f"kode {kode} dan nim {nim} tidak dapat ditemukan")

def abort_empty_data_mhs(nim):
    mhs = Mahasiswa.query.filter_by(NIM=nim).first()
    data = Nilai_mk.query.filter_by(mahasiswa=mhs).first()
    if data is None:
        abort(404, message=f"nim {nim} tidak dapat ditemukan")

def abort_empty_data_mk(kode):
    mk = Matakuliah.query.filter_by(kode=kode).first()
    data = Nilai_mk.query.filter_by(matakuliah=mk).first()
    if data is None:
        abort(404, message=f"kode {kode} tidak dapat ditemukan")


def abort_empty_args(arg, args):
    if not args[arg]:
        abort(400, message=f"Please check your args")

def get_data(nim, kode):
    mhs = Mahasiswa.query.filter_by(NIM=nim).first()
    mk = Matakuliah.query.filter_by(kode=kode).first()
    data = Nilai_mk.query.filter_by(mahasiswa=mhs).filter_by(matakuliah=mk).first()
    return jsonify({
        'NIM' : data.mahasiswa.NIM,
        'nama': data.mahasiswa.nama,
        'prodi': data.mahasiswa.prodi,
        'gender': data.mahasiswa.gender,
        'angkatan': data.mahasiswa.angkatan,
        'matakuliah': data.matakuliah.nama_mk,
        'sks': data.matakuliah.sks,
        'nilai': data.nilai
    })

class NilaiO(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nilai')

    def get(self, nim, kode):
        mhs = Mahasiswa.query.filter_by(NIM=nim).first()
        mk = Matakuliah.query.filter_by(kode=kode).first()
        data = Nilai_mk.query.filter_by(mahasiswa=mhs).filter_by(matakuliah=mk).first()
        abort_empty_data(nim, kode)
        return get_data(nim, kode)

    def put(self, nim, kode):
        args = self.parser.parse_args()
        nilai = args['nilai']
        abort_empty_data(nim, kode)
        mhs = Mahasiswa.query.filter_by(NIM=nim).first()
        mk = Matakuliah.query.filter_by(kode=kode).first()
        data = Nilai_mk.query.filter_by(mahasiswa=mhs).filter_by(matakuliah=mk).first()
        if data is not None:
            data.nilai = nilai
            db.session.add(data)
            db.session.commit()
        return get_data(nim, kode)
    
    def delete(self, nim, kode):
        abort_empty_data(nim, kode)
        mhs = Mahasiswa.query.filter_by(NIM=nim).first()
        mk = Matakuliah.query.filter_by(kode=kode).first()
        data = Nilai_mk.query.filter_by(mahasiswa=mhs).filter_by(matakuliah=mk).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({
            'success': f'nilai dari {data.mahasiswa.nama} dengan matakuliah {data.matakuliah.nama_mk} sukses dihapus'
        })
    
    def post(self, nim, kode):
        args = self.parser.parse_args()
        abort_empty_args('nilai', args)
        nilai = args['nilai']
        mhs = Mahasiswa.query.filter_by(NIM=nim).first()
        mk = Matakuliah.query.filter_by(kode=kode).first()
        input = Nilai_mk(mahasiswa=mhs, matakuliah=mk, nilai=nilai)
        db.session.add(input)
        db.session.commit()
        return jsonify({
            'success': f'nilai {mhs.nama} ditambahkan'
        })

class NilaiI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nilai')

    def get(self):
        z = []
        data = Nilai_mk.query.all()
        for x in range(len(data)):
            x = {
                'NIM' : data[x].mahasiswa.NIM,
                'nama': data[x].mahasiswa.nama,
                'prodi': data[x].mahasiswa.prodi,
                'gender': data[x].mahasiswa.gender,
                'angkatan': data[x].mahasiswa.angkatan,
                'matakuliah': data[x].matakuliah.nama_mk,
                'sks': data[x].matakuliah.sks,
                'nilai': data[x].nilai
            }
            z.append(x)
        return z

class NilaiMahasiswa(Resource):
    def put(self, nim):
        mhs = Mahasiswa.query.filter_by(NIM=nim).first()
        data = Nilai_mk.query.filter_by(mahasiswa=mhs).all()
        z = []
        abort_empty_data_mhs(nim)
        for i in range(len(data)):
            dicdata = {
                'NIM' : data[i].mahasiswa.NIM,
                'nama': data[i].mahasiswa.nama,
                'prodi': data[i].mahasiswa.prodi,
                'gender': data[i].mahasiswa.gender,
                'angkatan': data[i].mahasiswa.angkatan,
                'kode mk': data[i].matakuliah.kode,
                'nilai': data[i].nilai
            }
            z.append(dicdata)
        return z

class NilaiMk(Resource):
    def put(self, kode):
        mk = Matakuliah.query.filter_by(kode=kode).first()
        data = Nilai_mk.query.filter_by(matakuliah=mk).all()
        abort_empty_data_mk(kode)
        zy = []
        for i in range(len(data)):
            dics = {
                'mahasiswa' : data[i].mahasiswa.NIM,
                'matakuliah': data[i].matakuliah.nama_mk,
                'sks': data[i].matakuliah.sks,
                'nilai': data[i].nilai
            }
            zy.append(dics)
        return zy

config = {
    'name': 'Nilai Matkul',
    'routes': {
        '': NilaiI,
        '/<int:nim>/<int:kode>': NilaiO,
        '/mk/<int:kode>': NilaiMk,
        '/mhs/<int:nim>': NilaiMahasiswa,
    }
}




        


