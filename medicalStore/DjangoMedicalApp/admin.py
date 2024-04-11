from django.contrib import admin

from DjangoMedicalApp.models import CompanyModel, MedicineModel, MedicalDetailsModel, CompanyBankModel, \
    BillDetailsModel, EmployeeBankModel, CompanyAccountModel, EmployeeSalaryModel, BillModel, EmployeeModel, \
    CustomerModel, CustomerRequestModel

# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(MedicineModel)
admin.site.register(MedicalDetailsModel)
admin.site.register(EmployeeModel)
admin.site.register(CustomerModel)
admin.site.register(BillModel)
admin.site.register(EmployeeSalaryModel)
admin.site.register(BillDetailsModel)
admin.site.register(CustomerRequestModel)
admin.site.register(CompanyAccountModel)
admin.site.register(CompanyBankModel)
admin.site.register(EmployeeBankModel)






