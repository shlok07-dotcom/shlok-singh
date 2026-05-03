lst = []
while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	
	choice = input("Enter choice: ")
	
	if choice == '1':
		try:
			val = int(input("Integer: "))
			lst.append(val)
			print(f"List after adding: {lst}")
		except ValueError:
			print("Invalid input")
			
	elif choice == '2':
		if not lst:
			print("List is empty")
		else:
			try:
				val = int(input("Integer: "))
				if val in lst:
					lst.remove(val)
					print(f"List after removing: {lst}")
				else:
					print("Element not found")
			except ValueError:
				print("Invalid input")

	elif choice == '3':
		if not lst:
			print("List is empty")
		else:
			print(lst)

	elif choice =='4':
		break

	else:
		print("Invalid choice")