
def list_all_videos():
    pass
def add_video(videos):
    pass
def update_video(videos):
    pass
def delete_video(videos):
    pass

video=[]

while True:
    print("\n Yutube Manager | Choose an option ")
    print("1. List all youtube videos ")
    print("2. Add a Youtube video ")
    print("3. Update a Youtube video details ")
    print("4. Delete a youtube video ")
    print("5. Exit the app ")
    choice = input("Enter the choice")


    match choice:
        case '1':
            list_all_videos(videos)
        case '2': 
            add_video(videos)
        case '3':
            update_video(videos)
        case '4':
            delete_video(videos)


