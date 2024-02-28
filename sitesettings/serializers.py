from rest_framework import serializers

from sitesettings.models import SiteSettings


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = [
            "id",
            "title",
            "about_us",
            "contact_us",
            "customer_service",
            "phone",
            "email",
            "address",
            "facebook",
            "instagram",
            "twitter",
            "google",
            "youtube",
            "is_active",
            "is_deleted",
        ]
