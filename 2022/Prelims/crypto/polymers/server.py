#!/usr/bin/env python2
#-*- coding: utf-8 -*-

from companySecrets import secretStrand, nextMission

def polymer(ID, password):
	'''POLYMER©®™℠ Login system by PWNAGAUKAR LLC
	This uses state of the art technology to determine if a password is valid without storing the passwords
	This makes the POLYMER©®™℠ Login system immune to hackers and leaks'''
	secretDigest = sum([secretStrand[x] * ID ** x for x in range(len(secretStrand))])
	passwordStrand = map(ord, password)
	passwordDigest = sum([passwordStrand[x] * ID ** x for x in range(len(passwordStrand))])
	return secretDigest - passwordDigest

logo = '''
 ▄▄▄·      ▄▄▌   ▄· ▄▌• ▌ ▄ ·. ▄▄▄ .▄▄▄  
▐█ ▄█ ▄█▀▄ ██•  ▐█▪██▌·██ ▐███▪▀▄.▀·▀▄ █·
 ██▀·▐█▌.▐▌██ ▪ ▐█▌▐█▪▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ 
▐█▪·•▐█▌.▐▌▐█▌ ▄ ▐█▀·.██ ██▌▐█▌▐█▄▄▌▐█•█▌
.▀    ▀█▄▀▪.▀▀▀   ▀ • ▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀
'''

print logo
print 'Henlo and welcome to the POLYMER©®™℠ login mechanism'
print 'To login please enter your id and FLAG©®™℠ password'

try:
	ID = int(raw_input('ID: '))
	password = raw_input('pass: ').strip()
except:
	print 'Why error?'
	quit()

if not password or not ID:
	print 'you must enter BOTH the ID and the password'
	quit()

result = polymer(ID, password)
if result == 0:
	print 'Good evening, {}. '.format(ID) + nextMission
else:
	print 'Error: POLYMER©®™℠ returned {}. You are not agent #{}.'.format(result, ID)
