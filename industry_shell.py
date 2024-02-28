import json
from investor.models import IndustryCategory, IndustrySubcategory

def load_industry_data(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for category_data in data:
        category_name = category_data["kategori"]
        subcategories = category_data["altKategoriler"]

        # Create IndustryCategory instance
        category_instance, created = IndustryCategory.objects.get_or_create(category_name=category_name)

        # Create IndustrySubcategory instances for the category
        for subcategory_name in subcategories:
            subcategory_instance = IndustrySubcategory(category_name=category_instance, subcategory_name=subcategory_name)
            subcategory_instance.save()

if __name__ == "__main__":
    json_file_path = 'helpers/industry.json'
    load_industry_data(json_file_path)
