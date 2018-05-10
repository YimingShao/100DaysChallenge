import re

def main():
    text1 = extract_course_times()
    print(text1)
    text2 = split_on_multiple_chars()
    print(text2)
    text3 = match_first_paragraph()
    print(text3)
    text4 = find_double_words()
    print(text4)
    text5 = match_ip_v4_address('255.255.255.255')
    print(text5)

def extract_course_times():
    '''Use re.findall to capture all mm:ss timestamps in a list'''
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    return re.findall(r'\d+:\d+',flask_course)


def split_on_multiple_chars():
    '''Use re.split to split log line by ; , .
       but not on the last ... so list should have len of 4
       (hint check re.split docs for extra switches)'''
    logline = ('2017-11-03T01:00:02;challenge time,regex!.'
               'hope you join ... soon')
    return re.split('''[;]|[,]|\.(?=\w+)''', logline)


def get_all_hashtags_and_links():
    '''Use re.findall to extract the URL and 2 hashtags of this tweet'''
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    key = re.findall(r'(?:http.*.html|#\w+)', tweet)
    return key


def match_first_paragraph():
    '''Use re.sub to extract the content of the first paragraph (excl tags)'''
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    pat = re.findall(r'<\w>.*', html.split("</p>")[0])
    return re.sub('<\w>','',pat[0])


def find_double_words():
    '''Use re.search(regex, text).group() to find the double word'''
    text = 'Spain is so nice in the the spring'
    return re.search(r'\b(\w+)\s+\1\b',text).group()



def match_ip_v4_address(ip):
    '''Use re.match to match an ip v4 address (no need for exact IP ranges)'''
    return re.match("^(\d{1,3}.){3}\d{1,3}$",ip)


if __name__ == '__main__':
    main()