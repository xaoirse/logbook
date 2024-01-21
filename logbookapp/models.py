from django.db import models
from django.contrib import auth
from django.core.exceptions import ValidationError

class TermNo(models.Model):
    term = models.CharField(max_length=4,unique=True,verbose_name='ترم',help_text='سه رقمی و لاتین وارد شود. مانند: 962')
    objects = models.Manager()
    class Meta:
        verbose_name_plural = "ترم ها"
        verbose_name="ترم"
    def __str__(self):
        return str(self.term)

class Masters(models.Model):
    name = models.CharField(max_length=250,verbose_name='نام استاد')
    # TODO validator for username and password
    username = models.CharField(max_length=60,verbose_name='نام کاربری',help_text='با حروف لاتین')
    # TODO dont save password! hash it
    password = models.CharField(max_length=250,verbose_name='رمز عبور',help_text='رمز عبور برای وراد شدن استاد به سامانه')
    token = models.CharField(max_length=64,default='token') # TODO ediatble=False
    objects = models.Manager()
    class Meta:
        verbose_name_plural = "اساتید"
        verbose_name="استاد"
    def __str__(self):
        return self.name

class Departments(models.Model):
    name = models.CharField(max_length=250,verbose_name='نام بخش',unique=True)
    details = models.TextField(verbose_name='توضیحات',blank=True)
    class Meta:
        verbose_name_plural = "بخش ها"
        verbose_name="بخش"
    def __str__(self):
        return self.name

class Items(models.Model):
    name = models.CharField(max_length=250,verbose_name='نام آیتم',unique=True)
    objects = models.Manager()
    class Meta:
        verbose_name_plural = "آیتم ها"
        verbose_name="آیتم"
    def __str__(self):
        return self.name

class IntershipsWithItems(models.Model):
    name = models.CharField(max_length=250,verbose_name='نام مدل کارآموزی',unique=True)
    item = models.ManyToManyField(Items,through='Inter_Item')
    objects = models.Manager()    
    class Meta:
        verbose_name_plural = "مدل های کارآموزی"
        verbose_name="مدل کارآموزی"
    def __str__(self):
        return str(self.name)

class Inter_Item(models.Model):
    inter = models.ForeignKey(IntershipsWithItems,on_delete=models.PROTECT)
    item = models.OneToOneField(Items,on_delete=models.PROTECT,verbose_name ='آیتم')
    min_no = models.PositiveSmallIntegerField(verbose_name='حداقل تعداد',default=1)
    objects = models.Manager()
    class Meta:
        unique_together = ["inter", "item"]
        verbose_name_plural = "آیتم های کارآموزی"
        verbose_name="آیتم"
    def __str__(self):
        return '{}: {}'.format(self.inter.__str__(),self.item.__str__())

###########################################







class Internship(models.Model):
    name = models.ForeignKey(IntershipsWithItems,on_delete=models.PROTECT,verbose_name='کارآموزی',help_text='مدل کارآموزی را انتخاب کنید')
    term = models.ForeignKey(TermNo,on_delete=models.PROTECT,verbose_name='ترم کنونی',help_text='ترمی که میخواهید این کارآموزی در آن ثبت شود')
    department = models.ManyToManyField(Departments,through='Inter_Dep')
    objects = models.Manager()
    class Meta:
        unique_together = ["name", "term"]
        verbose_name_plural = "کارآموزی ها"
        verbose_name="کارآموزی"
    def __str__(self):
        return '{}  '.format(self.term)+ self.name.__str__()

class Inter_Dep(models.Model):
    inter = models.ForeignKey(Internship,on_delete=models.PROTECT,)
    dep = models.ForeignKey(Departments,on_delete=models.PROTECT,verbose_name = 'بخش')
    master = models.ManyToManyField(Masters,verbose_name = 'استاد')
    from_date = models.DateField(verbose_name='تاریخ شروع')
    to_date = models.DateField(verbose_name='تاریخ پایان')
    objects = models.Manager()
    class Meta:
        unique_together = ["inter", "dep",'from_date','to_date']
        verbose_name_plural = "برنامه بخش ها"
        verbose_name="بخش"
    def __str__(self):
        return '{}'.format(self.inter.__str__())


# A validator for Student num
# TODO make it smarter 
def validate_student_num(value):
    try:
        num = int(value)
        if len(value)!=8:
            raise ValidationError(
            ('شماره وارد شده معتبر نیست')
        )
    except:    
        raise ValidationError(
            ('شماره وارد شده معتبر نیست')
        )
class Students(models.Model):
    name = models.CharField(max_length=250,verbose_name='نام دانشجو')
    num = models.CharField(max_length=8,verbose_name='شماره دانشجویی',unique=True,validators=[validate_student_num])
    item = models.ManyToManyField(Inter_Item,through='Student_Item')
    objects = models.Manager()
    class Meta:
        verbose_name_plural = "دانشجویان"
        verbose_name="دانشجو"
    def __str__(self):
        return self.name + ' ({}) '.format(self.num)

class Student_Item(models.Model):
    student = models.ForeignKey(Students,on_delete=models.PROTECT)
    item = models.ForeignKey(Inter_Item,on_delete=models.PROTECT,verbose_name = 'آیتم')
    date = models.DateField(verbose_name = 'تاریخ')
    objects = models.Manager()
    class Meta:
        verbose_name_plural = "فعالیت ها"
        verbose_name="فعالیت انجام شده"
    def __str__(self):
        return '{} {}'.format(self.student.name,self.item.__str__())

class Groups(models.Model):
    no = models.ForeignKey(TermNo,on_delete=models.PROTECT,verbose_name='نیمسال ورودی')
    student = models.ManyToManyField(Students,through='Group_Student')
    objects = models.Manager()
    class Meta:
        verbose_name_plural = "گروه ها"
        verbose_name="گروه"
    def __str__(self):
        return '{} {}'.format(self.no," , ".join(str(name) for name in self.student.all()))

class Group_Student(models.Model):
    group = models.ForeignKey(Groups,on_delete=models.PROTECT)
    student = models.OneToOneField(Students,on_delete=models.Model,verbose_name = 'دانشجو ها')
    objects = models.Manager()
    class Meta:
        verbose_name_plural = "گروه دانشجویی"
        verbose_name="دانشجو" 
    def __str__(self):
        return '{}'.format(self.group.no)

class Terms(models.Model):
    init_term = models.OneToOneField(TermNo,verbose_name='ترم ورود دانشجویان',on_delete=models.PROTECT)
    group = models.ManyToManyField(Groups,through='Term_Group')
    inter = models.ManyToManyField(Internship,through='Term_Inter',verbose_name='کارآموزی')
    objects = models.Manager()
    class Meta:
        verbose_name_plural = " گروه بندی ها"
        verbose_name="گروه بندی ورودی های یک نیم سال"
    def __str__(self):
        return '{}'.format(self.init_term)


class Term_Inter(models.Model):
    term = models.ForeignKey(Terms,on_delete=models.PROTECT)
    inter = models.ForeignKey(Internship,on_delete=models.Model,verbose_name = 'کارآموزی ها')
    objects = models.Manager()
    class Meta:
        verbose_name_plural = "کارآموزی ها"
        verbose_name="کارآموزی"
    def __str__(self):
        return '{}'.format(self.inter.__str__())

class Term_Group(models.Model):
    term = models.ForeignKey(Terms,on_delete=models.PROTECT)
    group = models.OneToOneField(Groups,on_delete=models.PROTECT,verbose_name = 'اعضای گروه ها')
    objects = models.Manager()
    class Meta:
        verbose_name_plural = "گروه های دانشجویی این ترم"
        verbose_name="گروه"
    def __str__(self):
        return '{}'.format(self.term.__str__())

