"""
This module provides some predefined palettes.
"""

from ..gen import hue_gradient_palette
from ..conv import hex2rgb

__all__ = [ 
    'colorwheel',
    'tech',
    'service',
    'messaging',
    'social_media',
    'beverage',
    'retail',
    'automobile',
    'restaurant',
    'courier',
    'media',
    'whiskey',
    'beer',
    'misc', 
]

colorwheel = {
    'hxx_degrees': hue_gradient_palette([[0, 1, .5], [1, 1, .5]], 360),
}

## Brand palettes
# Sources
#   https://www.w3schools.com/colors/colors_brands.asp
#   https://usbrandcolors.com/
#   https://brandpalettes.com/
#   Original research
tech = {
'apple': hex2rgb(['#000000', '#555555']),
'google': hex2rgb(
    ['#4285F4', '#DB4437', '#F48400', '#0F9D58', 
     '#76A7FA', '#E57368', '#FBCB43', '#33B679', 
     '#A0C3FF', '#ED9D97', '#FFE168', '#7BCFA9', 
     '#F2F2F2', '#B3B3B3', '#666666', '#1A1A1A',
     '#E6E6E6', '#999999', '#4D4D4D', '#E7E6DD', 
     '#CCCCCC', '#808080', '#333333']),
'microsoft': hex2rgb(
    ['#F25022', '#7FBA00', '#00A4EF', '#FFB900', '#737373']),
'oracle': hex2rgb(['#F80000', '#000000']),
'intel': hex2rgb(['#0F7DC2']),
'ibm': hex2rgb(['#006699']),
'yahoo': hex2rgb(['#7B0099']),
'amazon': hex2rgb(['#FF9900', '#146EB4']),
'android': hex2rgb(['#A4C639']),
'samsung': hex2rgb(
    ['#14289F', '#000000', '#FFFFFF', '#1678C8', '#28B3E3', '#2DC3B2', 
     '#8091DE', '#95D552', '#FCB448', '#FA4437']),
'hp': hex2rgb(['#0096D6', '#000000']),
'xbox': hex2rgb(['#107C10', '#3A3A3A']),
'google_xx': hex2rgb(
    ['#4285F4', '#FBBC05', '#34A853', '#EA4335']),
'microsoft_xx': hex2rgb(
    ['#F65314', '#7CBB00', '#00A1F1', '#FFBB00']),
}

# Service brands
service = {
'airbnb': hex2rgb(['#FF5A5F', '#00A699', '#FC642D', '#484848', '#767676']),
'lyft': hex2rgb(['#FF00BF', '#11111F']),
'uber': hex2rgb(['#000000', '#FFFFFF']),
}

# Messaging brands
messaging = {
'slack': hex2rgb(['#36C5F0', '#2EB67D', '#E01E5A', '#ECB22E']),
'snapchat': hex2rgb(['#FFFC00', '#000000']),
'messenger': hex2rgb(['#00B2FF', '#006AFF']),
'whatsapp': hex2rgb(['#128C7E', '#075E54', '#25D366', '#34B7F1']),
}

# Social Media brands
social_media = {
'youtube':hex2rgb(['#FF0000', '#282828']),
'tiktok':hex2rgb(['#25F4EE', '#FE2C55', '#000000', '#FFFFFF']),
'instagram':hex2rgb(
    ['#405DE6', '#5B51D8', '#833AB4', '#C13584', '#E1306C', 
     '#FD1D1D', '#F56040', '#F77737', '#FCAF45', '#FFDC80']),
'facebook':hex2rgb(['#4267B2', '#898F9C', '#000000']),
'pinterest':hex2rgb(['#E60023', '#FFFFFF']),
'twitter':hex2rgb(
    ['#1DA1F2', '#14171A', '#657786', '#AAB8C2', '#E1E8ED', 
     '#F5F8FA', '#FFFFFF']),
'instagram_xx':hex2rgb(
    ['#3F729B', '#3B5998', '#8B9DC3','#DFE3EE', '#F7F7F7', '#FFFFFF']),
'twitter_xx':hex2rgb(
    ['#55ACEE', '#292F33','#66757F','#CCD6DD','#E1E8ED','#FFFFFF']),
}

# Beverage brands (non-alcoholic)
beverage = {
'coca-cola': hex2rgb(['#F40009', '#1E1E1E']),
'pepsi': hex2rgb(['#C9002B', '#004B93', '#005CB4']),
'red-bull': hex2rgb(['#DB0A40', '#FFCC00']),
'monster-energy': hex2rgb(['#95D600', '#000000']),
'kool-aid': hex2rgb(['#0056A2', '#00AEEF']),
'sprite': hex2rgb(['#008B47', '#F8CD24', '#6BB64A']),
'gatorade': hex2rgb(['#F8A350', '#EE3D42', '#231F20']),
'coke_xx': hex2rgb(['#ED1C16']),
'pepsi_xx': hex2rgb(['#E32934', '#004883']),
}

# Retail brands
retail = {
'ikea': hex2rgb(['#FFCC00','#003399']),
'levis': hex2rgb(['#C41230']),
}
# Car brands
automobile = {
'toyota': hex2rgb(['#EB0A1E', '#000000', '#FFFFFF', '#58595B']),
'mercedes': hex2rgb(['#000000', '#A4AAAE']),
}
# Restaurant brands
restaurant = {
'mcdonalds': hex2rgb(['#FFC72C', '#DA291C', '#27251F']),
'burger-king': hex2rgb(['#DA291C', '#0033A0', '#F2A900']),
'taco-bell': hex2rgb(['#702082', '#A77BCA', '#000000']),
'subway': hex2rgb(['#008C15', '#FFC600']),
'starbucks': hex2rgb(['#00704A', '#27251F']),
'dunkin-donuts': hex2rgb(['#FF671F', '#DA1884', '#653819']),
}

# Courier brands
courier = {
'fedex': hex2rgb(
    ['#4D148C', '#FF6600', '#999999', '#00CC00', '#0099CC', 
     '#FF0033', '#FFCC00', '#000000' ]),
'ups': hex2rgb(['#351C15', '#FFB500']),
'usps': hex2rgb(['#004B87', '#DA291C', '#000000']),
'dhl': hex2rgb(['#D40511', '#FFCC00']),
}

# Media brands
media = {
'netflix': hex2rgb(['#221F1F', '#E50914', '#F5F5F1']),
'spotify': hex2rgb(['#1DB954', '#191414']),
'disneyxd': hex2rgb(['#08EE59']),
'disneyxd-old': hex2rgb(['#243E65','#B5DB17']),
'disney-fireworks': hex2rgb(
    ['#1738B7', '#3340DB', '#504DF4', '#DE5BF8', '#EFE8FF', '#A76BFE']),
}

# Whiskey brands
whiskey = {
'johnny-walker': hex2rgb(['#000000', '#0C2340', '#866D4B']),
'jack-daniels': hex2rgb(['#000000', '#8C6E4B', '#38573D']),
'jim-beam': hex2rgb(['#000000', '#B4944A']),
}

# Beer brands
beer = {
'bud-light': hex2rgb(['#00A1E1', '#00A1E1']),
'budweiser': hex2rgb(['#C8102E']),
'busch': hex2rgb(['#373435', '#BB9D42', '#313A5F', '#22C4F3']),
'busch-light': hex2rgb(['#314973', '#00BCF1', '#C2C3C5']),
'coors': hex2rgb(['#000D48', '#FFFFFF', '#95969A']),
'coors-light': hex2rgb(['#D31245', '#D1D3D4', '#717073']),
'heineken': hex2rgb(['#007F2D', '#E30613', '#BDBCBC']),
'keystone-light': hex2rgb(['#00255B', '#47C3EB']),
'michelob-ultra': hex2rgb(['#0058A4', '#DC1D38', '#B21F3E']),
'miller-high-life': hex2rgb(['#86754D', '#AA483D']),
'miller-lite': hex2rgb(['#000F3D', '#A07713', '#AF282D']),
'natural-light': hex2rgb(
    ['#00AEEF', '#0067B1', '#004B8D', '#EE3124', 
     '#B30838', '#A7A9AC', '#7E8083']),
'pabst-blue-ribbon': hex2rgb(['#222D65', '#CE202E', '#D8D9DA']),
'samuel-adams': hex2rgb(['#002856', '#E2231A']),
}

# Miscellaneous brands
misc = {
'john-deere': hex2rgb(['#367C2B', '#FFDE00', '#000000']),
}
