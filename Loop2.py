#!/usr/bin/python3
#letter = ['abc','xyz','pqr']
#for letter in letter:
#    print(letter)

#for letter in 'python':
#    print(letter)


from	selenium	import	webdriver
browser	=	webdriver.Firefox()
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
userElem	=	browser.find_element_by_id('txtUserName')
userElem.send_keys('sachinsaurabh2008@gmail.com') #admn no here
passwordElem	=	browser.find_element_by_id('txtPassword')
passwordElem.send_keys('Sachin_2010') # password here
loginElem	=	browser.find_element_by_id('btnLogin')
loginElem.click()