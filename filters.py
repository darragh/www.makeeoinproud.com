from google.appengine.ext import webapp

register = webapp.template.create_template_register()

def minus( value, arg ):
    value = int( value )
    arg = int( arg )
    if arg: return value - arg

def progress( page ):
    page = int(page)
    if page < 10:
        return "progress-1"
    elif page < 20:
        return "progress-2"
    elif page < 30:
        return "progress-3"
    elif page < 40:
        return "progress-4"
    elif page < 50:
        return "progress-5"
    return "XXXX" + page

register.filter(minus)
register.filter(progress)