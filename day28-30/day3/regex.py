import re

def main():
    text1 = extract_course_times()
    print(text1)
    text2 = get_all_hashtags_and_links()
    print(text2)
    text3 = match_first_paragraph()
    print(text3)

def extract_course_times():
    """Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']"""
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    key = re.findall(r'\d+:\d+',flask_course)
    return key

def get_all_hashtags_and_links():
    """Write a regular expression that returns this list:
       ['http://pybit.es/requests-cache.html', '#python', '#APIs']"""
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')

    key = re.findall(r'(?:http.*.html|#\w+)', tweet)
    return key


def match_first_paragraph():
    """Write a regular expression that returns  'pybites != greedy' """
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    pat = re.findall(r'<\w>.*',html.split("</p>")[0])
    pat = re.sub('<\w>','',pat[0])
    return pat

if __name__ == '__main__':
    main()