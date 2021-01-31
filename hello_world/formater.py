
PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"
HIDD = "hidden_html"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON, HIDD]


def get_formatted(msg, imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif format == JSON:
        result = format_to_json(msg, imie)
    elif result == HIDD:
        result = hidden_html(mgs, imie)
    return result


def format_to_json(msg, imie):
    return ('{ "imie":"' + imie + '", "msg":"' +
            msg + '"}')

def plain_text(msg, imie):
    return imie + ' ' + msg
    
def plain_text_upper_case(msg, imie):
    return plain_text(msg.upper(), imie.upper())

def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())
    
def hidden_html(msg, imie):
    return imie + ' ' + msg
    
    #return '<!doctype html><html><body><p>Hello World!</p>' + imie + ' pozdrawia ;)</body></html>'  
