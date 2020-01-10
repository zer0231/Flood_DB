import requests
import random

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

url = input("Enter the url of the add.php")

r = requests.get(url)

print(r.status_code)

if r.status_code != 200:
    print("\nbhdsk correct url de")
else:
   print("Loading") 
   while :
        rn_num = random.randint(100, 999)
        first = random.choice(first_names)
        last = random.choice(last_names)
        full_name = first+" "+last
        passw = str(rn_num)+first.lower()
        email = first.lower() + last.lower() + '@gmail.com'
        rn_data = {'txtname':full_name,'txtemail':email,'txtpassword':passw}
        x = requests.post(url, data = rn_data)
        print(".\n")

