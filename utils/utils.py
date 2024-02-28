import os
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.text import slugify
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response




# email gonderme fonksiyonu
def send_email(user_email, context=None, user_name=None, uid=None, token=None, template_name=None, subject=None):
    to_email = user_email
    context = context
    html_message = render_to_string(template_name, context)
    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email=os.getenv('user'),
        to=[to_email],
    )
    email.content_subtype = 'html'
    email.send()


class StandardPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'next_page_url': self.get_next_link(),
            'prev_page_url': self.get_previous_link(),
            'first_page_url': self.request.build_absolute_uri().split('?')[0] + '?page=1',
            'last_page_url': self.request.build_absolute_uri().split('?')[0] + '?page=' + str(
                self.page.paginator.num_pages),
            'data': data,
            'total': self.page.paginator.count,
            'currentPage': self.page.number,
            'lastPage': self.page.paginator.num_pages,
            'firstItem': (self.page.number - 1) * self.page_size + 1,
            'lastItem': min((self.page.number) * self.page_size, self.page.paginator.count),
            'perPage': self.page_size,
        })


def turkish_slugify(text):
    tr_map = {
        'ı': 'i',
        'İ': 'i',
        'ö': 'o',
        'Ö': 'o',
        'ç': 'c',
        'Ç': 'c',
        'ş': 's',
        'Ş': 's',
        'ğ': 'g',
        'Ğ': 'g',
        'ü': 'u',
        'Ü': 'u'
    }
    for key, value in tr_map.items():
        text = text.replace(key, value)
    return slugify(text)
