import  pymysql
import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt
#查询个人记录
def exeQuery(id,name):
    sql='select * from InfoManage where id=%s and name=%s'
    try:
        ret=cursor.execute(sql,[id,name])
        results=cursor.fetchall()
        for row in results:
            id=row[0]
            sno=row[1]
            name=row[2]
            datd_x=row[3]
            time_x=row[4]
            week=row[5]
            If_ill=row[6]
            If_left=row[7]
            If_WH=row[8]
            print(id,sno,name,datd_x,time_x,week,If_ill,If_left,If_WH)              
    except:
        print("Error:unable to fetch data")
#查询患病月记录   
def Queryill_month():
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id<68001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          month1_ill=i[0]
          print("一月患病人数：",month1_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 68000 and 124001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
           month2_ill=i[0]
           print("二月患病人数：",month2_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 124000 and 184001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          month3_ill=i[0]
          print("三月患病人数：",month3_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 184001 and 200000"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
         month4_ill=i[0]
         print("四月患病人数：",month4_ill)
    except:
       print("Error:unable to fetch data")
#构造柱形图
    X=['Jan','Feb','Mar','Apr']
    Y=[1760,1448,1548,415]
    fig = plt.figure()
    plt.bar(X,Y,0.4,color="green")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("month_ill")
    plt.show()  
    
#查询迁移月记录       
def Queryleft_month():
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id<68001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          month1_left=i[0]
          print("一月迁移人数：",month1_left)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 68000 and 124001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
           month2_left=i[0]
           print("二月迁移人数：",month2_left)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 124000 and 184001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          month3_left=i[0]
          print("三月迁移人数：",month3_left)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 184001 and 200000"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
         month4_left=i[0]
         print("四月迁移人数：",month4_left)
    except:
       print("Error:unable to fetch data")
#构造柱形态
    X=['Jan','Feb','Mar','Apr']
    Y=[2261,1869,2013,537]
    fig = plt.figure()
    plt.bar(X,Y,0.4,color="green")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("month_left")
    plt.show()      
#查询武汉人数记录
def QueryWH_month():
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id<68001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          month1_WH=i[0]
          print("一月武汉人数：",month1_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 68000 and 124001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
           month2_WH=i[0]
           print("二月武汉人数：",month2_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 124000 and 184001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          month3_WH=i[0]
          print("三月武汉人数：",month3_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 184001 and 200000"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
         month4_WH=i[0]
         print("四月武汉人数：",month4_WH)
    except:
       print("Error:unable to fetch data")
#构造柱形图
    X=['Jan','Feb','Mar','Apr']
    Y=[3301,2470,2649,706]
    fig = plt.figure()
    plt.bar(X,Y,0.4,color="green")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("month_WH")
    plt.show()  
    
#查询患病周记录       
def Queryill_week():
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id<14001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week1_ill=i[0]
          print("第一周患病人数：",week1_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 14001 and 28001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week2_ill=i[0]
          print("第二周患病人数：",week2_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 28001 and 42001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week3_ill=i[0]
          print("第三周患病人数：",week3_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 42001 and 56001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week4_ill=i[0]
          print("第四周患病人数：",week4_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 56001 and 70001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week5_ill=i[0]
          print("第五周患病人数：",week5_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 70001 and 84001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week6_ill=i[0]
          print("第六周患病人数：",week6_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 84001 and 98001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week7_ill=i[0]
          print("第七周患病人数：",week7_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 98001 and 112001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week8_ill=i[0]
          print("第八周患病人数：",week8_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 112001 and 126001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week9_ill=i[0]
          print("第九周患病人数：",week9_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 126001 and 140001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week10_ill=i[0]
          print("第十周患病人数：",week10_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 140001 and 154001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week11_ill=i[0]
          print("第十一周患病人数：",week11_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 154001 and 168001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week12_ill=i[0]
          print("第十二周患病人数：",week12_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 168001 and 182001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week13_ill=i[0]
          print("第十三周患病人数：",week13_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 182001 and 196001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week14_ill=i[0]
          print("第十四周患病人数：",week14_ill)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_ill) from InfoManage where If_ill='yes'and id between 196001 and 2000000"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week15_ill=i[0]
          print("第十五周患病人数：",week15_ill)
    except:
       print("Error:unable to fetch data")
    #构造柱形图
    X=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',]
    Y=[361,362,361,363,365,363,363,361,361,359,361,362,363,364,102]
    fig = plt.figure()
    plt.bar(X,Y,0.4,color="green")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("month_ill")
    plt.show()
#查询迁移记录
def Queryleft_week():
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id<14001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week1_lelt=i[0]
          print("第一周迁移人数：",week1_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 14001 and 28001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week2_lelt=i[0]
          print("第二周迁移人数：",week2_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 28001 and 42001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week3_lelt=i[0]
          print("第三周迁移人数：",week3_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 42001 and 56001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week4_lelt=i[0]
          print("第四周迁移人数：",week4_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 56001 and 70001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week5_lelt=i[0]
          print("第五周迁移人数：",week5_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 70001 and 84001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week6_lelt=i[0]
          print("第六周迁移人数：",week6_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 84001 and 98001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week7_lelt=i[0]
          print("第七周迁移人数：",week7_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 98001 and 112001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week8_lelt=i[0]
          print("第八周迁移人数：",week8_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 112001 and 126001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week9_lelt=i[0]
          print("第九周迁移人数：",week9_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 126001 and 140001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week10_lelt=i[0]
          print("第十周迁移人数：",week10_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 140001 and 154001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week11_lelt=i[0]
          print("第十一周迁移人数：",week11_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 154001 and 168001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week12_lelt=i[0]
          print("第十二周迁移人数：",week12_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 168001 and 182001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week13_lelt=i[0]
          print("第十三周迁移人数：",week13_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 182001 and 196001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week14_lelt=i[0]
          print("第十四周迁移人数：",week14_lelt)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_lelt) from InfoManage where If_lelt='yes'and id between 196001 and 2000000"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week15_lelt=i[0]
          print("第十五周迁移人数：",week15_lelt)
    except:
       print("Error:unable to fetch data")
    X=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',]
    Y=[463,466,466,465,469,467,465,467,470,472,469,472,467,469,133]
    fig = plt.figure()
    plt.bar(X,Y,0.4,color="green")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("week_left")
    plt.show()
#查询武汉人数记录
def QueryWH_week():
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id<14001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week1_WH=i[0]
          print("第一周武汉人数：",week1_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 14001 and 28001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week2_WH=i[0]
          print("第二周武汉人数：",week2_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 28001 and 42001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week3_WH=i[0]
          print("第三周武汉人数：",week3_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 42001 and 56001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week4_WH=i[0]
          print("第四周武汉人数：",week4_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 56001 and 70001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week5_WH=i[0]
          print("第五周武汉人数：",week5_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 70001 and 84001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week6_WH=i[0]
          print("第六周武汉人数：",week6_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 84001 and 98001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week7_WH=i[0]
          print("第七周武汉人数：",week7_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 98001 and 112001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week8_WH=i[0]
          print("第八周武汉人数：",week8_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 112001 and 126001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week9_WH=i[0]
          print("第九周武汉人数：",week9_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 126001 and 140001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week10_WH=i[0]
          print("第十周武汉人数：",week10_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 140001 and 154001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week11_WH=i[0]
          print("第十一周武汉人数：",week11_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 154001 and 168001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week12_WH=i[0]
          print("第十二周武汉人数：",week12_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 168001 and 182001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week13_WH=i[0]
          print("第十三周武汉人数：",week13_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 182001 and 196001"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week14_WH=i[0]
          print("第十四周武汉人数：",week14_WH)
    except:
       print("Error:unable to fetch data")
    sql="select count(If_WH) from InfoManage where If_WH='yes'and id between 196001 and 2000000"
    try:
       ret=cursor.execute(sql)
       results=cursor.fetchall()
       for i in  results:
          week15_WH=i[0]
          print("第十五周武汉人数：",week15_WH)
    except:
       print("Error:unable to fetch data")
    #构造柱形图
    X=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',]
    Y=[617,618,618,619,617,618,616,617,619,621,617,619,616,616,178]
    fig = plt.figure()
    plt.bar(X,Y,0.4,color="green")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("week_WH")
    plt.show()
#构造月记录柱形图
def manage_month():
    name_list = ['Jan','Feb','Mar','Apr']
    num_list = [1760,1448,1548,415]
    num_list2 = [2261,1869,2013,537]
    num_list3=[3301,2470,2649,706]
    x = list(range(len(num_list)))
    total_width, n = 0.8, 2
    width = total_width / n
    plt.bar(x, num_list, width=width, label='month_ill', fc='b')
    for i in range(len(x)):
        x[i] += width/2
    plt.bar(x, num_list2, width=width, label='month_left', tick_label=name_list, fc='g')
    for j in range(len(x)):
        x[j]+= width/4
    plt.bar(x, num_list3, width=width/2, label='month_WH', tick_label=name_list, fc='r')
    plt.legend()
    plt.show()
#构造周记录柱形图
def manage_week():
    name_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',]
    num_list = [361,362,361,363,365,363,363,361,361,359,361,362,363,364,102]
    num_list2 = [463,466,466,465,469,467,465,467,470,472,469,472,467,469,133]
    num_list3=[617,618,618,619,617,618,616,617,619,621,617,619,616,616,178]
    x = list(range(len(num_list)))
    total_width, n = 0.8, 2
    width = total_width / n
    plt.bar(x, num_list, width=width, label='week_ill', fc='b')
    for i in range(len(x)):
        x[i] += width/2
    plt.bar(x, num_list2, width=width, label='week_left', tick_label=name_list, fc='g')
    for j in range(len(x)):
        x[j]+= width/4
    plt.bar(x, num_list3, width=width/2, label='week_WH', tick_label=name_list, fc='r')
    plt.legend()
    plt.show()
#连接数据库    
flag=True
print("请选择以下四个操作：\n\n 1、查询个人信息，2、查询患病月记录，\
      3、查询迁移月记录，4、查询武汉居民月记录，5、查询患病周记录,\n\n\
      6、查询迁移周记录,7、查询武汉居民周记录,8、月统计柱形图,9、周统计柱形图，10、结束请按‘00’\n");
while(flag): 
    num=int(input("请输入选择:"))
    conn=pymysql.connect(host="localhost",port=3306,user="root",password="root",database="data",charset="utf8")
    #获取光标
    cursor=conn.cursor()
    while(flag):
#结束查询        
        if(num==00):
            print("结束操作")
            break
#个人信息查询
        elif(num==1):
            id=input("请输入编号：").strip()
            name=input("请输入姓名：").strip()
            exeQuery(id,name)
            break
#患病月查询
        elif(num==2):
            if(flag==True):
                Queryill_month()
                break
#流动月查询
        elif(num==3):
            if(flag==True):
                Queryleft_month()
                break
#武汉月查询
        elif(num==4):
            if(flag==True):
                QueryWH_month()
                break
#患病周查询
        elif(num==5):
            if(flag==True):
                 Queryill_week()
                 break
#流动周查询
        elif(num==6):
            if(flag==True):
                 Queryleft_week()
                 break
#武汉周查询
        elif(num==7):
            if(flag==True):
                 QueryWH_week()
                 break
#月查询
        elif(num==8):
            if(flag==True):
                 manage_month()
                 break
#周查询
        elif(num==9):
            if(flag==True):
                 manage_week()
                 break        
    if(num==00):
        break
#关闭数据库    
cursor.close()
conn.close()

