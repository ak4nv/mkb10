import peewee as pw

from config import db


class MKB10(db.Model):
    rec_code = pw.CharField(8)
    code = pw.CharField(6, null=True, index=True)
    name = pw.TextField(index=True)
    id_parent = pw.ForeignKeyField('self', null=True, index=True)
    addl_code = pw.BooleanField()
    actual = pw.BooleanField()
    date = pw.DateField(null=True)


class MKBO(db.Model):
    id_parent = pw.ForeignKeyField('self', null=True, index=True)
    name = pw.TextField(index=True)
    level = pw.CharField(1, null=True)
    ict = pw.CharField(4, null=True)
    code = pw.CharField(6, null=True, index=True)
