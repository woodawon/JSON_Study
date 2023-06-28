import json

# JSON 문자열
json_String = '''{ 
    
    "id" : 1,
    "username" : "dawon",
    "email" : "woodawon0602@gmail.com",
    "address" : {
        "street" : "Na gil",
        "suite" : "Sangildong304-6",
        "city" : "Seoul",
        "zipcode" : "05283-0101"
    },
    "admin" : false,
    "hobbies" : null
    
}'''

print("Here's a string things of json_String ! " + "\n" + json_String)

# loads() 함수 -> JSON 문자열을 Python 객체로 변환
json_Object = json.loads(json_String)

print("json_String Type : ", type(json_String))
print("json_Object Type : ",type(json_Object))

assert json_Object['id'] == 1
assert json_Object['email'] == 'woodawon0602@gmail.com'
assert json_Object['admin'] is False
assert json_Object['hobbies'] is None