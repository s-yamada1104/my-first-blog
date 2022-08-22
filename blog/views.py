from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post
import os
from blog import addCsv
import logging
logger = logging.getLogger('development')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

from .forms import UploadFileForm

UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'  # アップロードしたファイルを保存するディレクトリ


# アップロードされたファイルのハンドル
def handle_uploaded_sell_file(f):
    path = os.path.join(UPLOAD_DIR, f.name)
    print("sususus")
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    try:
        addCsv.insert_sell_csv_data(path)  # csvデータをDBに登録する
    except Exception as exc:
        logger.error(exc)
    # os.remove(path)  # アップロードしたファイルを削除
def handle_uploaded_member_file(f):
    path = os.path.join(UPLOAD_DIR, f.name)
    print("sususus")
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    try:
        addCsv.insert_member_csv_data(path)  # csvデータをDBに登録する
    except Exception as exc:
        logger.error(exc)
    # os.remove(path)  # アップロードしたファイルを削除
      


# ファイルアップロード
def upload_sell(request):
    if request.user.is_superuser:
      return redirect('blog:upload_member')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_sell_file(request.FILES['file'])
            return redirect('blog:upload_complete_sell')  # アップロード完了画面にリダイレクト
    else:
        form = UploadFileForm()
    return render(request, 'upload_sell.html', {'form': form})

def upload_member(request):
    if not request.user.is_superuser:
      return redirect('blog:upload_sell')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_member_file(request.FILES['file'])
            return redirect('blog:upload_complete_member')  # アップロード完了画面にリダイレクト
    else:
        form = UploadFileForm()
    return render(request, 'upload_member.html', {'form': form})

# ファイルアップロード完了
def upload_complete_sell(request):
    return render(request, 'upload_complete_sell.html')
def upload_complete_member(request):
    return render(request, 'upload_complete_member.html')
