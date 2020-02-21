#coding:utf-8

'''
>>> 运行环境为Python3 on Linux
>>> 运行环境需要用到nmap工具，请先'apt-get install nmap'
>>> 该程序用到了nmap工具中-vv和-Pn两种处理模式
>>> 该程序能够根据不同主机情况能够得出目标端口的开放情况，开放协议，与开放的服务。
'''
import os

#首先定义nmap工具用到的-Pn，-vv两种端口扫描模式的函数
def nmap(x):
    result = os.popen('nmap -{} {}'.format(x,target)).readlines()  #调用Linux命令行完成对目标主机端口开放情况的捕获
    count = 0                                                      #用于for循环计数
    print('目标端口开放情况为(PORT/STATE/SERVICE/(REASON))：')
    for i in range(len(result)):                                   #对结果的处理          
        try:
            int(result[i][0])
            print(result[i])                                       #依次打印结果
            count += 1                                             #计数以保证能够得到结果
        except ValueError:
            continue
    if x != 'Pn':                                                  #vv模式扫描失败后调用Pn模式扫描
        if not count:                            
            print('该主机屏蔽了Ping请求，调用Pn处理模式再次扫描......')
            nmap('Pn')

if __name__ == '__main__':
    target= input('请正确输入你想扫描的IP地址或域名：') #用户输入需要扫描的IP地址或者域名
    print('扫描开始，请等待扫描结果......')
    nmap('vv')                                                      #首先使用vv模式扫描