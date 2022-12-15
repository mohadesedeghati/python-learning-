import instaloader
import getpass


f= open("followers.txt", "r")
previous_followers=[]
for line in f:
    previous_followers.append(line)
f.close


L=instaloader.Instaloader()

user_name=input("please enter your username: ")
pass_word= getpass.getpass("enter password: ")
L.login(user_name,pass_word)
print("login was succesful")


profile=instaloader.Profile.from_username(L.context,"mohadese_deghati")

new_followers=[]
for follwer in profile.get_followers():
    new_followers.append(follwer)

for new_follower in new_followers:
    if new_follower not in previous_followers:
        print(new_follower)

f=open("followers.txt", "w")
for follower in new_follower:
    f.write(follower+ "\n")
f.close()


