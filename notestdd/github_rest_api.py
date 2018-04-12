'Goal:  How to use any generic REST API'

import requests

def show_user_info(user):
    "Display a Github user's contact information"
    # https://developer.github.com/v3/
    info = requests.get('https://api.github.com/users/' + user).json()
    print('{name} works at {company}. Contact at {email}'.format(**info))

if __name__ == '__main__':

    show_user_info('raymondh')
    show_user_info('hugs')
