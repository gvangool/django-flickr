#!/usr/bin/env python
# encoding: utf-8

"""
This file gathers all the stuff used in the application but depending
on the flickr service. Having it all together in one place will help
maintenance just in case flickr opts to change anything.

References:
 * http://www.flickr.com/help/photos/
 * http://www.flickr.com/services/api/misc.urls.html
"""

FLICKR_PHOTO_SOURCE = 'http://farm%(farm-id)s.staticflickr.com/%(server-id)s/%(photo-id)s_%(secret)s%(size_suffix)s.%(format)s'
FLICKR_PHOTO_URL_PAGE = 'http://www.flickr.com/photos/%(user-id)s/%(photo-id)s/'
FLICKR_PHOTO_URL_PAGE_SIZES = 'http://www.flickr.com/photos/%(user-id)s/%(photo-id)s/sizes/%(size-suffix)s/'
FLICKR_PHOTO_SHORT_URL = 'http://flic.kr/p/%(short-photo-id)s'
FLICKR_PHOTOSTREAM = 'http://www.flickr.com/photos/%(user-id)s/'
FLICKR_PROFILE = 'http://www.flickr.com/people/%(user-id)s/'
FLICKR_BUDDY_ICON = 'http://farm%(icon-farm)s.staticflickr.com/%(icon-server)s/buddyicons/%(nsid)s.jpg'
FLICKR_BUDDY_ICON_DEFAULT = 'http://www.flickr.com/images/buddyicon.gif'

"""
All photo sizes, here for reference.
"""

FLICKR_PHOTO_SIZES = {
    'Square' : {'label' : 'square',
                'width' : 75,
                'height' : 75,
                'suffix' : 's',
                },
    'Large Square' : {  'label' : 'largesquare',
                        'width' : 150,
                        'height' : 150,
                        'suffix' : 'q',
                        },
    'Thumbnail' : { 'label' : 'thumb',
                    'longest' : 100,
                    'suffix' : 't',
                },
    'Small' : { 'label' : 'small',
                'longest' : 240,
                'suffix' : 'm',
                },
    'Small 320' : { 'label' : 'small320',
                    'longest' : 320,
                    'suffix' : 'n',
                },
    'Medium' : {'label' : 'medium500',
                'longest' : 500,
                },
    'Medium 640' : {'label' : 'medium',
                    'longest' : 640,
                    'suffix' : 'z',
                },
    'Medium 800' : {'label' : 'medium800',
                    'longest' : 800,
                    'suffix' : 'c',
                },
    'Large' : { 'label' : 'large',
                'longest' : 1024,
                'suffix' : 'b',
                },
    'Large 1600' : {'label' : 'large1600',
                    'longest' : 1600,
                    'suffix' : 'h',
                    'secret_field' : '',
                },
    'Large 2048' : {'label' : 'large2048',
                    'longest' : 2048,
                    'suffix' : 'k',
                    'secret_field' : '',
                },
    'Original' : {  'label' : 'ori',
                    'suffix' : 'o',
                    'secret_field' : 'originalsecret',
                },
    }

def get_size_from_label(label):
    for key, size_item in FLICKR_PHOTO_SIZES.items():
        if label == size_item.get('label', None):
            return size_item

def build_photo_source(farm_id, server_id, photo_id, secret, size, format='jpg'):
    size_suffix = ''
    if size.get('suffix', False):
        size_suffix = '_%s' % size['suffix']
    return FLICKR_PHOTO_SOURCE % {
                                'farm-id':farm_id,
                                'server-id':server_id,
                                'photo-id':photo_id,
                                'secret':secret,
                                'size_suffix':size_suffix,
                                'format':format,
                                }


"""
base58
http://www.flickr.com/groups/api/discuss/72157616713786392/
"""

class b58generator(object):
    alphabet = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
    base = len(alphabet)

    @classmethod
    def b58encode(div, s=''):
        if div >= base:
            div, mod = divmod(div, base)
            return b58encode(div, alphabet[mod] + s)
        return alphabet[div] + s

    @classmethod
    def b58decode(s):
        return sum(alphabet.index(c) * pow(base, i) for i, c in enumerate(reversed(s)))

