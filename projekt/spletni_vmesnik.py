import bottle
#import model

#glavni_model = model.Model()

@bottle.route('/')
def index():
    return "To je glavna stran za moj projekt"


bottle.run(debug=True, reloader=True)