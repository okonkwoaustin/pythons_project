
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
        try:
            self.title = input("Enter Title: ")
            self.author = input("Enter Author: ")
            self.date_created = date.today()
            self.content = input("Enter Content: ")
            if not self.title or not self.author or not self.content:
                raise ValueError("fields are required")
        except Exception as e:
            return f"Error collecting input: {e}"

    def save_post_to_file(self, dir="posts"):
        """Save post to file with filename based on title"""
        try:    
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

            return f"\n Post saved as : {path}"
        except Exception as e:
            return f"Error saving post: {e}"

    def read_post(self, filename, dir="posts"):
        """Read and display a saved post"""
        try:
            path = os.path.join(dir, filename)
            if os.path.exists(path):
                print(f"\nReading {filename}: \n")
                with open(path, "r") as file:
                    content = file.read()
                    return content
            else:
                return "File not found."
        except Exception as e:
            return f"Error reading file post: {e}"

    def delete_post(self, dir="posts"):
        """Delete the file of the blog post"""
        try:
            if hasattr(self, 'filepath') and os.path.exists(self.filepath):
                os.remove(self.filepath)
                return f"\n Post '{self.title}' has been deleted."
            else:
                safe_title = self.title.replace(" ", "_").replace("/", "_")
                filepath = os.path.join(dir, f"{safe_title}.txt")
                if os.path.exists(filepath):
                    os.remove(filepath)
                    return f"\n Post '{self.title}' has been deleted"
                else:
                    return "File notfoumd"
        except Exception as e:
            return f"Error deleting post: {e}"
            
    def update_post(self, dir="posts"):
        """Update a saved blog post"""
        try:
            safe_title = self.title.replace(" ", "_").replace("/", "_")
            path = os.path.join(dir, f"{safe_title}.txt")
            
            if os.path.exists(path):
                print("\nUpdate your post:")
                
                # Prompt for new values
                self.collect_post_info()

                # Save new values
                self.save_post_to_file(dir)

                # Delete the old file if title changed
                new_safe_title = self.title.replace(" ", "_").replace("/", "_")
                if new_safe_title != safe_title:
                    os.remove(path)
                    print(f"🗑️ Old file '{safe_title}.txt' deleted")

                return f"Post '{self.title}' has been updated."
            
            return "Post not found to update."
        except Exception as e:
            return f"Error updating post: {e}"



