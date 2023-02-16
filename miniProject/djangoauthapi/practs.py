#
# from collections import namedtuple, deque, OrderedDict, defaultdict, ChainMap, Counter
# #
# # l = [10,58,64,78]
# # l = deque(l)
# # l.rotate(2)
# # print(l)
#
# #
# # t = namedtuple('marks',['phy','chem','bio','math'])
# # npt = t(52,84,68,57)
# # print(t)
# #
# # print(npt)
# # print(npt[2])
# # print(npt.math)
# #
# # import random
# # ls = [random.randint(10,15) for i in range(10)]
# # ls1 = [ random.randint(10,15) for i in range(10)]
# # print(ls)
# # print('ls1-->',ls1)
# # cnt = Counter(ls)
# # cnt1 = Counter(ls1)
# # print(cnt)
# # print(cnt1)
# # # mcmn3=cnt.most_common(3)
# # # print(mcmn3)
# #
# # sub = cnt-cnt1
# # print(sub)
# # d = {3:45,8:95,7:45}
# # d1 = defaultdict(tuple,d)
# # print(d1[2])
# # print(d1)
# # d2 = d1.setdefault(9,'xxx')
# # print(d1)
#
# # d ={10:6584,20:445,'ma':2455}
# # print(d)
# # d = OrderedDict(d)
# # print(d)
# # d.move_to_end(10)
# # print(d)
# # d.setdefault(4,'xxxxx')
# # print(d)
# # d.popitem()
# # print(d)
#
#
# d1 = {11: 'FFF', 12: 200, 13: 300}
# d2 = {24: 400, 25: 500, 1: 1002, 2: 2002, 3: 3001}
# d3 = {33: 300, 34: 400, 35: 500, 1: 1003, 3: 3002}
# d4 = ChainMap(d1,d2,d3)
# cmaps = d4.maps
# print('maps==>',cmaps)
# cmaps[1][786]='llllllllll'
# print(cmaps)
# print(d4)
# # d4 = {}
# # d4 = {**d1,**d2,**d3}
# # print(d4)
# d4[88888]='chava'
# print(d4)
# chmps = d4.parents
# chmps[99]='mahesh'
# print(chmps)
# d5 = {505:55,606:66}
# nwchld=chmps.new_child(d5)
# print(nwchld)
#
# ans = chmps.get(36666)
# print(ans)

from itertools import cycle,repeat,count,product,permutations,combinations,combinations_with_replacement\
    ,chain,compress,islice,groupby,tee,accumulate,filterfalse,dropwhile,takewhile,starmap,zip_longest

l = [10,5,75,96]
# l1 = repeat(l,3)
# print(list(l1))
#
# for i in count(10):
#     if i==50:
#         break
#     else:
#         print(i)


# cnt=0
# for x in cycle(l):
#     if cnt>10:
#         break
#     else:
#         cnt+=1
#         print(x,end=' ')
#
# l1 = [10,20]
# l2 = [10,20,30,40]
# p = product(l1,l2)
# print(list(p))
#
# pe = permutations(l2,r=2)
# print(list(pe))
# c = combinations(l2,r=2)
# print(list(c))
# cr = combinations_with_replacement(l2,r=2)
# print(list(cr))

# drpw=dropwhile(lambda x:x<20,[i for i in range(10,30)])
# print(list(drpw))
#
# tkwhl = takewhile(lambda x:x<20,[i for i in range(10,30)])
# print(list(tkwhl))
#
# fltr = list(filter(lambda x:x%2==0,[i for i in range(10,20)]))
# print(fltr)
#
# fltrfls = list(filterfalse(lambda x: x%2==0, [i for i in range(10,30)]))
# print(fltrfls)

# l1 = [i for i in range(10,21)]
# l2 = ['mahesh','jaggu',60,'rashi',50.633,'amol','ashu','rutu']
# zp = zip_longest(l1,l2,fillvalue='-')
# print(dict(zp))
#
# li = [2, 4, 6, 7, 8, 10, 20]
# ans =list(tee(li,3))
# print(ans)


l1 = [i for i in range(10,21)]
l2 = ['mahesh','jaggu',60,'rashi',50.633,'amol','ashu','rutu']
# ac = accumulate(l1,lambda x,y:x+y)
# print(list(ac))

# l = [(10,20,30),(50,60,40),(70,80,60),(200,90,100)]
# mp = starmap(lambda a,b,c,:(a*2,b*3,c*4),l)
# print(list(mp))
#
# ch = chain('maheshmore','akshata')
# print(list(ch))
# cmprs = compress('maheshmore',selectors=[1,0,0,1,0,1,1,0,1,0])
# print(list(cmprs))
#
# l = [i for i in range(10,21)]
# islc = list(islice(l,2,7))
# print(islc)

# def decor(func):
#     def inner(a,b):
#         if type(a)==int and type(b)==int:
#             if a<b:
#                 a,b=b,a
#                 print('*'*30)
#                 func(a,b)
#                 print('*'*30)
#             else:
#                 print('*'*30)
#                 func(a,b)
#                 print('*'*30)
#         else:
#             print("Please provide integer values.")
#     return inner
# def decor2(func):
#     def inner(x,y):
#         print('#'*30)
#         func(x,y)
#         print('#'*30)
#     return inner
#
# @decor2
# @decor
# def add(a,b):
#     print("Difference-->",a-b)
#
# add(50,100)


#
# def generate_num(limit):
#     a,b=0,1
#     while a<=limit:
#         yield a
#         a,b = b,a+b
#
# gen = generate_num(15)

# for x in gen:
#     print(x,end=' ')
#

# def closure(message):
#     msg = message
#     def inner():
#         print(msg)
#     return inner
#
# c = closure('hellooo')
# c()


#emp --> id name salary      cmpny --> id  name  address  empid
#Employee                        Company

# Company.objects.all().select_related('employee')
# Company.objects.select_related('employee')
# Employee.objects.all().prefetch_related('company')
# Employee.objects.prefetch_related('company')
#
# Employee.objects.create(id=1,name='mahesh',salary=95000)
# Employee.objects.bulk_create(
#     Employee(id=2,name='Aniket',salary=70000),
#     Employee(id=3,name='Akshay',salary=50000),
#     Employee(id=4,name='Anuj',salary=70000),
#     Employee(id=5,name='Sikandar',salary=80000),
# )
#
# Employee.objects.get(id=13).delete()
#
#
#
#
# Employee.objects.get(id=15).update(name='ravish',salary=9000)
#
# Employee.objects.filter(name__icontains='hes')
# Employee.objects.filter(name__startswith='M')
# Employee.objects.filter(id__range=(10,50))
# Employee.objects.filter(id__in = [10,20,30,40])
#
# stud_data=Students.objects.all()
#
# avg_marks= stud_data.aggregate(Avg(stud_marks))
#
# studs = Students.objects.all()[:5]
#
# Employee.objects.filter(joiningDate__date = date(2022,02,12))
# Employee.objects.filter(joining__year = 2022)
# Employee.objects.filter(joining__month = 5)
# Employee.objects.filter(Q(joinigdate__date__gt = date(2022,02,01) & Q(joiningdate__date__lt=date(2023,02,01)) ))

from collections import defaultdict,Counter,OrderedDict

### matrix -->

no_rows = int(input("Enter the number of rows: "))

x=1
for i in range(1,no_rows+1):
    for j in range(1,i+1):
        print(x, end=' ')
        x = x + 1
    print()

# for i in range(no_rows-1,0,-1):
#     for j in range(1,i+1):
#         print(chr(ch+i), end=' ')
#     print()

