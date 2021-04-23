MENU_PROMPT = 'Enter "c" to create blog, "l" to list blogs, "r" to read one, "p" to create a post and "q" to quit.'
POST_TEMPLATE =''' 
 --- {} ---

{}

'''

blogs = dict() # blog_name: Blog object 
def menu(): 
    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'l':
            ask_create_blog()
        elif selection == 'c':
            ask_create_blog()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_post_blog()
        selections = input(MENU_PROMPT)

        def ask_create_blog():
            title = input('Enter your blog title: ')
            author = input('Enter your name: ')

            blogs[title] = Blog(title, author)
        
        def ask_read_blog():
            title = input('Enter the blog title you want to read: ')

            print_posts(blogs(title))

        def print_post(blog):
            for post in blog.post:
                print_post(post)

        def print_post(post):
            print(POST_TEMPLATE.format(post.title, post.content))

        def ask_create_post():
            pass

def print_blogs():
    # print the available blogs
    for key, blog in blogs.items(): # [(Blog_name, Blog), (Blog_name, Blog)]
        print('-{}'.format(blog)) #will print the blog in a list form with bullet points
        
        