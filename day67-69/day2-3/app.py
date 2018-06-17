from googletrans import Translator
import pyperclip
import sys
import webbrowser


def main():
    url = 'http://py-googletrans.readthedocs.io/en/latest/#googletrans-languages'
    old_text = paste_from_clipboard()
    print('[H]elp to see all language code')
    print('[S]elect a target language')
    print('[Q]uit')
    key = input('Insert your selection:\t')

    while key.lower() != 'q':
        if key.lower() == 'h':
            webbrowser.open(url)
        elif key.lower() == 's':
            langauge = input('Insert a target language:\t')
            try:
                new_text = translate(old_text, langauge)
                copy_to_clipboard(new_text)
                input()
            except:
                print('Error')
        key = input('Insert your selection:\t')
    sys.exit()




def paste_from_clipboard():
    text = pyperclip.paste()
    return text

def copy_to_clipboard(new_text):
    pyperclip.copy(new_text)
    print("The new text is now copied to the clipboard. Hit CTRL V to paste.")

def translate(old_text, langauge):
    translator = Translator()
    return (translator.translate(old_text, dest=langauge)).text


if __name__ == '__main__':
    main()
