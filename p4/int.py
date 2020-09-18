print('-'*12+'\nTurnip Shop\n'+'-'*12)
while True:
  try:
      n = int(input('\nHow many turnips would you like?'))
      break
  except ValueError:
    print('\nError, can only buy full turnips')
    
print('\nHere is/are your',str(n),'turnip(s)\n')
for i in range (n):
  print('turnip',str(i+1))