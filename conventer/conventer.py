def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Sıcaklık değerini Celsius cinsinden girin: "))


fahrenheit = celsius_to_fahrenheit(celsius)


print(f"{celsius} Celsius, {fahrenheit} Fahrenheit'a eşittir.")
