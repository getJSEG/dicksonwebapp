from django.db import models
from datetime import datetime, timedelta
import shortuuid

s = shortuuid.ShortUUID(alphabet="0123456789")


# Create your models here.
class JobNumber(models.Model):
    invoice = models.AutoField(primary_key=True)
    status = models.CharField(max_length=30)
    created = models.DateTimeField (default= datetime.today )

# this selts the expirations for the code
def get_expiration():
        return datetime.today() + timedelta(days=5)

class CustomerCode(models.Model):
    code = s.random(length=5)
    JobNumber = models.ForeignKey(JobNumber, on_delete=models.CASCADE)
    created = models.DateTimeField ( default= datetime.today)
    expiration = models.DateField(default=get_expiration)

class File(models.Model):
    file = models.FileField(upload_to='files/designs')
    description = models.CharField( max_length=50)
    JobNumber = models.ForeignKey(JobNumber, on_delete=models.CASCADE)

class Proof(models.Model):
    proof = models.FileField(upload_to='files/proofs/')
    approved = models.BooleanField(False)
    description = models.CharField(max_length=300)
    JobNumber = models.ForeignKey(JobNumber, on_delete=models.CASCADE)
