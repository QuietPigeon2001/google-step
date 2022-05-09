res,curr,prev,pprev,counter = 0,0,0,0,0
while True:
    pprev = prev
    prev = curr
    print("Number: ")
    curr = input()
    if not curr:
        print("Answer: {}".format(res))
        break
    if pprev == curr or prev == curr:		# if repeated
        if counter == 0:		# condition for res update
        	res = curr
        	counter += 1
        elif curr != res:
       		counter -= 1
        else:
        	counter += 1		# res remains the same 
