'''
for i in range(100):
    if (i%3 == 0):
        print(i)

for i in range(100):
    if  (i == 18):
        break
    print(i)

for i in range(100):
    if (i%3 == 0):
        continue
    print(i)


for i in range(100):
    if (i%2 == 1):
        print(i)

a = 0
a += 1
a = a + 1
'''

#a = 0
#for i in range(1,101):
#    a += i
#print(a)


# for i in range(2,10000001):
#     for s in range(2,i):
#         if (i%s == 0):
#             break
#     else:
#         print(i)
#
# if __name__ == '__main__':
#     a = [15,11,5,7,9,21,65,78,90,35,50,45,38]
#     for i in range(len(a)-1,0,-1):
#         for j in range(i):
#             if (a[j] > a[j+1]):
#                 a[j],a[j+1] = a[j+1],a[j]
#     print(a)
#
# if __name__ == '__main__':
#     i = 1
#     while(i<101):
#         print(i)
#         i = i+1
#

# def cheng_fa(a,b):
#     print(a*b)
#
#
# if __name__ == '__main__':
#     cheng_fa(15,15)

# def jia_fa(a,b):
#     return (a+b)
#
# if __name__ == '__main__':
#     c = jia_fa(212,18)
#     print(c)
#

#
# def aa(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# aa({'name','chenqi'},4,5,6,7,3,d=15,e=3000


# class FangFa():
#
#     def jiafa(self):
#         print('你是风儿')
#
#     def jianfa(self):
#         print('我是沙')
#
#
# if __name__ == '__main__':
#     c = FangFa()
#     c.jiafa()
#     c.jianfa()


# a = 'degrakio'
# print(a[0:8:2])
# print(a[1:8:2])
# print('k' in a)

# a = "姓名，性别，电话，住址"
#
# b = a.split("，")
# print(b)

# e = '   138 8637 1549  '
# print(e.split(' '))
# print(e.strip())
#
# print(e.replace(' ',''))

# class TestOne():
#     def a(self):
#         print("你是风儿")
#
#     def b(self):
#         print("我是沙")
# if __name__ == '__main__':
#     c = TestOne()
#     c.a()
#     c.b()
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=python%20去字符串空格&oq=python%2520%25E5%258E%25BB%25E5%25AD%2597%25E7%25AC%25A6%25E4%25B8%25B2%25E7%25A9%25BA%25E6%25A0%25BC&rsv_pq=91393d7300001d8e&rsv_t=80caTcD38q98Ssa0I4VkBzMSFdP3rqFNB3JW3%2FHcUjf0fdX9RDnZr5mjuLw&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=1&rsv_sug4=2598

# r = "GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1"
#
# print('请求方法：',r.split(' ')[0])
# a = r.split(':')[0]
# print('协议名称：',a.split(' ')[1])
# print('url:',r.split('/')[2])
# b = r.split('/')[3]
# print('请求路径:','/'+b.split('?')[0])
# c = r.split('?')[1]
# print('请求内容:',c.split(' ')[0])
# print('协议版本:',r.split(' ')[2])

# a = [1,2,3,4,5,6,7,8,9]
# b = [11,12,13,14,15,16,17,18,19]
# # a.insert(3,80)
# # a.append(11)
# a.extend(b)
# print(a)
# print(b)

# a = [9,8,3,6,5,4,7,2,1]
# # print(a.pop(-3))
# print(a.remove(5))
# print(a)
#
# a.sort(reverse=True)
# print(a)
# a.sort(reverse=False)
# print(a)
#
# d = {'name':'flag','sex':'man'}
# d['age']=30
# # print(d.pop('sex'))
# # print(d)
# del d['sex']
# d.clear()
# print(d)


# d = {1:'123',2:'234',3:'345'}
# f = {4:'456',5:'567',6:'678'}
#
# d.update(f)
# print(d)
def dang_dang_1(self):
    print('这是dingding1类里面的方法1叮叮当当')

class DingDing1():
    def dang_dang_1(self):
        print('这是dingding1类里面的方法1叮叮当当')

class DingDing2():
    def dang_dang_1(self):
        print('这是dingding2类里面的方法1叮叮当当')
    def dang_dang_2(self):
        print('葫芦娃,葫芦娃, 一根藤上七朵花，风吹雨打都不怕，啦啦啦啦。叮叮当当咚咚当当，葫芦娃，啦啦啦啦')

class DingDing3():
    def dang_dang_1(self):
        print('这是dingding3类里面的方法1叮叮当当')
    def dang_dang_2(self):
        print('这是dingding3类里面的方法2叮叮当当')

f = open("D:\\Python_1908a\\demo\\day01\\test.txt","r",encoding='utf-8')
# a = f.readlines()
# print(a[5])
print(f.readline())
f.close()