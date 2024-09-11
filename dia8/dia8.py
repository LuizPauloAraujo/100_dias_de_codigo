def celsius_fahrenheit():
   c = float(input('Digite a temperatura em °c'))
   f = float((9 * c) / 5) + 32

   return print('A temperatura em fahrenheit: {0}°F'.format(f))

celsius_fahrenheit()