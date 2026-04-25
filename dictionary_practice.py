contestants = {
    "Tejas":200,
    "Amar": 50,
    "Anand":60,
    "Samadhan":150,
    "Vikas":45,
    "Vaishu":15,
    "Kirti":35,
    "Vaibhav":90,
    "Surekha":88,
    "Chinchu":19
    }


for name, score in contestants.items():
    if score>50 or score==50:
        print(f"{name} is Pro contributer with {score} points\n")


    else:
        print(f"{name} it just starting with {score} points. keep it up!\n")