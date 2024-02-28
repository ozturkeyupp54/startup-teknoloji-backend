# startup-teknoloji-backend/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='turkish_date')
def turkish_date(value):
    months = {
        1: 'OCAK',
        2: 'ŞUBAT',
        3: 'MART',
        4: 'NİSAN',
        5: 'MAYIS',
        6: 'HAZİRAN',
        7: 'TEMMUZ',
        8: 'AĞUSTOS',
        9: 'EYLÜL',
        10: 'EKİM',
        11: 'KASIM',
        12: 'ARALIK',
    
    }
    day, month, year = value.day, value.month, value.year
    return f"{day} {months[month]} {year}"
