from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
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
