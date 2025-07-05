
import os
from datetime import date


class BlogPost:
    """Model a blog post"""

    def __init__(self, title="", author="", date_created=None, content=""):
        self.title = title
        self.author = author
        self.date_created = date_created
        self.content = content

    def collect_post_info(self):
        """Collect user input"""
        self.title = input("Enter Title: ")
        self.author = input("Enter Author: ")
        self.date_created = date.today()
        self.content = input("Enter Content: ")

    def save_post_to_file(self, dir="posts"):
        """Save post to file with filename based on title"""
        if not os.path.exists(dir):
            os.makedirs(dir)

        safe_title = self.title.replace(" ", "_").replace("/", "_")
        filename = f"{safe_title}.txt"
        path = os.path.join(dir, filename)

        with open(path, "w") as file:
            file.write(f"Title: {self.title}\n")
            file.write(f"Author: {self.author}\n")
            file.write(f"Date Created: {self.date_created}\n")
            file.write(f"Content: {self.content}\n")
            file.write("----------------------------\n")

        print(f"\n Post saved as : {path}")

    def read_post(self, filename, dir="posts"):
        """Read and display a saved post"""
        path = os.path.join(dir, filename)
        if os.path.exists(path):
            print(f"\nReading {filename}: \n")
            with open(path, "r") as file:
                print(file.read())
        else:
            print("File not found.")

    def delete_post(self, dir="posts"):
        """Delete the file of the blog post"""
        if hasattr(self, 'filepath') and os.path.exists(self.filepath):
            os.remove(self.filepath)
            print(F"\n Post '{self.title}' has been deleted.")
        else:
            safe_title = self.title.replace(" ", "_").replace("/", "_")
            filepath = os.path.join(dir, f"{safe_title}.txt")
            if os.path.exists(filepath):
                os.remove(filepath)
                print(f"\n Post '{self.title}' has been deleted")
            else:
                print("File notfoumd")


# Step 1: Create and save a post
post = BlogPost()
post.collect_post_info()
post.save_post_to_file()

# Step 2: Read post from it's own file
filename = input(
    "Enter the filename of the post to read (e.g., My_Title.txt): ")
post.read_post(filename)

# Step 3: If you want to delete it later:
delete_choice = input("\nDo you want to delete this post? (yes/no): ").lower()
if delete_choice == 'yes':
    post.delete_post()
