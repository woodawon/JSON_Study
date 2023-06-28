import json

# loads() 함수와 load() 함수의 차이점?
# => loads() : json 문자열 --> python 객체로 변환
# => load() : json 파일(input.json)의 데이터 --> python 객체로 변환

with open('input.json') as f:
    json_Object = json.load(f) 
    
print(type(json_Object), json_Object)
assert json_Object['id'] == 1
assert json_Object['email'] == 'woodawon0602@gmail.com'
assert json_Object['admin'] is False
assert json_Object['hobbies'] is None