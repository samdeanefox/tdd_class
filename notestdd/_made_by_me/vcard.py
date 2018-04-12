"""Make Digital Business Cards

A true, old, and sordid tale of Python
featuring raisins, pushy relatives, checkerboards,
business cards, web pages, and getting much needed rest.

"""

import urllib.request
import urllib.parse

vcard_template = """BEGIN:VCARD
VERSION:2.1
N:{last};{first}
FN:{first}, {last}
ORG:Earthborn Studios Inc
TITLE: {title}
TEL;WORK;VOICE:(205) {phone}
TEL;HOME;VOICE:(205) 613-0280
TEL;
ADR;WORK;PREF:;;7575 Parkway Dr;Leeds;AL;35094;United States of America
EMAIL:{email}
REV:20080424T195243Z
END:VCARD"""

def make_vcard(first, last, title, email, phone):
    return vcard_template.format(first=first, last=last, title=title, email=email, phone=phone)

def make_qr_code(text):
    root_url = 'http://chart.googleapis.com/chart'
    query = {'cht': 'qr', 'chs': '400x400', 'chl': text}
    url = root_url + '?' + urllib.parse.urlencode(query)
    con = urllib.request.urlopen(url)
    image = con.read()
    con.close()
    return image

if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.INFO)

    with open('../raisin_team.csv') as reader:
        for line in reader:
            cleaned_line = line.strip()
            fields = cleaned_line.split(',')
            last, first, title, email, phone = fields

            vcard = make_vcard(first, last, title, email, phone)
            filename = '{first}-{last}.vcf'.format(first=first, last=last)
            with open(filename, 'w') as text_writer:
                text_writer.write(vcard)
            logging.info('Wrote: %s', filename)

            image = make_qr_code(vcard)
            filename = '{first}-{last}.png'.format(first=first, last=last)
            with open(filename, 'wb') as binary_writer:
                binary_writer.write(image)
            logging.info('Wrote: %s', filename)