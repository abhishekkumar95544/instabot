import requests, urllib

APP_ACCESS_TOKEN = '2170149923.5a5863d.94363ab14ad940019bfbc7a0cb8cfa3b'
#Token Owner : AVinstaBot.main
#Sandbox Users : AVinstaBot.test0, AVinstaBot.test1, AVinstaBot.test2...... AVinstaBot.test10

BASE_URL = 'https://api.instagram.com/v1/'

'''
Function declaration to get your own info
'''
#function declaration

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
#user info
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            #else user doesnot exist
            print 'User does not exist!'
    else:
        #printing the status of code
        print 'Status code other than 200 received!'


'''
Function declaration to get the ID of a user by username
'''

#geting the user details
def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
#detailing of the use info
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        #printing the status of the code
        print 'Status code other than 200 received!'
        exit()


'''
Function declaration to get the info of a user by username
'''

#defining the user
def get_user_info(vivekkumar3075):
    user_id = get_user_id(vivekkumar3075)
    if user_id == 1:
        print 'User  exist!'
        exit()
        #requesting the url
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
#printing the get request
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
#user whole details
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
          #printing the user name
            print 'Username: %s' % (user_info['data']['username'])
            #printing the number of follower
             print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
             #printing number of people
             print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            #printing number of post
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            #if yes then print the data for user
            print 'There is no data for this user!'
    else:
        #printing the status of code
        print 'Status code other than 200 received!'


'''
Function declaration to get your recent post
'''


def get_own_post():
    #requesting base url
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
#in case of own media
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            #image name
            image_name = own_media['data'][0]['id'] + '.jpeg'
            #image url
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            #printing your image has been download
            print 'Your image has been downloaded!'
        else:
            #printing the post
            print 'Post does not exist!'
    else:
        #printing the status of code
        print 'Status code other than 200 received!'


'''
Function declaration to get the recent post of a user by username
'''


def get_user_post(insta_username):
    #detailing of the user id
    user_id = get_user_id(insta_username)
    if user_id == None:
        #printng the user does not exist
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
#user media
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

#start bot
def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get the recent post of a user by username\n"
        # print "e.Get a list of people who have liked the recent post of a user\n"
        # print "f.Like the recent post of a user\n"
        # print "g.Get a list of comments on the recent post of a user\n"
        # print "h.Make a comment on the recent post of a user\n"
        # print "i.Delete negative comments from the recent post of a user\n"
        print "j.Exit"

        choice = raw_input("Enter you choice: ")
        if choice == "a":
            self_info()
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "c":
            get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        # elif choice=="e":
        #    insta_username = raw_input("Enter the username of the user: ")
        #    get_like_list(insta_username)
        # elif choice=="f":
        #    insta_username = raw_input("Enter the username of the user: ")
        #    like_a_post(insta_username)
        # elif choice=="g":
        #    insta_username = raw_input("Enter the username of the user: ")
        #    get_comment_list(insta_username)
        # elif choice=="h":
        #    insta_username = raw_input("Enter the username of the user: ")
        #    make_a_comment(insta_username)
        # elif choice=="i":
        #    insta_username = raw_input("Enter the username of the user: ")
        #    delete_negative_comment(insta_username)
        elif choice == "j":
            exit()
        else:
            print "wrong choice"

start_bot()