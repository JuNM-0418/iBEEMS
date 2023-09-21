import pandas as pd
import csv
import datetime


'''
min_step은 분단위 설정
hour_step은 시간단위 설정

ex) 1시간 간격이면
min_step = 0
hour_step = 1

ex) 15분 간격이면
min_step = 15
hour_step = 0
'''

min_step = 1
hour_step = 0

# csv파일일 경우 pd.read_csv('여기에 파일 이름을 입력')
df = pd.read_csv('data.csv')

# xlsx파일일 경우 pd.read_excel("여기에 파일 이름을 입력")
# df = pd.read_excel('data.csv')

start_time = datetime.datetime.strptime(
    df.loc[len(df)-1][0], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=hour_step, minutes=min_step)
f = open("result.csv", "a", newline="", encoding="utf-8")
wr = csv.writer(f, lineterminator='\n')
wr.writerow(["time", "average"])


sum = 0
average = 0
times = 0


for i in range(len(df)-1, -1, -1):
    if start_time > datetime.datetime.strptime(df.loc[i][0], '%Y-%m-%d %H:%M:%S'):
        sum += df.loc[i][1]
        times += 1
    else:
        if times == 0:
            average = 0
        else:
            average = sum / times
        wr.writerow(list([datetime.datetime.strptime(
            df.loc[i][0], '%Y-%m-%d %H:%M:%S'), average]))
        sum = 0
        times = 0
        average = 0
        start_time = datetime.datetime.strptime(
            df.loc[i][0], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=hour_step, minutes=min_step)
f.close()
