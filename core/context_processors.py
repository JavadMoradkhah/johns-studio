from core.models import ContactInfo, SocialMedaInfo


def footer(request):
    contact_info = ContactInfo.objects.all().first()

    return {
        'contact_info': contact_info
    }


def sidebar(request):
    social_media_info = SocialMedaInfo.objects.all().first()

    return {
        'social_media_info': social_media_info
    }
