"""
컨슈머 클러스터에서 하루치 데이터를 계속 적재하고
일정 시간이 넘어가면 s3에 적재?

"""

import boto3
import datetime

s3 = boto3.client('s3')
#s3 = boto3.resource('s3')


try:
    time = datetime.datetime.now().strftime("%Y-%d-%m")
    input_data = open(time + '.txt', 'w')

    for num in range(20):
        input_data.write(str(num) + '\n')
    input_data.close()
    s3.upload_file(input_data.name, "dataflowinput", input_data.name)
    
except Exception as err:
    print("input error", err)
