from django.db import models

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(unique=True, max_length=100)
    branch_code = models.CharField(unique=True, max_length=100)

class Batch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    batch_name = models.CharField(max_length=100)

class Schema(models.Model):
    scheme_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    schema_evaluation = models.CharField(max_length=100)

class Subjects(models.Model):
    sub_id = models.AutoField(primary_key=True)
    sub_code = models.CharField(unique=True, max_length=100)
    sub_name = models.CharField(unique=True, max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subject_credit = models.IntegerField()

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(unique=True, max_length=100)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    staff_code = models.CharField(unique=True, max_length=100)

class Students(models.Model):
    std_id = models.AutoField(primary_key=True)
    std_name = models.CharField(unique=True, max_length=100)
    std_usn = models.CharField(unique=True, max_length=10)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    sec = models.CharField(max_length=10)
    sem = models.IntegerField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    # staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    sem = models.IntegerField(default=0)
    sec = models.CharField(max_length=2)
    std_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    attendance = models.CharField(max_length=100)
    # schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
