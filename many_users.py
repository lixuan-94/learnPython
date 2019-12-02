users = {
	'aeinstein' : {
		'first' : 'albert',
		'last' : 'einstein',
		'location' : 'princeton',
		},

	'mcurie' : {
		'first' : 'marie',
		'last' : 'curie',
		'location' : 'paris',
	},
}

for username, userinfo in users.items():
	print("Username: " + username)

	fullname = userinfo['first'].title() + " " + userinfo['last'].title()
	print("Fullname: " + fullname)
	print("Location: " + userinfo['location'].title() + "\n")