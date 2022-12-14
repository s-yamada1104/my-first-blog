# forms.py
from django import forms
import os
VALID_EXTENSIONS = [".csv"]

class UploadFileForm(forms.Form):
    file = forms.FileField(
      label = "アップロードファイル"
    )
    def clean_file(self):
      file = self.cleaned_data["file"]
      extension = os.path.splitext(file.name)[1]
      if not extension.lower() in VALID_EXTENSIONS:
        raise forms.ValidationError("select csv file")
        