import peewee as pw
from playhouse.flask_utils import FlaskDB

db = FlaskDB()


class MKB10(db.Model):
    rec_code = pw.CharField(8)
    code = pw.CharField(6, null=True, index=True)
    name = pw.TextField(index=True)
    parent = pw.ForeignKeyField("self", null=True, index=True)
    addl_code = pw.BooleanField()
    actual = pw.BooleanField()
    date = pw.DateField(null=True)


class MKBO(db.Model):
    parent = pw.ForeignKeyField("self", null=True, index=True)
    code = pw.CharField(6, null=True, index=True)
    name = pw.TextField(index=True)
    synonym = pw.CharField(4, null=True)
