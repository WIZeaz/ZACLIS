from django.contrib import admin
from .models import post, Blogimage
from django.utils.safestring import mark_safe
# Register your models here.
class post_display(admin.ModelAdmin):
    list_display=('title','release_time','link', )

admin.site.register(post,post_display)

class BlogimageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url', 'image_data')
    readonly_fields = ('image_url', 'image_data') #这里必须加上这行，表明为自定义的字段属性
    # 通过两个函数返回自定义字段的数据
    def image_url(self, obj):
        #from django.utils.safestring import mark_safe
        #mark_safe 是用来取消html转义。
        return mark_safe('<a href="%s">右键复制图片地址</a>' % obj.path.url)
    def image_data(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % obj.path.url)
    # 页面显示的字段名称
    image_data.short_description = u'图片'
    image_url.short_description = u'图片地址'


admin.site.register(Blogimage, BlogimageAdmin)