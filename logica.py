

def logica(cartas):
    print("Entra en logica")
    print(cartas)

    lista_cartas = []
    if "4.PNG" in cartas:
        print("ENTRA EN 4 PNG")
        if "carrot_hummer.PNG" in cartas:
            lista_cartas.append("carrot_hummer.PNG")
            if "vine_dagger.PNG" in cartas:
                lista_cartas.append("vine_dagger.PNG")

    elif "vegan_diet.PNG" in cartas:
        lista_cartas.append("vegan_diet.PNG")
