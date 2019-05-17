###Creating QRcode with the help of Python###
#install the library
pip install pyqrcode
#import the library pyqrcode
import pyqrcode   
#replace the url of your website
a = "https://www.google.com/" 
#Creating qrcode for your website                                                                        
url = pyqrcode.create (a)         
#saving the qrcode in respective folder                                                                    
url.svg("mysite.svg", scale = 10)                                                                     


