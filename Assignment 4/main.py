import instaloader
import getpass

f = open("follower.txt" , "r")
old_followers = []

for line in f :
    old_followers.append(line)
f.close()

L = instaloader.Instaloader()

username = input("Enter username : ")
password = getpass.getpass("Enter your password : ")

if L . login(username , password) :
    print("--- login successfully ---")
else :
    print("something went wrong !!!")
profile = instaloader.Profile.from_username(L.context , username )

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

for old_followers in old_followers :
    if old_followers not in new_followers :
        print (old_followers)

for new_followers in new_followers :
    if new_followers not in old_followers :
        print(new_followers)

f = open("followers.txt" , "w")
for follower in new_followers :
    f.write(follower + "\n")
f.close()

