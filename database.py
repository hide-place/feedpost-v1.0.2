import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv('.env')
# Edit this with your path to serviceAccount.json after downloading from Firebase

Certificate = os.getenv('PATH_TO_SERVICE_ACCOUNT_JSON')


cred = credentials.Certificate(Certificate)
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv('DATA_BASE_URL')
})


def get_posts_data() -> dict :
    """
    This function retrieves all the post data from the database.

    Returns:
        dict: A dictionary containing all the post data.
    """
    ref = db.reference('/posts')
    posts : dict = ref.get()
    print('GPD -S ') #test
    return posts



def store_post_data(username : str , postText : str , time :str) -> None:
    """
    This function stores the username, postText, and time in a realtime database.

    Parameters:
        username (str): The username of the post author.
        postText (str): The text content of the post.
        time (str): The time when the post was created.

    Returns:
        None
    """
    post_data : dict = {
        "username" : username,
        "postText" : postText, 
        "time"  : time,
        "likes" : 0
    }
    ref = db.reference('/posts')
    posts : dict= ref.get()
    lastId = len(posts.keys())
    postID   = f"{post_data['username'] }-{lastId}"
    postID_base = ref.child(postID)
    postID_base.set(post_data)
    print('SPD - S') #test
    

if __name__ == '__main__':
    #test of the store_post_data
    now : str = str(datetime.now())[0:16]
    print(now)
   # store_post_data('alfred' , 'hello world' , now)
    get_posts_data()