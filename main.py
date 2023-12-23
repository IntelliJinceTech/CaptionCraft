from client import create_app

app = create_app()

# if we run this file...then run the following
if __name__ == '__main__':
    # debugging is true for development to automatically rerun on changes
    app.run(debug=True)