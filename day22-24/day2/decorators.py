from functools import wraps

def main():
    @make_html('p')
    @make_html('strong')
    def get_text(text):
        return text
    text = get_text('I Code with PyBites')
    print(text)


def make_html(element):
    def first_layer(func):
        @wraps(func)
        def second_layer(*args, **kwargs):
            return ('<'+str(element)+'>'+str(func(*args, **kwargs))+'</'+str(element)+'>')
            #return '<{}>{}</{}>'.format(element, func(*args, **kwargs), element)
        return second_layer
    return first_layer






if __name__ == '__main__':
    main()