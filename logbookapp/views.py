from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import jwt
from .models import Masters,Inter_Dep ,Term_Inter, Students,Internship,Term_Inter,Terms,Groups,Term_Group,Group_Student,Student_Item,Inter_Item,Items,IntershipsWithItems,Terms,TermNo
# TODO fucking rename intership to internship


# /app/login (prefix app was my fuking mistake)
#   POST, returns a json
#   input: username,password
#   output: status:ok, token: ,name:
@csrf_exempt
@require_POST
def login(request):
    # TODO change username and num names for security
    # My teribble mistake was in using postman
    # i should set my params in body -> form-data
    try:
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        obj = Masters.objects.get(username=Username)
        if Username==obj.username and Password==obj.password:
            # TODO find best way for check empety token
            if obj.token=='token':
                # TODO remove it before publishing on github
                secret = 'qwertyuiop'
                token = jwt.encode({
                    'username': obj.username,
                    'password':obj.password,
                }, secret, algorithm='HS256')
                obj.token =token
                obj.save()
            return JsonResponse({
                'status':'ok',
                'token':str(obj.token),
                'name':obj.name,
                })
        # At first i forgot this return inside if block and its caused http 500 error
        return JsonResponse({
            # TODO change it to just `error` for security
            'status':'error',
            })        
    except:
        return JsonResponse({
            # TODO change it to just `error` for security
            'status':'error',
            })

@csrf_exempt
@require_POST
def get_terms(request):
    terms = {}
    master = Masters.objects.get(username=request.POST.get('username')) # request.POST.get('username')
    now = TermNo.objects.get(term= max(TermNo.objects.values_list('term',flat=True)))
    inter_dep_list = Inter_Dep.objects.filter(master=master)
    for inter_dep in inter_dep_list:
        for term_inter in Term_Inter.objects.filter(inter=inter_dep.inter):
            terms[get_term_num(term_inter.term.init_term.term,now.term)]=''

    return JsonResponse({
        'terms':list(terms.keys())
    })

@csrf_exempt
@require_POST
def get_groups(request):
    now = TermNo.objects.get(term= max(TermNo.objects.values_list('term',flat=True)))
    term = TermNo.objects.get(term=str(num_to_term(request.POST.get('term'),str(now))))
    groups = []
    for g in Groups.objects.filter(no=term):
        students = {}
        for s in g.student.all():
            students[s.num] = s.name
        studentskv = []
        for k,v in students.items():
            stu = {}
            stu['name'] = v
            stu['num'] = k
            studentskv.append(stu)
        groups.append(studentskv)

    return JsonResponse({
        'groups':groups,
    },json_dumps_params={'ensure_ascii':False})


@csrf_exempt
@require_POST
def get_items(request):
    student = Students.objects.get(num=str(request.POST.get('no')))
    print(student.name)
    gs = Group_Student.objects.get(student=student)
    t = Term_Group.objects.get(group=gs.group).term
    inter_list = t.inter.all()
    items = []
    for inter in inter_list:
        interList = []
        for inter_item in Inter_Item.objects.filter(inter=inter.name):
            item = {}
            item['name'] = inter_item.item.name
            item['inter'] = inter_item.inter.name
            item['id'] = inter_item.id
            item['count'] = 0
            item['min'] = inter_item.min_no
            for i in student.item.all():
                if i.item == inter_item.item:
                    item['count'] += 1
            interList.append(item)
        d = {'name':inter.name.name,'items':interList}
        items.append(d)
        

    return JsonResponse({
        'items': items,
    })



# app/master
def get_master(request):
    # TODO explain this code 
    this_master = Masters.objects.get(username='test')
    this_inter_dep_list = list(Inter_Dep.objects.filter(master=this_master))
    interships=[]
    for this_inter_dep in this_inter_dep_list:
        this_inter_list = []
        this_inter_list.extend(list(Internship.objects.filter(inter_dep=this_inter_dep)))
        for this_inter in this_inter_list:
            this_term_list = []
            this_term_list.extend(list(Terms.objects.filter(inter=this_inter)))
            for this_term in this_term_list:
                this_term_group_list = []
                this_term_group_list.extend(list(Term_Group.objects.filter(term=this_term)))
                this_student_list=[]
                for this_term_group in this_term_group_list:
                    this_group_student_list = []
                    this_group_student_list.extend(list(Group_Student.objects.filter(group=this_term_group.group)))
                    for this_group_student in this_group_student_list:
                        stu={}
                        stu["name"]=this_group_student.student.name
                        stu["num"]=this_group_student.student.num
                        items={}
                        Student_Item_list = []
                        Student_Item_list = list(Student_Item.objects.filter(student=this_group_student.student))
                        # Collect all items
                        allItem = list(Inter_Item.objects.filter(inter=this_inter.name))
                        for i in allItem:
                            items[i.item.name]=0                        
                        # TODO remember this
                        # Counting Items 
                        for i in Student_Item_list:
                            if i.item.inter == this_inter.name:    
                                items[i.item.item.name] += 1
                        # Removing repeated items
                        itemskv=[]
                        for k,v in items.items():
                            # So odd! it worked with one try!
                            item = Items.objects.get(name=k)
                            min = Inter_Item.objects.get(inter=this_inter.name,item=item).min_no
                            itemskv.append({'name':k,'count':v,'min':min})
                        stu["items"]=itemskv
                        this_student_list.append(stu)
                    # 
                    inter={}
                    inter['name']=this_inter.name.name
                    inter['term']=this_inter.term.term
                    inter['students']=this_student_list
                    interships.append(inter)
                    
    # Removing repeated Interships and appending to interskv
    inters={}
    interskv=[]
    for inter in interships:
        inters[inter['name']]=inter
    for k,v in inters.items():
        interskv.append({'name':k,'term':v['term'],'students':v['students']})

    # TODO httpresponse should be
    # return HttpResponse(encrypt(interskv))

    #TODO remember Return json response by utf8  
    return JsonResponse({
        # 'hash':myhash.decode("utf-8") ,
        # 'unhash':str(unhash),
        'status':'ok',
        'interships': interskv,
    },json_dumps_params={'ensure_ascii':False})


# TODO use fonts
# HTML table for interships plan
def get_plan(request):
    now = TermNo.objects.get(term= max(TermNo.objects.values_list('term',flat=True)))
    print(now)
    myPage = '<!DOCTYPE html><html dir="rtl" align="center"><head><style> @media print {.pagebreak { page-break-before: always; }} @font-face {font-family: "Roboto";src: url("/home/sadegh/w/logbook/lbenv/lib/python3.7/site-packages/django/contrib/admin/static/admin/fonts/Nazanin.ttf");font-weight: 400;font-style: normal;} p {font-family: Roboto;font-size: 2.2vw;} table, th, td {font-family: Roboto ;font-size: 1.9vw ;border: 0.2vw solid black;border-collapse: collapse;align: center;padding:0.5vw;}</style></head><body>'
    for this_term in Terms.objects.all():
        myPage += '<p>برنامه کارآموزی ترم {}</p>'.format(persian_int(get_term_num(this_term.init_term.term,now.term)))
        myPage += '<table align="center">'
        interDepList = []
        for inter in this_term.inter.filter(term=now):
            interDepList.extend(Inter_Dep.objects.filter(inter=inter))
        myPage += '<tr style="border: 0.3vw solid black;"><td style="border: 0.3vw solid black;"></td>'
        if len(interDepList) <= len(this_term.group.all())/2 :
            for i in interDepList:
                myPage += '<td style="border: 0.3vw solid black;">{}</td>'.format(i.dep.name)
            myPage += '</tr>'
            myPage += '<tr><td></td>'
            for i in interDepList:
                myPage += '<td>{}</td>'.format(' - ')
            myPage += '</tr>'
            for group in this_term.group.all():
                myPage += '<tr><td width ="40%" align="right" style="white-space: nowrap;font-size:1.6vw;">'
                sn = 1
                for student in group.student.all():
                    myPage += '{}. {}<br>'.format(persian_int(sn),student.name)
                    sn += 1
                myPage += '</td>'
                for i in interDepList:
                    myPage += '<td style="font-size:1.6vw;">{}<span style="font-size:1.5vw;"> لغایت </span>{}</td>'.format(persian_int(str(i.from_date)[2:]),persian_int(str(i.to_date)[2:]))
                interDepList.insert(0,interDepList[-1])
                interDepList.pop()
                myPage += '</tr>'
            myPage += '</table><br>'

        else :
            for i in interDepList:
                myPage += '<td style="font-size:1.5vw;">{}<br><span style="font-size:1.5vw;">لغایت</span><br>{}</td>'.format(persian_int(str(i.from_date)[2:]),persian_int(str(i.to_date)[2:]))
            myPage += '</tr>'
            myPage += '<tr><td></td>'
            for i in interDepList:
                myPage += '<td>{}</td>'.format(' - ')
            myPage += '</tr>'
            for group in this_term.group.all():
                myPage += '<tr><td width ="20%" align="right" style="white-space: nowrap;font-size:1.6vw;">'
                sn = 1
                for student in group.student.all():
                    myPage += '{}. {}<br>'.format(persian_int(sn),student.name)
                    sn += 1
                myPage += '</td>'
                for i in interDepList:
                    myPage += '<td>{}</td>'.format(i.dep.name)
                interDepList.insert(0,interDepList[-1])
                interDepList.pop()
                myPage += '</tr>'
            myPage += '</table><br>'



        # Masters
        myPage += '<table align="center"><tr><td>{}</td>'.format('بخش')
        for i in interDepList:
            if i.dep.name != 'off':
                myPage += '<td>{}</td>'.format(i.dep.name)
        myPage += '</tr><tr><td>{}</td>'.format('مربی')
        for i in interDepList:
            if i.dep.name != 'off':
                m = ''
                for mas in i.master.all():
                    m += mas.name+'، '
                myPage += '<td style="font-size:1.5vw;">{}</td>'.format(m[0:-2])
        myPage += '</tr></table><br><br><div class="pagebreak"></div><br>'
    myPage += '<div align="center" style="position: fixed; bottom: 0; width:100%; text-align: center">{}</div></body></html>'.format('') # copy right: SA
    
    return HttpResponse(myPage)

import json
from jalali_date import date2jalali
import datetime
@csrf_exempt
@require_POST
def save_items(request):
    # try:
    r = json.loads(request.POST.get('items'))
    s = request.POST.get('student')
    t = datetime.datetime.now().date()
    stu = Students.objects.get(num=s)
    for k,v in r.items():
        for _ in range(int(v)):
            i = Inter_Item.objects.get(id=k)
            S = Student_Item(student=stu,item=i,date=t)
            S.save()
            print(stu.name)
    return HttpResponse('ok')
    # except:
    #     return HttpResponse('erroe')

    

def get_term_num(initTerm,now):
    return (int(now[:2])-int(initTerm[:2])-1)*2+(2+int(now[-1:])-int(initTerm[-1:]))+1

def num_to_term(n,now):
    num = int(n) - 1
    res = int(now[-1:])-int(num%2)
    if res == 0:
        print((int(now[:2])-int(num/2)-1)*10 + 2)
        return (int(now[:2])-int(num/2)-1)*10 + 2
    else:
        print((int(now[:2])-int(num/2))*10 + 1)
        return (int(now[:2])-int(num/2))*10 + 1

def encrypt(data):
    import base64
    from cryptography.fernet import Fernet
    key2_ = bytes('12345678901234567890123456789012','utf-8')
    key2 = base64.b64encode(key2_)
    myhash = Fernet(key2).encrypt(bytes(str(data),'utf-8'))
    # str(myhash) return "b'AAA..." but decode() not
    return myhash.decode('utf-8')

def persian_int(english_int):
    devanagari_nums = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    number = str(english_int)
    return ''.join(devanagari_nums[int(digit)] if digit.isdigit() else '/' for digit in number)