from blog_post import BlogPost

if __name__ == '__main__':
    is_running_post = True
    while is_running_post:
        choice = input("""
                    \n Enter <c> to create new blogpost, <r> to read an existing blog, <u> to update post, <d> to delete a blog or <q> to quit: """)

        if choice == 'c':
            post = BlogPost()
            post.collect_post_info()
            print(post.save_post_to_file())

        elif choice == 'r':
            filename = input("Enter filename e.g, post.txt: ")
            post = BlogPost()
            print(post.read_post(filename))

        elif choice == 'u':
            post_title = input("Enter post title to update: ")
            post = BlogPost(title = post_title)
            print(post.update_post())

        elif choice == 'd':
            delete_post = input("Enter title of post to delete: ")
            post = BlogPost(title = delete_post)
            print(post.delete_post())

        elif choice == 'q':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid chioce. try again!")