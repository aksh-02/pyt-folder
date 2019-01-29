punctuation = "#()*+,-/:;<=>? \\@^_'{|}~[]"
input_string = input("enter a text string")
output_string = ' '
space_flag = False
for char in input_string:
 if char == '.':
  print(output_string)
 elif char not in punctuation:
  print(char)
 else:
  if not space_flag:
   print(output_string)
   space_flag = True

  
