def temp_converter(temp, metric):
  # TODO: Converta a temperatura fornecida de celsius para fahrenheit e vice e versa
  # TODO: Se métrica informada for igual celsius função deverá retornar valor temp em fahrenheit
  # TODO: Se métrica informada for igual fahrenheit função deverá retornar valor temp celsius
  # Auxílio: https://www.google.com/search?q=celsius%2C+fahrenheit+are&oq=ce&aqs=chrome.0.69i59j69i57j35i39j46i199i291i512j0i20i263i512j0i512j69i61l2.976j0j9&sourceid=chrome&ie=UTF-8
  # Exemplo: temp = 35, metric = celsius, return = 95 (fahrenheit)
  # Exemplo: temp = 104, metric = fahrenheit, return = 40 (celsius)
  pass
  
  if metric == 'celsius':
    temp = temp * 1.8 + 32
    return temp #temperatura fahrenheit

  else: 
    temp = (temp - 32) / 1.8
    return temp  #temperatura em celsius

















