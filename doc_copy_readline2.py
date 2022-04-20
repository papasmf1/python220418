#정규표현식을 사용
import re 

#원본 로그 파일
f=open('c:\\work\\PV3.txt','rt')
#복사본 로그 파일 
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일(500MB, 1GB)이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''):
    if (re.search("error", line)):
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()








