import requests
import bs4,pickle,os,re
import tkinter as tk
from urllib.parse import urlencode
import pyperclip #操作粘贴板
#以上模块记得安装
import getallcshi,getzwei #自己的py

def open_url(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    res=requests.get(url,headers=headers)
    return res
def getxinxi(url):#爬取58同城信息主函数
    res=open_url(url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    #获取招聘信息
    listxx=[]
    listurl=[]
    tager1=soup.find_all('li',class_='job_item clearfix')
    for each in tager1:
        xinxi=""
        
        listurl.append(each.div.div.a['href'])
        for each2 in each.div.div.a.strings:
            xinxi+=each2.strip()
        xinxi=xinxi.strip()
        gongzi=each.div.p.text.strip()[0:-3]
        gongsi=each.div.next_sibling.div.a.text.strip()
        listxx.append(xinxi+' '*(35-len(xinxi.encode('gb18030')))+gongzi+' '*(12-len(gongzi.encode('gb18030')))+gongsi) 
        
    return [listxx,listurl]
        #print(xinxi+' '*(40-len(xinxi.encode('gb2312')))+gongzi+' '*(20-len(gongzi.encode('gb2312')))+gongsi)

def getcity(dict1,city,wu):#取城市在字典中的值
    tmp = dict1
    for k,v in tmp.items():
        if k == city:
            return v
        else:
            if type(v)==type(dict()):
                ret = getcity(v, city, wu)
                if ret is not wu:
                    return ret
    return wu

def getcs(csbjk,zwbjk,yeslabel,xxlb):#将爬取的信息放入tkinter列表
    global count
    global yeshu
    global zhaopxx
    city=csbjk.get()
    list1=open(r'D:\python\python_work\项目\58同城\my_citylist.pkl','rb')
    citylist=pickle.load(list1)
    #print(root.winfo_width())#获取窗口宽度
    #print(root.winfo_height())#获取窗口高度
    while 1:
        diqu=getcity(citylist,city,None)
        if diqu!=None:
            diqu=diqu.split('|')[0]
            break
        else:
            city=input('错误请输入城市:')
    url='http://'+diqu+'.58.com'

    zhiwei=zwbjk.get()
    list2=open(r'D:\python\python_work\项目\58同城\my_zhiweilist.pkl','rb')
    zhiweilist=pickle.load(list2)
    zhiweiurl=zhiweilist[zhiwei]
    #print(url+zhiweiurl)
    res=open_url(url+zhiweiurl)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    tager=soup.find('i',class_='total_page')
    yeshu=tager.string
    yeslabel['text']='一共'+yeshu+'页,当前是第'+str(count)+'页'

    url=url+zhiweiurl+str(count)+'/'
    zhaopxx=getxinxi(url)
    xxlb.delete(0,tk.END)
    for zhaop in zhaopxx[0]:
        xxlb.insert(tk.END,zhaop)
def xiayiye(yeslabel,xxlb):#下一页按钮函数
    global count
    global yeshu
    global zhaopxx
    count+=1
    xxlb.delete(0,tk.END)
    yeslabel['text']='一共'+yeshu+'页,当前是第'+str(count)+'页'
    url='http://hshi.58.com/pugong/pn'+str(count)+'/'
    zhaopxx=getxinxi(url)
    for zhaop in zhaopxx[0]:
        xxlb.insert(tk.END,zhaop)
def shangyiye(yeslabel,xxlb):#上一页按钮函数
    global count
    global yeshu
    global zhaopxx
    count-=1
    xxlb.delete(0,tk.END)
    yeslabel['text']='一共'+yeshu+'页,当前是第'+str(count)+'页'
    url='http://hshi.58.com/pugong/pn'+str(count)+'/'
    zhaopxx=getxinxi(url)
    for zhaop in zhaopxx[0]:
        xxlb.insert(tk.END,zhaop)
def fuzurl(url,top):#复制按钮复制url
    global winkd
    global wingd
    pyperclip.copy(url)
    meg=tk.Toplevel(top)
    meg.title('提示')
    meg.geometry('%dx%d+%d+%d'%(150,100,(winkd-150)/2,(wingd-100)/2))
    tk.Label(meg,text='复制成功,请按Ctrl+C粘贴',anchor='center').grid(row=0,column=0)
    meg.mainloop()
    
def shuangjilistbox(wangmin,xxlb):#tkinter列表被双击函数,同城详细信息
    global winkd
    global wingd
    global zhaopxx
    urlindex=xxlb.curselection()[0]
    url=zhaopxx[1][urlindex]#列表被点击的索引
    res=open_url(url)
    
    cateid=re.search(r"____json4fe._trackURL=.*localcate':'(.*?)','.*;",res.text)[1].split(',')[1]
    querystring=re.search("var ____json4fe =.*?(?:locallist:\[\{dispid:')(.*?)', name.*,infoid:'(.*?)',userid:'(.*?)',linkman.*;",res.text)
    datasq={'infoId':querystring[2],
            'userId':querystring[3],
            'local':querystring[1],
            'cateID':cateid,
            'referUrl':'' ,
            'callback':'jQuery110208506778244349542_1534823551200',
            '_':'1534823551201'}
    geturl='http://statisticszp.58.com/position/totalcount/?'+urlencode(datasq)
    sqrs=open_url(geturl)
    sqrsq=re.search('.*(?:"deliveryCount":)(.*?),"commentCount".*\)',sqrs.text)[1]
    datall={'infoid':querystring[2],
            'userid': '',
            'uname': '',
            'sid': 0,
            'lid': 0,
            'px': 0,
            'cfpath': ''}
    llrsurl='http://jst1.58.com/counter?'+urlencode(datall)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'Host': 'jst1.58.com',
        'Referer': url}
    llrs=requests.get(llrsurl,headers=headers)
    llrsq=re.search('.*(?:total=)(.*)',llrs.text)[1]
    #爬取信息
    tcwz=''
    xxsoup=bs4.BeautifulSoup(res.text,'lxml')
    tager=xxsoup.find_all('div',class_='bread')
    for each in tager:
        for each1 in each.strings:
            tcwz+=each1
    zpgongs=xxsoup.find('div',class_='baseInfo_link').text#公司
    zpzwei=xxsoup.find('div',class_='pos_base_info').text#职位和薪资
    zpgzxx=xxsoup.find('span',class_='pos_name').text#招聘信息
    zptiaoj=xxsoup.find('div',class_='pos_base_condition').text#招聘条件
    gsdiz=xxsoup.find('div',class_='pos-area').text[0:-5]#公司地址
    zpgxsj=xxsoup.find('div',class_='pos_base_statistics').text[0:-17]+'\n'+'浏览:'+llrsq+'人'+' 申请:'+sqrsq+'人'#更新时间,浏览人数,申请人数
    zpzwms=xxsoup.find('div',class_='des').text#职位描述
    zpgsjs=xxsoup.find('div',class_='shiji').text#公司介绍
    #tkinter子窗口部件
    top=tk.Toplevel()
    top.title(tcwz)
    top.resizable(height=False,width=False)
    #print('%d%d'%(winkd,wingd))
    top.geometry('%dx%d+%d+%d'%(330,474,(winkd-599)/2+610,(wingd-474)/2))
    
    tk.Label(top,text='网址',width=6).grid(row=0,column=0,columnspan=3)#第一行第一列列宽为5
    zpurl=tk.Entry(top,width=26)
    zpurl.grid(row=0,column=3,columnspan=23)
    zpurl.insert(tk.END,zhaopxx[1][urlindex])
    tk.Button(top,text='复制',width=8,command=lambda:fuzurl(zhaopxx[1][urlindex],top)).grid(row=0,column=26,columnspan=4,padx=2)
    
    top_zp=tk.LabelFrame(top,text='招聘信息',fg='red',labelanchor='n')
    top_zp.grid(row=1,column=0,columnspan=40)
    top_sb=tk.Scrollbar(top_zp)
    top_sb.grid(row=0,column=22,columnspan=8,sticky='n'+'s')
    xxxx=tk.Text(top_zp,width=44,height=32,wrap=tk.WORD,yscrollcommand=top_sb.set)
    xxxx.grid(row=0,column=0,columnspan=22)
    xxxx.tag_config('tag1',background='yellow',foreground='red',font=('楷体',14))
    xxxx.tag_config('tag2',foreground='blue',font=('叶根友毛笔行书2.0版',16))
    xxxx.tag_config('tag3',foreground='purple',font=('楷体',14))
    xxxx.insert(tk.INSERT,zpgongs,('tag2'))
    xxxx.insert(tk.INSERT,'\n'*2+zpgzxx)
    xxxx.insert(tk.INSERT,'\n'*2)
    xxxx.insert(tk.INSERT,zpzwei,('tag1'))
    xxxx.insert(tk.INSERT,'\n'*2+zptiaoj)
    xxxx.insert(tk.INSERT,'\n'*2+'地址:'+gsdiz)
    xxxx.insert(tk.INSERT,'\n'*2)
    xxxx.insert(tk.INSERT,zpgxsj,('tag3'))
    xxxx.insert(tk.END,'\n'*3+' '*6+'职位描述'+'\n'+zpzwms+'\n'*3+' '*6+'公司介绍'+'\n'*2+zpgsjs)
    top_sb.config(command=xxxx.yview)
    top.mainloop()
    
def shijiansp(fun,**kwds):#事件适配器
    return lambda wangmin,fun=fun,kwds=kwds:fun(wangmin,**kwds)

#全局变量
count=1
yeshu=0
zhaopxx=[]
winkd=0#储存屏幕大小
wingd=0

def main():
    global winkd
    global wingd
    getallcshi.get_allcity()
    getzwei.get_zw()
    #tkinter主窗口部件
    root=tk.Tk()
    root.title('58同城信息获取')
    root.resizable(height=False,width=False)#不允许窗口尺寸改变
    winkd=root.winfo_screenwidth()
    wingd=root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d'%(1000,800,(winkd-599)/2,(wingd-474)/2))#窗口在屏幕居中显示
    #print('%d%d'%(winkd,wingd))
    zhk=tk.Frame(root)
    zhk.pack()
    #第一行
    tk.Label(zhk,text='请输入你要搜索的城市:',fg='blue',width=24).grid(row=0,column=0,columnspan=12)
    csbjk=tk.Entry(zhk)#输入查询城市编辑框
    csbjk.insert(0,'黄石')
    csbjk.grid(row=0,column=12,columnspan=8)
    tk.Label(zhk,text='职 位:',fg='blue',width=6).grid(row=0,column=20,columnspan=6)
    zwbjk=tk.Entry(zhk)
    zwbjk.insert(0,'普工')
    zwbjk.grid(row=0,column=26,columnspan=8)
    sous=tk.Button(zhk,text='搜  索',command=lambda:getcs(csbjk,zwbjk,yeslabel,xxlb))
    sous.grid(row=0,column=34,columnspan=6,pady=2,sticky='w',padx=10) 
    #第二行信息列表占32行
    sb=tk.Scrollbar(zhk)
    sb.grid(row=1,column=36,rowspan=24,columnspan=4,sticky='n'+'s')
    xxlb=tk.Listbox(zhk,height=24,width=72,fg='black',font=('楷体'),yscrollcommand=sb.set,selectbackground='yellow',selectforeground='red',highlightthickness=0)
    xxlb.grid(row=1,column=0,rowspan=20,columnspan=36,padx=2)#招聘列表
    xxlb.bind('<Double-Button-1>',shijiansp(shuangjilistbox,xxlb=xxlb))
    sb.config(command=xxlb.yview)
    #第三行,开始于33行
    shangyiy=tk.Button(zhk,text='上一页',fg='blue',command=lambda:shangyiye(yeslabel,xxlb))
    shangyiy.grid(row=25,column=0,columnspan=6)
    yeslabel=tk.Label(zhk,text='我爱你',fg='red',width=56,font='楷体')
    yeslabel.grid(row=25,column=6,columnspan=28)#一个有多少页,当前是在多少页
    xiayiy=tk.Button(zhk,text='下一页',fg='blue',command=lambda:xiayiye(yeslabel,xxlb))
    xiayiy.grid(row=25,column=34,columnspan=6)
    root.mainloop()

if __name__=='__main__':
    main()

    
    
    
  

