#testing for basic alexa prompt to my api
'''
import requests
GET_URL = "http://localhost:5000/harambe/diagnosis"
GET_DATA = {
    'recipe' : "chicken noodle soup"
}
r = requests.post(GET_URL, json=GET_DATA)
print(r.text)
'''


#testing for passing through food id and inspecting response from food api
'''
def testingid(id):
	myTestString = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/{}/analyzedInstructions".format(id);
	return(myTestString)

myDict = {"john's sphagetti":56, "my mom's sphagetti":69,"Steve's white sauce":21}
print(myDict.keys()[0])
print(testingid(myDict[myDict.keys()[0]]))
'''

#testing for nested dictionary manipulation
'''
def nestedDictManip():
	
	k = [
      {
        "number": 1,
        "step": "Place tuna in a large bowl; set aside. In another large bowl, combine the mayonnaise, cashews, onions, pimientos, green pepper, sour cream, vinegar and salt.",
        "ingredients": [
          {
            "id": 11333,
            "name": "green pepper",
            "image": "https://spoonacular.com/cdn/ingredients_100x100/green-bell-pepper.jpg"
          },
          {
            "id": 4025,
            "name": "mayonnaise",
            "image": "https://spoonacular.com/cdn/ingredients_100x100/mayonnaise.jpg"
          },
          {
            "id": 1056,
            "name": "sour cream",
            "image": "https://spoonacular.com/cdn/ingredients_100x100/sour-cream.jpg"
          },
          {
            "id": 11943,
            "name": "pimiento",
            "image": "https://spoonacular.com/cdn/ingredients_100x100/pimento.jpg"
          },
          {
            "id": 12087,
            "name": "cashews",
            "image": "https://spoonacular.com/cdn/ingredients_100x100/cashews.jpg"
          },
          {
            "id": 2047,
            "name": "salt",
            "image": "https://spoonacular.com/cdn/ingredients_100x100/salt.jpg"
          }
        ],
        "equipment": [
          {
            "id": 404783,
            "name": "bowl",
            "image": "https://spoonacular.com/cdn/equipment_100x100/bowl.jpg"
          }
        ]
      },
      {
        "number": 2,
        "step": "Pour over tuna and toss to coat.",
        "ingredients": [],
        "equipment": []
      },
      {
        "number": 3,
        "step": "Serve with chow mein noodles.",
        "ingredients": [
          {
            "id": 93803,
            "name": "chow mein noodles",
            "image": "https://spoonacular.com/cdn/ingredients_100x100/udon-noodles.png"
          }
        ],
        "equipment": []
      }
    ]
 	Instructions = []
 	InstructionsJson = []
 	for dicts in k:
 		Instructions.append(dicts["step"])
 		InstructionsJson+=dicts["ingredients"]
  	print InstructionsJson
	ingredients = [dicts["name"] for dicts in InstructionsJson]

	return Instructions, ingredients

a, b = nestedDictManip()
print "Instructions: "
print a
print "Ingredients: "
print b
'''

#testing case
'''
import requests
GET_URL = "http://127.0.0.1:5000/harambe/extract_ingredient"
GET_DATA = {
	"recipe": "chicken salad"
}
r = requests.get(GET_URL, params=GET_DATA)
#print r.text
'''
#workable list of receipe
'''
"chow_mein_noodles"
"chicken risotto"

'''
lmafsfda = {"your mom": ["fdsafas", "dfafd","dfasdfas"]}
msdafdsa = {"your siste": ["is hot", "sexy"], "your dad":["buff","stronk"]}
msdafdsa["your siste"] = " ".join(msdafdsa["your siste"])
print msdafdsa.update(lmafsfda)
print lmafsfda
print(msdafdsa)
print "*"*100
m = {"dish1":4114, "dish2":12421, "dish3":51251,"dish4":72353,"dish5":125609}
print(m)
k = m
print(k)
print("New Test 2")
std = {"testCase":[]}
i=0
print(m)
for l in m:
  print(l)
  std["testCase"].append(m.keys()[i])
  i+=1
print(std)
del std["testCase"][0]
print std


del k[k.keys()[2]]
print("Case 1:")
for l in k.keys():
  print(k[l])
print("Case 2:")
print()
del k[k.keys()[0]]
for l in k.keys():
  print(k[l])
print(k)

print("New Test")
other_recipt = {"some": []}
other_recipt["some"].append("your mom")
print other_recipt
other_recipt["some"].append("your dad")
print other_recipt

print("New Test 2")
std = {"testCase":[]}
i=0
print(m)
for l in m:
  print(l)
  std["testCase"].append(m.keys()[i])
  i+=1
print(std)