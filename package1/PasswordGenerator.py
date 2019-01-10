import string
from random import*
characters=string.ascii_letters+string.punctuation+string.digits
password="".join(choice(characters)for x in range(randint(8,16)))
print "Noone is going to guess this password : "+ password

