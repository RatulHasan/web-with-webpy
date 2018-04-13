import web

urls = (
    '/(.*)'#this is url#
     , 'index' #this is corospondent class#

)

render = web.template.render('templates/')

app = web.application(urls, globals())

class index:
    def GET(self, name):
        # Render templates
        if not name:
            name = 'Ratul'
            return render.main(name)
        else:
            return render.starter_template(name)

        # Render templates

if __name__ == "__main__":
    app.run()