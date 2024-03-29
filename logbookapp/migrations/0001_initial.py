# Generated by Django 3.0.2 on 2020-01-08 18:08

from django.db import migrations, models
import django.db.models.deletion
import logbookapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='نام بخش')),
                ('details', models.TextField(blank=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'بخش',
                'verbose_name_plural': 'بخش ها',
            },
        ),
        migrations.CreateModel(
            name='Group_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'دانشجو',
                'verbose_name_plural': 'گروه دانشجویی',
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'گروه',
                'verbose_name_plural': 'گروه ها',
            },
        ),
        migrations.CreateModel(
            name='Inter_Dep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(verbose_name='تاریخ شروع')),
                ('to_date', models.DateField(verbose_name='تاریخ پایان')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.Departments', verbose_name='بخش')),
            ],
            options={
                'verbose_name': 'بخش',
                'verbose_name_plural': 'برنامه بخش ها',
            },
        ),
        migrations.CreateModel(
            name='Inter_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_no', models.PositiveSmallIntegerField(default=1, verbose_name='حداقل تعداد')),
            ],
            options={
                'verbose_name': 'آیتم',
                'verbose_name_plural': 'آیتم های کارآموزی',
            },
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ManyToManyField(through='logbookapp.Inter_Dep', to='logbookapp.Departments')),
            ],
            options={
                'verbose_name': 'کارآموزی',
                'verbose_name_plural': 'کارآموزی ها',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='نام آیتم')),
            ],
            options={
                'verbose_name': 'آیتم',
                'verbose_name_plural': 'آیتم ها',
            },
        ),
        migrations.CreateModel(
            name='Masters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='نام استاد')),
                ('username', models.CharField(help_text='با حروف لاتین', max_length=60, verbose_name='نام کاربری')),
                ('password', models.CharField(help_text='رمز عبور برای وراد شدن استاد به سامانه', max_length=250, verbose_name='رمز عبور')),
                ('token', models.CharField(default='token', max_length=64)),
            ],
            options={
                'verbose_name': 'استاد',
                'verbose_name_plural': 'اساتید',
            },
        ),
        migrations.CreateModel(
            name='Student_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.Inter_Item', verbose_name='آیتم')),
            ],
            options={
                'verbose_name': 'فعالیت انجام شده',
                'verbose_name_plural': 'فعالیت ها',
            },
        ),
        migrations.CreateModel(
            name='Term_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.Groups', verbose_name='اعضای گروه ها')),
            ],
            options={
                'verbose_name': 'گروه',
                'verbose_name_plural': 'گروه های دانشجویی این ترم',
            },
        ),
        migrations.CreateModel(
            name='Term_Inter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inter', models.OneToOneField(on_delete=models.Model, to='logbookapp.Internship', verbose_name='کارآموزی ها')),
            ],
            options={
                'verbose_name': 'کارآموزی',
                'verbose_name_plural': 'کارآموزی ها',
            },
        ),
        migrations.CreateModel(
            name='TermNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(help_text='سه رقمی و لاتین وارد شود. مانند: 962', max_length=4, unique=True, verbose_name='ترم')),
            ],
            options={
                'verbose_name': 'ترم',
                'verbose_name_plural': 'ترم ها',
            },
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ManyToManyField(through='logbookapp.Term_Group', to='logbookapp.Groups')),
                ('init_term', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.TermNo', verbose_name='ترم ورود دانشجویان')),
                ('inter', models.ManyToManyField(through='logbookapp.Term_Inter', to='logbookapp.Internship', verbose_name='کارآموزی')),
            ],
            options={
                'verbose_name': 'گروه بندی ورودی های یک نیم سال',
                'verbose_name_plural': ' گروه بندی ها',
            },
        ),
        migrations.AddField(
            model_name='term_inter',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.Terms'),
        ),
        migrations.AddField(
            model_name='term_group',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.Terms'),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='نام دانشجو')),
                ('num', models.CharField(max_length=8, unique=True, validators=[logbookapp.models.validate_student_num], verbose_name='شماره دانشجویی')),
                ('item', models.ManyToManyField(through='logbookapp.Student_Item', to='logbookapp.Inter_Item')),
            ],
            options={
                'verbose_name': 'دانشجو',
                'verbose_name_plural': 'دانشجویان',
            },
        ),
        migrations.AddField(
            model_name='student_item',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.Students'),
        ),
        migrations.CreateModel(
            name='IntershipsWithItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='نام مدل کارآموزی')),
                ('item', models.ManyToManyField(through='logbookapp.Inter_Item', to='logbookapp.Items')),
            ],
            options={
                'verbose_name': 'مدل کارآموزی',
                'verbose_name_plural': 'مدل های کارآموزی',
            },
        ),
        migrations.AddField(
            model_name='internship',
            name='name',
            field=models.ForeignKey(help_text='مدل کارآموزی را انتخاب کنید', on_delete=django.db.models.deletion.PROTECT, to='logbookapp.IntershipsWithItems', verbose_name='کارآموزی'),
        ),
        migrations.AddField(
            model_name='internship',
            name='term',
            field=models.ForeignKey(help_text='ترمی که میخواهید این کارآموزی در آن ثبت شود', on_delete=django.db.models.deletion.PROTECT, to='logbookapp.TermNo', verbose_name='ترم کنونی'),
        ),
        migrations.AddField(
            model_name='inter_item',
            name='inter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.IntershipsWithItems'),
        ),
        migrations.AddField(
            model_name='inter_item',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.Items', verbose_name='آیتم'),
        ),
        migrations.AddField(
            model_name='inter_dep',
            name='inter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.Internship'),
        ),
        migrations.AddField(
            model_name='inter_dep',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.Masters', verbose_name='استاد'),
        ),
        migrations.AddField(
            model_name='groups',
            name='no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.TermNo', verbose_name='نیمسال ورودی'),
        ),
        migrations.AddField(
            model_name='groups',
            name='student',
            field=models.ManyToManyField(through='logbookapp.Group_Student', to='logbookapp.Students'),
        ),
        migrations.AddField(
            model_name='group_student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logbookapp.Groups'),
        ),
        migrations.AddField(
            model_name='group_student',
            name='student',
            field=models.OneToOneField(on_delete=models.Model, to='logbookapp.Students', verbose_name='دانشجو ها'),
        ),
        migrations.AlterUniqueTogether(
            name='internship',
            unique_together={('name', 'term')},
        ),
        migrations.AlterUniqueTogether(
            name='inter_item',
            unique_together={('inter', 'item')},
        ),
        migrations.AlterUniqueTogether(
            name='inter_dep',
            unique_together={('inter', 'dep', 'from_date', 'to_date')},
        ),
    ]
