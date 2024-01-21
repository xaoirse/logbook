from django.contrib import admin
# from .models import Students,Items,Logs,Departmant,Masters,Items_Dep,Masters_Deps,Logs_Students,Term,Term_Dep,Parent,Child2,Child1,Pto1,Pto2,Cchild,ctoc
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	


# class LogsInline(admin.TabularInline):
#     model = Logs
#     extra = 1

# class LogsOptions (admin.ModelAdmin):
    
#     # TODO do it for all models
#     autocomplete_fields = ['master','item_dep'] # ForeignKey must have --> search_fields=['name']
#     # list_display =('stu','master','item_dep','number','datep')
#     fieldsets = [
#     (None, {'fields': ['master']}),
#     (None, {'fields': ['item_dep']}),
#     ]

# class studentsInline (TabularInlineJalaliMixin,admin.TabularInline):
#     model = Logs_Students
#     # can_delete = False
#     extra = 5
#     max_num = 10
#     def has_view_permission(self, request, obj=None):
#         return True

# class StudentsOptions (ModelAdminJalaliMixin,admin.ModelAdmin):
#     list_display =('num','name')
#     search_fields=['name']
#     inlines=[studentsInline]

# class Items_depOptions (admin.ModelAdmin):
#     list_display =('Item','dep','max_number')
#     search_fields=['Item']

# class DepInline (admin.TabularInline):
#     model = Items
#     extra = 1
# class DepartmantOptions (admin.ModelAdmin):
#     # fieldsets = [
#     #     (None, {'fields': ['name']}),
#     #     # ('Items', {'fields': ['items'], 'classes': ['collapse']}),
#     #     ]
#     # inlines=[DepInline]
#     search_fields=['name']
# class MasterInline(TabularInlineJalaliMixin,admin.TabularInline):
#     model= Masters_Deps
#     extra= 1
# class MasterOptions (ModelAdminJalaliMixin,admin.ModelAdmin):
#     search_fields=['name']
#     inlines= [MasterInline]

# class ItemsInline(admin.TabularInline):
#     # its awsome
#     # model = Items.dep.through
#     model = Items_Dep
#     extra = 1

# class ItemsOption (admin.ModelAdmin):
#     # pass
#     # list_display=('name')
#     inlines=[ItemsInline]

# # class DepartmantAdmin(admin.ModelAdmin):
# #     # TODO at the end design these 
# #     # fieldsets = [
# #     #     (None, {'fields': ['name]}),
# #     #     ('Items', {'fields': ['pub_date'], 'classes': ['collapse']}),
# #     # ]
# #     inlines = [ItemsInline]

# class TermInline (admin.TabularInline):
#     model = Term_Dep
#     extra = 1

# class TermOptions (admin.ModelAdmin):
#     inlines=[TermInline]

# # TODO sort these
# # TODO design it
# admin.site.register(Departmant,DepartmantOptions)
# admin.site.register(Students,StudentsOptions)
# admin.site.register(Items,ItemsOption)
# admin.site.register(Items_Dep,Items_depOptions)
# admin.site.register(Logs,LogsOptions)
# admin.site.register(Masters,MasterOptions)
# admin.site.register(Masters_Deps)
# admin.site.register(Term,TermOptions)

# class inline1(admin.TabularInline):
#     model = Pto1
#     extra = 1

# class inline2(admin.TabularInline):
#     model = Pto2
#     extra = 1

# class P(admin.ModelAdmin):
#     inlines = [inline1,inline2]
    
# admin.site.register(Parent,P)

# class Cinline(admin.TabularInline):
#     model = ctoc
#     extra = 1
    

# class C(admin.ModelAdmin):
#     inlines = [Cinline]
    
# admin.site.register(Child1,C)
# admin.site.register(Child2)
# admin.site.register(Pto1)
# admin.site.register(Pto2)
# admin.site.register(ctoc)
# admin.site.register(Cchild)


#############################################################
#                  New version (0.2)                        #
#############################################################

# TODO just import necessary models
from .models import *
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

class Master_option(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Masters,Master_option)
admin.site.register(TermNo)
class Inter_Dep_inline(admin.TabularInline):
    # TabularInlineJalaliMixin,
    model = Inter_Dep
    extra = 2
    formfield_overrides = {
        models.DateField: {'widget': AdminJalaliDateWidget},
    }
    

# class inter_dep(admin.ModelAdmin):
#     formfield_overrides = {
#         models.DateField: {'widget': AdminJalaliDateWidget},
#     }
    
# admin.site.register(Inter_Dep,inter_dep)

class Inter_item_inline(admin.TabularInline):
    model = Inter_Item
    extra = 1
class intershipwithitem_option(admin.ModelAdmin):
    inlines = [Inter_item_inline]
    search_fields = ['name']
admin.site.register(IntershipsWithItems,intershipwithitem_option)

class intership_options(admin.ModelAdmin):
    inlines = [Inter_Dep_inline]
    list_display =('name','term')
    list_filter = ('name','term')
    search_fields = ['name']    

admin.site.register(Internship,intership_options)
admin.site.register(Departments)
admin.site.register(Items)

class student_item_inline(TabularInlineJalaliMixin,admin.TabularInline):
    model = Student_Item
    extra = 2

class students_options(admin.ModelAdmin):
    inlines=[student_item_inline]
    list_display =('name','num')
    search_fields = ['name','num']    


admin.site.register(Students,students_options)

class term_group_inline(admin.TabularInline):
    model = Term_Group
    extra = 1
class term_inter_inline(admin.TabularInline):
    model = Term_Inter
    extra = 1
class terms_options(admin.ModelAdmin):
    inlines = [term_group_inline,term_inter_inline]
    list_filter = ('init_term','inter')

class group_students_inline(admin.TabularInline):
    autocomplete_fields = ['student']
    model = Group_Student
    extra = 1
class group_options(admin.ModelAdmin):
    inlines = [group_students_inline]
    list_display =('no','__str__')
    list_filter = ('no',)

admin.site.register(Terms,terms_options)
admin.site.register(Groups,group_options)

admin.site.site_title = "پنل مدیریت"
admin.site.site_header = "دانشگاه علوم پزشکی سبزوار"
admin.site.index_title ="برنامه ثبت فعالیت های دانشجویان پرستاری"
