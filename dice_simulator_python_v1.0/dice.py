#dice simulator using python
#developer : sibisaravanan

import random 
import os

print('''
        _____   _                _____  _                    _         _                          __        ___  
       |  __ \ (_)              / ____|(_)                  | |       | |                        /_ |      / _ \ 
       | |  | | _   ___  ___   | (___   _  _ __ ___   _   _ | |  __ _ | |_  ___   _ __   __   __  | |     | | | |
       | |  | || | / __|/ _ \   \___ \ | || '_ ` _ \ | | | || | / _` || __|/ _ \ | '__|  \ \ / /  | |     | | | |
       | |__| || || (__|  __/   ____) || || | | | | || |_| || || (_| || |_| (_) || |      \ V /   | |  _  | |_| |
       |_____/ |_| \___|\___|  |_____/ |_||_| |_| |_| \__,_||_| \__,_| \__|\___/ |_|       \_/    |_| (_)  \___/ 
    	                                                                                  Developed by sibisaravanan.																				                                                                                                                                          
    	
    																					
		'''	)

def roll(a,b,c,d,e,f,g,h,i):
	print('''
					-------
					|{} {} {}|
					|{} {} {}|
					|{} {} {}|
					-------
				'''.format(a,b,c,d,e,f,g,h,i))

run = True
while (run):
	print('''
		Welcome:
		1.Roll dice
		2.Quit Game
		''')
	user_input = int(input(">>>"))
	ran_num = random.randint(1,6)
	if user_input == 1:
		if ran_num==1:
			roll(' ',' ',' ',' ',0,' ',' ',' ',' ')
		elif ran_num==2:
			roll(' ',' ',' ',0,' ',0,' ',' ',' ')
		elif ran_num==3:
			roll(' ',' ',' ',0,0,0,' ',' ',' ')
		elif ran_num==4:
			roll(0,' ',0,' ',' ',' ',0,' ',0)
		elif ran_num==5:
			roll(0,' ',0,' ',0,' ',0,' ',0)
		elif ran_num==6:
			roll(0,' ',0,0,' ',0,0,' ',0)			
	else:
		print('''
				Thanks for Playing Dice simulator v1.0!
				''')
		exit()                    
