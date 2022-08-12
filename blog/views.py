from django.shortcuts import render
from blog.forms import ClassroomForm  
from django.shortcuts import render  
from django.http import HttpResponse  
from blog.functions import process_files
from blog.functions import write_into_csv
from blog.forms import ClassroomForm  
from django.template import loader
import csv


# Create your views here.
def post_list(request):
   return render(request, 'blog/post_list.html', {}) 

  # if request.method == 'POST':  
  #     classroom = ClassroomForm(request.POST, request.FILES)
  #     #classroomにデータがある場合
  #     if classroom.is_valid():  
  #         availability = request.FILES['availablity']
  #         reservation = request.FILES['reservation']
  #         #implement process_files
  #         csv_data = process_files(availability, reservation)
  #         #download result as a csv format             
  #         response = write_into_csv(csv_data)

  #         return response
  # else:       
  #     ###ClassroomFormをindex.htmlに渡す
  #     classroom = ClassroomForm()  

  #     return render(request,"blog/post_list.html",{'form':classroom})  
