from django.conf import settings as original_settings#必须引入
from post.models import tag
def tags_info(request):
    tags=tag.objects.all()
    return {'tags':tags}