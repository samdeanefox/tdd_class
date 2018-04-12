''' A true, old, and sordid tale of Python
    featuring raisins, pushy relatives, checkerboards,
    business cards, web pages, and getting much needed rest.
'''

import requests

vcard_template = '''\
BEGIN:VCARD
VERSION:2.1
N:{lname};{fname}
FN:{fname} {lname}
ORG:Raisins R Us, Inc.
TITLE:{title}
TEL;WORK;VOICE:{phone}
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:{email}
REV:20170424T195243Z
END:VCARD
'''

def make_vcard(fname, lname, title, email, phone):
    'Create an electronic business card in a Vcard 2.1 format'
    return vcard_template.format(lname=lname, fname=fname,
                                 title=title, email=email, phone=phone)

def make_qr_code(text):
    'Create a compute readable QR code in a PNG format using the Google Chart REST API'
    # https://developers.google.com/chart/infographics/docs/qr_codes
    query = dict(cht='qr', chs='300x300', chl=text)
    r = requests.get('https://chart.googleapis.com/chart', params=query)
    image = r.content
    # https://www.w3.org/TR/PNG/#5PNG-file-signature
    assert list(image[:8]) == [137, 80, 78, 71, 13, 10, 26, 10]
    return image

if __name__ == '__main__':

    import csv
    import logging

    logging.basicConfig(
        filename = 'raisins.log',
        level = logging.INFO,
        format = '%(levelname)-8s | %(asctime)s | %(message)s',
    )

    with open('notestdd/raisin_team_update.csv') as f:
        for lname, fname, title, email, phone in csv.reader(f):
            normalized_email = email.replace('.', '_dot_').replace('@', '_at_')

            vcard = make_vcard(fname, lname, title, email, phone) 
            filename = f'{normalized_email}.vcf'
            with open(filename, 'w') as vcard_file:
                vcard_file.write(vcard)
            logging.info(f'Wrote: {filename}')

            image = make_qr_code(vcard)
            filename = f'{normalized_email}.png'
            with open(filename, 'wb') as image_file:
                image_file.write(image)
            logging.info(f'Wrote: {filename}')
