

from django.urls import path
from WebApp.views import Fin, Form_Report, Remainder_Report, Remainder_Update, Sign_up, Update,Search
from WebApp.views import Remainder,HomePage,Fin_data,Fin_update

urlpatterns=[
    path('Home/',HomePage,name='Home'),
    path('Home/Report/',Form_Report),
    path('Home/search/update/<int:id>',Update),
    path('Home/Report/update/<int:id>',Update),
    path('Home/Report/Finance/<int:id>',Fin),
    path('Home/search/Finance/<int:id>',Fin),
    path('Home/fin_reports/',Fin_data),
    path('Home/fin_reports/update/<int:id>',Fin_update),
    path('Home/Report/fin_reports/update/<int:id>',Fin_update),
    path('Home/search/',Search,name='search'),
    path('Home/Report/remainder/<int:id>',Remainder,name='search'),
    path('Home/report/',Remainder_Report),
    path('Home/report/<int:id>',Remainder_Report),
    path('Home/report/remainder_update/<int:id>',Remainder_Update),
    path('Home/search/remainder/<int:id>',Remainder),
    path('search/report/',Remainder_Report),
    path('search/remainder/report/remainder_update/<int:id>',Remainder_Update),

]