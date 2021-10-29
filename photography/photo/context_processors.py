from .models import Avatar

def add_variable_to_context(request):
    try:
        temp = Avatar.objects.filter(is_published=True)
        return {
            'proc_photo': temp[0].photo.url
        }
    except:
        return {
            'proc_photo': '/media/nullav.jpg'
        }