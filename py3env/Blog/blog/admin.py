#coding:utf-8
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# Register your models here.


class MyUserCreationForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(MyUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['email'].required = True
        self.fields['jobnum'].required = True


class MyUserChangeForm(UserChangeForm):
    def __init__(self,*args,**kwargs):
        super(MyUserChangeForm,self).__init__(*args,**kwargs)
        self.fields['email'].required = True
#        self.fields['jobnum'].required = True

class CustomUserAdmin(UserAdmin):
    def __init__(self,*args,**kwargs):
        super(CustomUserAdmin,self).__init__(*args,**kwargs)
        self.list_display = ('username','avatar','qq','mobile','jobnum','email', 'is_active', 'is_staff', 'is_superuser')
        self.search_fields = ('username', 'email', 'jobnum')
        self.form = MyUserChangeForm  #  编辑用户表单，使用自定义的表单
        self.add_form = MyUserCreationForm  # 添加用户表单，使用自定义的表单
        # 以上的属性都可以在django源码的UserAdmin类中找到，我们做以覆盖
    
    def changelist_view(self, request, extra_context=None):  # 这个方法在源码的admin/options.py文件的ModelAdmin这个类中定义，我们要重新定义它，以达到不同权限的用户，返回的表单内容不同
        if not request.user.is_superuser:  # 非super用户不能设定编辑是否为super用户
            self.fieldsets = ((None, {'fields': ('username', 'password',)}),
                              (_('Personal info'), {'fields': ('avatar','qq','mobile','jobnum','email')}),  # _ 将('')里的内容国际化,这样可以让admin里的文字自动随着LANGUAGE_CODE切换中英文
                              (_('Permissions'), {'fields': ('is_active', 'is_staff', 'groups','user_permissions')}),
                              (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                              )  # 这里('Permissions')中没有'is_superuser',此字段定义UserChangeForm表单中的具体显示内容，并可以分类显示
            self.add_fieldsets = ((None, {'classes': ('wide',),
                                          'fields': ('username', 'avatar','qq','mobile','jobnum', 'password1', 'password2', 'email', 'is_active',
                                                     'is_staff', 'groups'),
                                          }),
                                  )  #此字段定义UserCreationForm表单中的具体显示内容
        else:  # super账户可以做任何事
            self.fieldsets = ((None, {'fields': ('username', 'password',)}),
                              (_('Personal info'), {'fields': ('avatar','qq','mobile','jobnum','email')}),
                              (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups','user_permissions')}),
                              (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                              )
            self.add_fieldsets = ((None, {'classes': ('wide',),
                                          'fields': ('username','avatar','qq','mobile','jobnum','password1', 'password2', 'email', 'is_active',
                                                     'is_staff', 'is_superuser', 'groups'),
                                          }),
                                  )
        return super(CustomUserAdmin, self).changelist_view(request, extra_context)

        
        

def make_recommend(self,request,queryset):
    queryset.update(is_recommend=True)

make_recommend.short_description = "推荐文章"



def dis_recommend(modeladmin,request,queryset):
    queryset.update(is_recommend=False)
dis_recommend.short_description = "取消推荐"

def make_published(modeladmin,request,queryset):
    queryset.update(is_post = True)
make_published.short_description = "发表文章"
def dis_published(modeladmin,request,queryset):
    queryset.update(is_post = False)
dis_published.short_description = "取消发表"

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','desc','is_recommend','is_post','click_count')
    list_display_links = ('title','desc')
    list_editable = ('click_count',)
    actions= [make_recommend,make_published,dis_recommend,dis_published]
    filter_horizontal = ('tag',)
    '''
    fieldsets = (
			(None,{
				'fields':('title','desc','content','user','category',),
				}),
			('高级设置',{
				'classes':('collapse',),
				'fields':('click_count','is_recommend','is_post',),
				}),
		)
        '''
    class Media:
        js =(
            'js/kindeditor/kindeditor-all.js',
            'js/kindeditor/lang/zh_CN.js',
            'js/kindeditor/config.js',)  


class CommentAdmin(admin.ModelAdmin):
    list_display =('username','Article','pid','date_publish')
admin.site.register(Article,ArticleAdmin)
admin.site.register(User,CustomUserAdmin)
admin.site.register(Tag)
admin.site.register(Master)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Links)
admin.site.register(Ad)
admin.site.register(Event)
