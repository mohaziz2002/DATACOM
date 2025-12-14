
def index_cell_check(cell_indx,array):
	if cell_indx < 1 or cell_indx > len(array):
		return True
	return False

def check_empty_cell(arr,cell,n):
	return True if arr[n-1] != cell else False

def invalid_cell_index(cell_indx,player):
	cell_indx = int(input(f'Invalid cell number! Player {player} Enter case number: '))
	return cell_indx

def Tic_tac_toe():
	array, nums = [], []
	start, size, cell = True, 3, ' -- ◦ --| '

	for i in range(1,(size**2)+1):
		array.append(cell)

	for x in range(len(array)//size):
		for n in range(size):
			print(cell,end='')
		print()

	counter, switcher = 1, 1
	player1, player2 = 'X', 'O'

	while start:
		choice = int(input(f'Player {switcher} Enter case number: '))

		while index_cell_check(choice,array):
			choice = invalid_cell_index(choice,switcher)

		while check_empty_cell(array,cell,choice):
			choice = int(input(f'Invalid case! Player {switcher} Enter case number: '))

			while index_cell_check(choice,array):
				choice = invalid_cell_index(choice,switcher)

		if counter % 2 != 0:
			item_player = player1; switcher = 2
		else:
			item_player = player2; switcher = 1

		array[choice-1] = (f'-- {item_player} --|')
		counter += 1

		for j in range(1,len(array)+1):
			delim = ''
			if j % size == 0:delim = '\n'
			print(array[j-1],end=f'{delim}')

		length,divider = len(array),int(len(array)/2)
		indx = [x for x in range(size,len(array)+1,3)]

		for c in range(size):
			if (array[c] != cell and (array[c] == array[c+size] and array[c] == array[c+(size*2)])):
				start = False

			if (array[length-indx[c]] != cell and (array[length-indx[c]] == array[(length-indx[c])+1] 
				and array[length-indx[c]] == array[(length-indx[c])+2])):
				start = False

			pointer = (length % divider)
			if ((array[pointer-1] != cell and (array[pointer-1] == array[divider]
				and array[pointer-1] == array[divider*2])) or
			(array[pointer+1] != cell and (array[pointer+1] == array[divider]
				and array[pointer+1] == array[divider+2]))):
				start = False

	print(f'Congratulations PLayer {size-switcher} ! You win the game')

Tic_tac_toe()
