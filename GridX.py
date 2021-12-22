row = 0

while row  <= 10:
      col = 0
      while col <= 10:
            if row == 0 or row == 5 or row == 10:
                if col == 0 or col == 5 or col == 10:
                  print('+', end='')
                else: print('-', end='')
            else: 
                if col == 0 or col == 5 or col == 10:
                    print('!', end='')
                else: print(' ', end='')
            col += 1
      print()
      row += 1
               
            