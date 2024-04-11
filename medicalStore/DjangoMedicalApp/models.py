from django.db import models


# Create your models here.
class CompanyModel(models.Model):
    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=255)
    licence_no: str = models.CharField(max_length=255)
    address: str = models.CharField(max_length=255)
    contact_no: str = models.CharField(max_length=255)
    email: str = models.CharField(max_length=255)
    description: str = models.CharField(max_length=255)
    added_on: str = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class MedicineModel(models.Model):
    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=255)
    medical_type: str = models.CharField(max_length=255)
    buy_price: str = models.CharField(max_length=255)
    sell_price: str = models.CharField(max_length=255)
    c_gst: str = models.CharField(max_length=255)
    s_gst: str = models.CharField(max_length=255)
    batch_no: str = models.CharField(max_length=255)
    shelf_no: str = models.CharField(max_length=255)
    expire_date: str = models.DateField()
    mfg_date: str = models.DateField()
    company_id: str = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    description: str = models.CharField(max_length=255)
    in_stock_total: int = models.IntegerField()
    qty_in_strip: int = models.IntegerField()
    added_on: str = models.DateTimeField(auto_now_add=True)


class MedicalDetailsModel(models.Model):
    id: int = models.AutoField(primary_key=True)
    medicine_id: int = models.ForeignKey(MedicineModel, on_delete=models.CASCADE)
    salt_name: str = models.CharField(max_length=255)
    salt_qty: str = models.CharField(max_length=255)
    salt_qty_type: str = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    added_on: str = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class EmployeeModel(models.Model):
    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=255)
    joining_date: str = models.DateField()
    phone: str = models.CharField(max_length=255)
    address: str = models.CharField(max_length=255)
    added_on: str = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class CustomerModel(models.Model):
    id: int = models.AutoField(primary_key=True)
    name: str = models.CharField(max_length=255)
    address: str = models.CharField(max_length=255)
    contact: str = models.CharField(max_length=255)
    added_on: str = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class BillModel(models.Model):
    id: int = models.AutoField(primary_key=True)
    customer_id: int = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    added_on: str = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class EmployeeSalaryModel(models.Model):
    id: int = models.AutoField(primary_key=True)
    employee_id: int = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    salary_date: str = models.DateField()
    salary_amount: str = models.CharField(max_length=255)
    added_on: str = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class BillDetailsModel(models.Model):
    id: int = models.AutoField(primary_key=True)
    bill_id: int = models.ForeignKey(BillModel, on_delete=models.CASCADE)
    medicine_id: int = models.ForeignKey(MedicineModel, on_delete=models.CASCADE)
    qty: int = models.IntegerField()
    added_on: str = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class CustomerRequestModel(models.Model):
    id: int = models.AutoField(primary_key=True)
    customer_name: str = models.CharField(max_length=255)
    phone: str = models.CharField(max_length=255)
    medicine_details: str = models.CharField(max_length=255)
    status: bool = models.BooleanField(default=False)
    added_on: str = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class CompanyAccountModel(models.Model):
    choices = ((1, 'Debit'), (2, 'Credit'))
    id: int = models.AutoField(primary_key=True)
    company_id: int = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    transaction_type: str = models.CharField(choices=choices, max_length=255)
    transaction_amt: str = models.CharField(max_length=255)
    transaction_date: str = models.DateField()
    added_on: str = models.DateTimeField(auto_now_add=True)
    payment_mode: str = models.CharField(max_length=255)


class CompanyBankModel(models.Model):
    id: int = models.AutoField(primary_key=True)
    bank_account_no: str = models.CharField(max_length=255)
    ifsc_no: str = models.CharField(max_length=255)
    company_id: int = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    added_on: str = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class EmployeeBankModel(models.Model):
    id: int = models.AutoField(primary_key=True)
    bank_account_no: str = models.CharField(max_length=255)
    ifsc_no: str = models.CharField(max_length=255)
    employee_id: int = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    added_on: str = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()




