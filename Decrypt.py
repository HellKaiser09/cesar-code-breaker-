print( "Hello, Contosoville!" )

#Definimos la funcion que ns hayara a desencriptar el codigo en un cifrado cesar el cual pide una letra y cuanto avanzara 
def lasso_letter (letter, amount): 
# Creamos una variable llamada letter code para que se almacene el valor en ascii de la letra que se introdujo además de que con el comando .lower hacemos que se haga minuscula 
    letter_code = ord(letter.lower())
# Despues de convertirse en un numero ascii se le suma la cantidad que se especifico que avanzara
    decodded_letter_code = letter_code + amount
# Obtiene el código ASCII de la letra 'a' para usar como referencia en el cálculo
    a_ascii = ord("a")
# Define el tamaño del alfabeto inglés, que es de 26 letras
    alphabet_size = 26
# Calcula el código ASCII de la letra decodificada ajustada por el desplazamiento
    true_letter_code = a_ascii + (((letter_code - a_ascii) + amount) % alphabet_size)
#Devuelve el codigo ascii en una letra
    decoded_letter= chr(true_letter_code)
# Devuelve la letra decodificada
    return decoded_letter



# Función que decodifica una palabra completa aplicando un desplazamiento a cada letra
def lasso_word(word, shift_amount):
    # Inicializa una cadena vacía para almacenar la palabra decodificada
    decoded_word = ""
    
    # Recorre cada letra en la palabra dada
    for letter in word:
        # Decodifica la letra actual utilizando la función lasso_letter y el valor de desplazamiento
        decoded_letter = lasso_letter(letter, shift_amount)
        
        # Agrega la letra decodificada a la palabra decodificada acumulada
        decoded_word = decoded_word + decoded_letter
    
    # Devuelve la palabra completa decodificada
    return decoded_word

# Llama a la función lasso_word para decodificar la palabra 
print(f"Esta es la palabra descodificada\n" + lasso_word("Ncevy", 13))
print(f"Esta es la palabra descodificada\n" + lasso_word("gpvsui", 25))
print(f"Esta es la palabra descodificada\n" + lasso_word("p", -2))
print(f"Esta es la palabra descodificada\n" + lasso_word("wjmmf", -1))
