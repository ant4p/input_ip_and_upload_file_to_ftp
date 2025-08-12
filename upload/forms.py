import os
import ipaddress
from django import forms

from django.core.validators import validate_ipv4_address
from django.core.exceptions import ValidationError


class UploadForm(forms.Form):
    ip_address = forms.CharField(
        label="ip",
        max_length=15,
        help_text="Введите IP адрес устройства: ",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    file = forms.FileField(
        label="file",
        help_text="Выберите файл прошивки размером до 10МБ",
        widget=forms.FileInput(attrs={"class": "form-control"}),
    )

    def clean_ip_address(self):
        ip_address = self.cleaned_data["ip_address"].strip()
        try:
            validate_ipv4_address(ip_address)
            ip = ipaddress.IPv4Address(ip_address)
            if ip.is_loopback or ip.is_multicast or ip.is_unspecified:
                raise ValidationError("IP-адрес введён неверно")
            return ip_address
        except ValidationError:
            raise ValidationError("Введите корректный IP-адрес")

    def clean_file(self):
        file = self.cleaned_data["file"]
        max_size = 10 * 1024 * 1024
        if file.size > max_size:
            raise ValidationError("Файл слишком большой. Максимальный размер 10 МБ.")
        file_type = [".txt"]
        ext = os.path.splitext(file.name)[1].lower()
        if ext not in file_type:
            raise ValidationError(
                "Данный тип файла не поддерживается. Загрузите .txt файл."
            )
        return file
