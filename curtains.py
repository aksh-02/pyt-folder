roll_width = 140
cost_per_metre = 5
window_length = input("please enter your window's height : ")
window_width = input("please enter your window's width : ")
length = float(window_length) + 15
width = float(window_width)*0.75 + 20
if length < roll_width :
 length_required = width*2
elif width>roll_width and width%roll_width<0.5:
 length_required = length*3
elif width>roll_width and width%roll_width>0.5:
 length_required = length*4
cost = (length_required/100)*5
print("you will require", round(length_required,2)," cm of cloth with a total cost of ",round(cost,2) ,"rupees")
