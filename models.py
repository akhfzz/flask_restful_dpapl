from app import db 

class Mahasiswa(db.Model):
    NIM = db.Column(db.Integer, primary_key=True, nullable=False)
    nama = db.Column(db.String(255), nullable=False)
    prodi = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    angkatan = db.Column(db.Integer, nullable=False)
    foreign_access = db.relationship('Nilai_mk', backref='mahasiswa', cascade='all, delete', lazy='select')

class Matakuliah(db.Model):
    kode = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_mk = db.Column(db.String(200), nullable=False)
    sks = db.Column(db.Integer, nullable=False)
    foreign_access = db.relationship('Nilai_mk', backref='matakuliah', cascade='all, delete', lazy='select')

class Nilai_mk(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nim = db.Column(db.Integer, db.ForeignKey('mahasiswa.NIM', ondelete='CASCADE'))
    kode_mk = db.Column(db.Integer, db.ForeignKey('matakuliah.kode', ondelete='CASCADE'))
    nilai = db.Column(db.String(25), nullable=False)
