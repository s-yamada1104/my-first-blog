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
def handle_uploaded_file(f):
    path = os.path.join(UPLOAD_DIR, f.name)
    print("sususus")
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    try:
        addCsv.insert_csv_data(path)  # csvデータをDBに登録する
    except Exception as exc:
        logger.error(exc)
    # os.remove(path)  # アップロードしたファイルを削除
      


# ファイルアップロード
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('upload_complete')  # アップロード完了画面にリダイレクト
    else:
        form = UploadFileForm()
    return render(request, 'blog/upload.html', {'form': form})

# ファイルアップロード完了
def upload_complete(request):
    return render(request, 'blog/upload_complete.html')
