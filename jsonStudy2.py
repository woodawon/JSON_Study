import json

# Python  객체
json_Object = {
    
    "id" : 1,
    "username" : "dawon",
    "email" : "woodawon0602@gmail.com",
    "address" : {
        "street" : "Na gil",
        "suite" : "Sangildong304-6",
        "city" : "Seoul",
        "zipcode" : "05283-0101"
    },
    "admin" : False,
    "hobbies" : None
    
}

# dumps() 함수 -> Python 객체를 JSON 문자열로 변환함
json_String = json.dumps(json_Object) 
json_String2 = json.dumps(json_Object, indent=2) 

print("json_String Type : " , type(json_String))
print(json_String)
print(json_String2)

print("json_Object Type : " , type(json_Object))
print(json_Object) 