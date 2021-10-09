import requests

BASE="http://127.0.0.1:5000/"


data=[{"likes":10,"name":"Sup","views":1000000},
      {"likes":70,"name":"Ban","views":7000000},
      {"likes":80,"name":"ti","views":8000000},
      {"likes":90,"name":"li","views":9000000},
      {"likes":40,"name":"Ananya","views":4000000}]


for i in range(len(data)):
        response=requests.put(BASE+"video/"+str(i),data[i])
        print(response.json())

input()
response=requests.delete(BASE+"video/0")
print(response)		#dont print in json format here
input()
response=requests.get(BASE+"video/4")
print(response.json())