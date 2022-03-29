
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Finance_Model(models.Model):
    id=models.AutoField(primary_key=True)
    Phone_Number=models.IntegerField(unique=True)
    Name=models.CharField(max_length=30,blank=True)
    Date_Of_Function=models.DateField(blank=True,null=True)
    Price_Agreed=models.CharField(max_length=20)
    Total_amount_Received_So_Far=models.CharField(max_length=30)
    Add_Money=models.CharField(max_length=30)
    amount=('Completed','Completed'),('Incompleted','Incompleted')
    Total_Amount_Status=models.CharField(max_length=20,choices=amount,blank=True)
    Email_Options=('Yes','Yes'),('No','No')
    Email_Receipt=models.CharField(max_length=30,choices=Email_Options,blank=True)
    Receipt_Options=('Yes','Yes'),('No','No')
    Print_Receipt=models.CharField(max_length=20,choices=Receipt_Options,blank=True)

    def __str__(self):
        return self.Name

class Web_Model(models.Model):
    id=models.AutoField(primary_key=True)
    Phone_Number=models.PositiveIntegerField(unique=True,help_text=" This Field is Required(*)")
    Name=models.CharField(max_length=30,help_text=" This Field is Required(*)")
    Another_name=models.CharField(max_length=30,blank=True)
    choises=('Follow-Up','Follow-Up'),('New','New')
    Calling_status=models.CharField(max_length=20,choices=choises,blank=True)
    roles=('Follow Up','Follow-Up'),('Booked SomeWhere','Booked Somewhere'),('Not Interested','Not Interested'),('Need Something','Need Something'),('GH Booking','GH Booking')
    Current_status=models.CharField(max_length=20,choices=roles,blank=True)
    Date_Of_Function=models.DateField(blank=True,null=True,help_text='use this format:<em>YYYY-MM-DD</em>')
    options=('Wedding','Wedding'),('Prewedding','Prewedding'),('Retairement','Retairement'),('Shooting','Shooting'),('Mics','Mics')
    type_function=models.CharField(max_length=20,choices=options,blank=True)
    Guests=models.PositiveIntegerField(blank=True,null=True)
    Dec_choises=('Yes','Yes'),('No','No')
    Decoration=models.CharField(max_length=10,choices=Dec_choises,blank=True)
    Food_choises=('Yes','Yes'),('No','No')
    Food=models.CharField(max_length=10,choices=Food_choises,blank=True)
    Customer_Budget=models.CharField(max_length=10,blank=True)
    Price_Quoted=models.CharField(max_length=30,blank=True)
    Price_Finalized=models.CharField(max_length=30,blank=True)
    Discount=('Yes','Yes'),('No','No')
    Discount_given=models.CharField(max_length=10,choices=Discount,blank=True)
    Comments=models.CharField(max_length=100,blank=True)
    Added_Into_System=models.DateTimeField(auto_now=True)
    
    

class Remainder_Model(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    Phone_Number=models.IntegerField()
    Date_And_Time=models.DateTimeField(auto_now=True)
    choises=('call-back','call-back'),('declined','declined'),('answered','answered')
    Calling_status=models.CharField(max_length=20,choices=choises,blank=True)
    Remainder_Date=models.DateField(blank=True,null=True,help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    Remainder_Time=models.TimeField(blank=True,null=True,help_text="Please use the following format< <em>H:M</em>>.")
    Comment=models.CharField(max_length=100,blank=True)
