zodiac_signs = ['aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','sagittarius','capricorn','aquarius','pisces']
fin_zodiac_signs = ['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces']
houses = ['Mars','Venus','Mercury','The Moon','The Sun','Mercury','Venus','Mars','Jupiter','Saturn','Saturn','Jupiter','Mars']
exaltations = {33:'The Moon',19:'The Sun',105:'Jupiter',165:'Mercury',201:'Saturn',200:'Saturn according to Pliny, Firmicus Maternus and Varāhamihira',298:'Mars',357:'Venus'}
dejections = {199:'The Sun',213:'The Moon',21:'Saturn',20:'Saturn according to Pliny, Firmicus Maternus and Varāhamihira',108:'Mars',285:'Jupiter',147:'Venus',345:'Mercury'}
house_exaltations = {'aries':'The Sun','taurus':'The Moon','libra':'Saturn','cancer':'Jupiter','capricorn':'Mars','pisces':'Venus','virgo':'Mercury'}
house_dejections = {'libra':'The Sun','scorpio':'The Moon','aries':'Saturn','capricorn':'Jupiter','cancer':'Mars','virgo':'Venus','pisces':'Mercury'}


rep = True
while rep:
	#START POINT
	print('\nStart Point\n')

	init_sign = 'a'
	while init_sign.lower() not in zodiac_signs:
		init_sign = input('Sign: ')
	init_sign = init_sign.lower()
	init_house = houses[zodiac_signs.index(init_sign)]
	print('(House of '+init_house+')')

	#house exaltations/dejections
	try:
		house_ex_dej = house_exaltations[init_sign]
		house_ex_dej = ' exaltation of '+house_ex_dej
		print('(House of the'+house_ex_dej+')')
	except:
		pass
	try:
		house_ex_dej = house_dejections[init_sign]
		house_ex_dej = ' dejection of '+house_ex_dej
		print('(House of the'+house_ex_dej+')')
	except:
		pass

	init_degrees = '1'
	while True:
		init_degrees_str = input('Degree: ')
		if init_degrees_str.isdigit():
			init_degrees = int(init_degrees_str)
			if 0 < init_degrees < 31:
				process = 1 #casts by degrees
				init_total_degrees = (((zodiac_signs.index(init_sign))*30)+init_degrees) #number of 30s + input degrees
				#exaltation or dejection
				try:
					init_ex_dej = exaltations[init_total_degrees]
					print('(Exaltation of '+init_ex_dej+')')
				except:
					try:
						init_ex_dej = dejections[init_total_degrees]
						print('(Dejection of '+init_ex_dej+')')
					except:
						init_ex_dej = ''
				break

		elif init_degrees_str == '':
			process = 2 #casts by sign
			break
	#Cast

	print('\nCast\n')

	while True:
		cast_str = input('Number: ')
		if cast_str.isdigit():
			cast = int(cast_str)
			break


	cast_direction = 'a'
	while cast_direction.upper() != 'F' and cast_direction.upper() != 'B':
		cast_direction = input('Forwards or backwards (f/b)? ')

	if cast_direction.upper() == 'B':
		cast = 0 - (cast-2)



	#ACTUAL PROCESS

	if process == 1: #cast by degree
		init_total_degrees = (((zodiac_signs.index(init_sign))*30)+init_degrees) #number of 30s + input degrees
		fin_total_degrees = (init_total_degrees + (cast-1)) #when casting you add by 1 less
		fin_sign = fin_zodiac_signs[(((((fin_total_degrees-1) % 360)+1)-1) // 30)]
		fin_house = houses[((((fin_total_degrees-1) % 360)+1) // 30)]
		fin_degrees = ((fin_total_degrees-1) % 30)+1
		#exaltation or dejection
		try:
			ex_dej = exaltations[fin_total_degrees%360]
			ex_dej = '(Exaltation of '+ex_dej+')'
		except:
			try:
				ex_dej = dejections[fin_total_degrees%360]
				ex_dej = '(Dejection of '+ex_dej+')'
			except:
				ex_dej = ''

		#house exaltations or dejections
		try:
			fin_house_ex = house_exaltations[fin_sign.lower()]
			fin_house_ex = '(House of the exaltation of '+fin_house_ex+') '
		except:
			fin_house_ex = ''
		try:
			fin_house_dej = house_dejections[fin_sign.lower()]
			fin_house_dej = '(House of the dejection of '+fin_house_dej+') '
		except:
			fin_house_dej = ''

		print('\nEnd Point\n')


		print('Sign: '+fin_sign+' (House of '+fin_house+')')
		print(fin_house_ex+fin_house_dej)
		print('Degrees: '+str(fin_degrees)+'° '+ex_dej)
		print('\n')


	else: #cast by sign
		init_total_degrees = (((zodiac_signs.index(init_sign))*30)) #number of 30s + input degrees
		fin_total_degrees = (init_total_degrees + ((cast-1)*30)) #when casting you add by 1 less
		fin_sign = fin_zodiac_signs[((((((fin_total_degrees-1) % 360)+1))) // 30)]
		fin_house = houses[((((((fin_total_degrees-1) % 360)+1))) // 30)]
		#exaltation or dejection

		#house exaltations or dejections
		try:
			fin_house_ex = house_exaltations[fin_sign.lower()]
			fin_house_ex = '(House of the exaltation of '+fin_house_ex+') '
		except:
			fin_house_ex = ''
		try:
			fin_house_dej = house_dejections[fin_sign.lower()]
			fin_house_dej = '(House of the dejection of '+fin_house_dej+') '
		except:
			fin_house_dej = ''

		print('\nEnd Point\n')


		print('Sign: '+fin_sign+' (House of '+fin_house+')')
		print(fin_house_ex+fin_house_dej)
		print('\n')

	rep_str = 'a'
	while rep_str.lower() != 'y' and rep_str.lower() != 'n':
		rep_str = input('Repeat program (y/n)? ')
	if rep_str == 'n':
		rep = False
	else:
		print('\n\n')

