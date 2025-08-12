import os
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from upload.forms import UploadForm
from upload.utils import download_to_ftp

from dotenv import load_dotenv

load_dotenv()


class UploadView(FormView):
    template_name = "upload/index.html"
    form_class = UploadForm
    success_url = reverse_lazy("upload:upload_page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        ip_address = form.cleaned_data["ip_address"]
        file = form.cleaned_data["file"]
        username = os.getenv('USER')
        password = os.getenv('USER_PASSWORD')

        try:
            success, report = download_to_ftp(ip_address, username, password, file)
            if success:
                messages.success(
                    self.request,
                    f"✅ Успешно! Файл {file.name} загружен на {ip_address}\n"
                    f"Отчёт сервера: {report}",
                )
            else:
                messages.warning(
                    self.request,
                    f"⚠️ Загрузка завершена с предупреждениями\n"
                    f"Отчёт сервера: {report}",
                )
        except Exception as e:
            messages.error(
                self.request,
                f"❌ Ошибка! Не удалось загрузить файл\n"
                f"Техническая информация: {str(e)}",
            )

        return super().form_valid(form)
