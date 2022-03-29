
from django.contrib import admin
from WebApp.models import  Remainder_Model, Web_Model
from WebApp.models import Finance_Model
class Web_Admin(admin.ModelAdmin):
    list_display=['Phone_Number','Name','Another_name','Calling_status','Current_status','Date_Of_Function',
                'type_function','Guests','Decoration',
                'Food','Customer_Budget','Price_Quoted',
                'Price_Finalized','Discount_given',
                'Comments']
    
class Fin_Admin(admin.ModelAdmin):
    list_display=['id','Phone_Number','Name','Date_Of_Function','Price_Agreed','Add_Money','Total_amount_Received_So_Far','Email_Receipt','Print_Receipt']

class Remainder_Admin(admin.ModelAdmin):
    list_display=['id','Name','Phone_Number','Date_And_Time','Calling_status']

# Register your models here.
admin.site.register(Web_Model,Web_Admin)
admin.site.register(Finance_Model,Fin_Admin)
admin.site.register(Remainder_Model,Remainder_Admin)



