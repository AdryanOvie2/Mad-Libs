# historias locas juego
# Tenemos un parrafo con espacios en blanco para completar por el usuario
# y luego mostrarle al usuario su historia loca, el texto completado con sus palabras.

# aspectos a tener en cuenta
# concatenar caracteres

adj = input("Ingresa un Adjetivo: ")
verb1 = input("Ingresa un Verbo: ")
verb2 = input("Ingresa otro Verbo: ")
sustantivo = input("Ingresa un Sustantivo plural: ")


madlib = f"Programar es tan {adj}! Siempre me emociona porque me encanta {verb1} problemas. Aprende a {verb2} en 42Madrid y alcanza tus {sustantivo}!"

print(madlib)