import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Edit this with your path to serviceAccount.json after downloading from Firebase
Certificate = r'C:\Users\hp\Desktop\feedpost using flask\serviceAccount.json'
 
cred = credentials.Certificate(Certificate)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'YOUR_databaseURL '
})


def get_posts_data() -> dict :
    """
    This function retrieves all the post data from the database.

    Returns:
        dict: A dictionary containing all the post data.
    """
    ref = db.reference('/posts')
    posts : dict = ref.get()
    
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
    

if __name__ == '__main__':
    #test of the store_post_data
    store_post_data('john' , 'hello world' , '29/06/2024 02:51')