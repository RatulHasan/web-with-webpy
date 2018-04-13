import web
from pymongo import MongoClient

myClient = MongoClient()

db = myClient.mydb

posts = db.posts

all_posts = posts.find()

urls = (
    '/(.*)'#this is url#
     , 'index' #this is corospondent class#

)

render = web.template.render('templates/')

app = web.application(urls, globals())

class index:
    def GET(self, posts):
        # Render templates
        if not posts:
            posts = 'Ratul'
            return render.main(posts)
        else:
            return render.starter_template(all_posts)

        # Render templates

if __name__ == "__main__":
    app.run()