from django.db import models
from user.models import User
class IndustryCategory(models.Model):    
    class Meta:
        db_table = 'industry_category'
        verbose_name = 'Industry Category'
        verbose_name_plural = 'Industry Categories'
        ordering = ['-pk']
    
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class IndustrySubcategory(models.Model):
    category_name = models.ForeignKey(IndustryCategory, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=255)
    class Meta:
        db_table = 'industry_subcategory'
        verbose_name = 'Industry Subcategory'
        verbose_name_plural = 'Industry Subcategories'
        ordering = ['-pk']

    def __str__(self):
        return self.subcategory_name

class Investor(models.Model):    
   
    TURKISH_CITIES = [
    (1, 'ADANA'),
    (2, 'ADIYAMAN'),
    (3, 'AFYONKARAHİSAR'),
    (4, 'AGRI'),
    (5, 'AMASYA'),
    (6, 'ANKARA'),
    (7, 'ANTALYA'),
    (8, 'ARTVIN'),
    (9, 'AYDIN'),
    (10, 'BALIKESIR'),
    (11, 'BILECIK'),
    (12, 'BINGOL'),
    (13, 'BITLIS'),
    (14, 'BOLU'),
    (15, 'BURDUR'),
    (16, 'BURSA'),
    (17, 'CANAKKALE'),
    (18, 'CANKIRI'),
    (19, 'CORUM'),
    (20, 'DENIZLI'),
    (21, 'DIYARBAKIR'),
    (22, 'EDIRNE'),
    (23, 'ELAZIG'),
    (24, 'ERZINCAN'),
    (25, 'ERZURUM'),
    (26, 'ESKISEHIR'),
    (27, 'GAZIANTEP'),
    (28, 'GİRESUN'),
    (29, 'GUMUSHANE'),
    (30, 'HAKKARI'),
    (31, 'HATAY'),
    (32, 'ISPARTA'),
    (33, 'MERSIN'),
    (34, 'ISTANBUL'),
    (35, 'IZMIR'),
    (36, 'KARS'),
    (37, 'KASTAMONU'),
    (38, 'KAYSERI'),
    (39, 'KIRKLARELI'),
    (40, 'KIRSEHIR'),
    (41, 'KOCAELI'),
    (42, 'KONYA'),
    (43, 'KUTAHYA'),
    (44, 'MALATYA'),
    (45, 'MANISA'),
    (46, 'KAHRAMANMARAS'),
    (47, 'MARDIN'),
    (48, 'MUGLA'),
    (49, 'MUS'),
    (50, 'NEVSEHIR'),
    (51, 'NIGDE'),
    (52, 'ORDU'),
    (53, 'RIZE'),
    (54, 'SAKARYA'),
    (55, 'SAMSUN'),
    (56, 'SIIRT'),
    (57, 'SINOP'),
    (58, 'SIVAS'),
    (59, 'TEKIRDAG'),
    (60, 'TOKAT'),
    (61, 'TRABZON'),
    (62, 'TUNCELI'),
    (63, 'SANLIURFA'),
    (64, 'USAK'),
    (65, 'VAN'),
    (66, 'YOZGAT'),
    (67, 'ZONGULDAK'),
    (68, 'AKSARAY'),
    (69, 'BAYBURT'),
    (70, 'KARAMAN'),
    (71, 'KIRIKKALE'),
    (72, 'BATMAN'),
    (73, 'SIRNAK'),
    (74, 'BARTIN'),
    (75, 'ARDAHAN'),
    (76, 'IGDIR'),
    (77, 'YALOVA'),
    (78, 'KARABUK'),
    (79, 'KILIS'),
    (80, 'OSMANIYE'),
    (81, 'DUZCE'),
]
    
    mentor_keys = [
      (1, 'B2B'),
      (2,'B2C'),
      (3,'Basın'),
    ]

    
    class Meta:
        db_table = 'investor'
        verbose_name = 'Investor'
        verbose_name_plural = 'Investors'
        ordering = ['-pk']


    investor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    company_name = models.CharField(max_length=254, blank=True, null=True, unique=True)
    company_logo = models.ImageField(upload_to='company_logo/', default='', blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    company_slogan = models.CharField(max_length=255, blank=True, null=True, unique=True)
    company_foundation_date = models.DateField(blank=True, null=True)
    company_social_media = models.URLField(blank=True, null=True)
    employee_number = models.PositiveIntegerField(blank=True, null=True)
    company_location_city = models.PositiveSmallIntegerField(choices=TURKISH_CITIES, default = 34)
    investment_done = models.BooleanField(default=False, null=True, blank=True)
    investment_amount = models.PositiveBigIntegerField(blank=True, null=True)
    finance_used = models.BooleanField(default=False, null=True, blank=True)
    companization_done = models.BooleanField(default=False, null=True, blank=True)
    invoicing =  models.BooleanField(default=False, null=True, blank=True)
    calisma_durumu = models.BooleanField(default=False, null=True, blank=True)
    company_purchasing_merging = models.BooleanField(default=False, null=True, blank=True)
    public_offering = models.BooleanField(default=False, null=True, blank=True)
    
    
    company_industry_category = models.ForeignKey(IndustryCategory, blank=True, null=True, on_delete=models.SET_NULL)
    company_subcategory = models.ForeignKey(IndustrySubcategory, blank=True, null=True, on_delete=models.SET_NULL)
    company_mentoring = models.PositiveSmallIntegerField(choices=mentor_keys, default = 3)
    
    
    
    ekip_arkadasi_adi= models.CharField(max_length=40, blank=True, null=True)
    ekip_arkadasi_soyadi= models.CharField(max_length=40, blank=True, null=True)
    ekip_arkadasi_email= models.CharField(max_length=40, blank=True, null=True)
    ekip_arkadasi_phone= models.CharField(max_length=40, blank=True, null=True)
    ekip_arkadasi_linkedin = models.URLField(blank=True, null=True)
    ekip_arkadasi_department=models.PositiveSmallIntegerField(choices=TURKISH_CITIES, default = 34)
    ekip_arkadasi_position= models.PositiveSmallIntegerField(choices=TURKISH_CITIES, default = 34)
    
    
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.company_name
