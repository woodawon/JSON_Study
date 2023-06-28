import json

#Python 객체
json_Object = {
  "id": 1,
  "username": "dawon",
  "email": "woodawon0602@gmail.com",
  "address": {
    "street": "Na gil",
    "suite": "Sangildong304-6",
    "city": "Seoul",
    "zipcode": "05283-0101"
  },
  "admin": False,
  "hobbies": None
}

# dumps() 함수와 dump() 함수의 차이점?
# => dumps() : Python 객체 --> JSON 문자열로 변환
# => dump() : Python 객체 --> JSON 파일에 변환 후 저장

with open('output.json', 'w') as f:
    json.dump(json_Object, f, indent=2)