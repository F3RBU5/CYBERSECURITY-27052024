########################Square function - side multiplied by four##############

def square_perimeter():
    square_side = input ("Inserisci il valore del lato del Quadrato:")
    s_s = float (square_side)
    square_perimeter = s_s * 4
    print ("Il perimetro del Quadrato è di:", square_perimeter)

###############################################################################

#############Rectangle function - (base * 2) + (height * 2)####################

def rectangle_perimeter():
    rectangle_base = input("Inserisci il valore della base del Rettangolo:")
    rectangle_height = input("Inserisci il valore dell'altezza del Rettangolo:")
    b = float(rectangle_base)
    h = float(rectangle_height)
    rectangle_perimeter = (b * 2) + (h * 2)
    print ("Il perimetro del Rettangolo è di:", rectangle_perimeter)

    ##########Circumference function - radius * 2 * 3.14###########################

def circumference():
    radius = input("Inserisci il valore del raggio del Cerchio")
    r = float (radius)
    circumference = r * 2 * 3.14
    print ("La circonferenza del Cerchio è di:", circumference)

###############################################################################
###############################################################################
###############################################################################

################################Selection Menù##################################
print("A - Perimetro del Quadrato")
print("B - Perimetro del Rettangolo")
print("C - Circonferenza del Cerchio")
selection = input("Seleziona la figura di cui vuoi conoscere il perimetro o la circonferenza!:")


if (selection == "A"): square_perimeter()
elif (selection == "B"): rectangle_perimeter()
elif (selection == "C"): circumference()
else: print("La scelta non è valida, ricorda di utilizzare lettere maiuscole per la scelta!")