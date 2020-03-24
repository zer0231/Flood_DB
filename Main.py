import requests
import random

def random_data():
	first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']
	last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']
	rn_num = random.randint(100, 999)
	first = random.choice(first_names)
	last = random.choice(last_names)
	full_name = first+" "+last
	passw = str(rn_num)+first.lower()
	email = first.lower() + last.lower() + '@gmail.com'
	return full_name,passw,email   

def main():
	url = input("Enter the url of the add.php")
	r = requests.get(url)
	if r.status_code != 200:
		print("\nURL refuses")
	else:
   		print("Loading") 
   		while True:
   				full_name,passw,email=random_data()
   				rn_data = {'txtname':full_name,'txtemail':email,'txtpassword':passw}
   				x = requests.post(url, data = rn_data)
   				print("\n")


if __name__ == '__main__':
	main()