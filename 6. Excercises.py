# Recursive Python3 program to find maximum number of cookies

import math

def countRec(cookies, wrap):
	
	if (cookies < wrap):
		return 0;

	newCookies = cookies / wrap;

	# Now we have "newCookies + cookies%wrap" wrappers.
	return newCookies + countRec(newCookies + cookies %
								wrap, wrap);


def countMaxCookies(money, price, wrap):
	
	# We can directly buy below
	# number of cookies
	cookies = money / price;

	return math.floor(cookies + countRec(cookies, wrap));

money = 15;
price = 1;
wrap = 3 ;
	
# exchanged for one cookies
print(countMaxCookies(money, price, wrap));


