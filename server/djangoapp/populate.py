from .models import CarMake, CarModel


def initiate():
    data = {
        "Toyota": ["Camry", "RAV4", "Corolla"],
        "Honda": ["Civic", "CR-V", "Accord"],
        "Ford": ["Focus", "Escape", "Explorer"],
    }
    types = {"Camry": "SEDAN", "Corolla": "SEDAN", "Civic": "SEDAN",
             "Accord": "SEDAN", "Focus": "SEDAN"}
    for make_name, models_list in data.items():
        make, _ = CarMake.objects.get_or_create(
            name=make_name, defaults={"description": f"{make_name} cars"})
        for m in models_list:
            CarModel.objects.get_or_create(
                car_make=make, name=m,
                defaults={"type": types.get(m, "SUV"), "year": 2023})
