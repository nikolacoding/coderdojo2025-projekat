from p5 import *
from make_planet import make_planet

# run() izvrsava setup() jednom, na pocetku izvrsavanja
def setup():
    size(900, 900) # generisanje prozora dimenzija 900x900
    load_planets() # ucitavanje planeta (davanje vrijednosti globalnim promjenljivim unutar ove funkcije)

# run() izvrsava draw() svaki frejm
def draw():
    background(0)    # pozadina crne boje
    draw_sun()       # iscrtavanje sunca
    draw_orbits()    # iscrtavanje orbita svake planete
    draw_planets()   # iscrtavanje samih planeta

# funkcija koja ucitava planete tako sto globalnim dict-ovima koji reprezentuju pojedinacne planete dodjeljuje
# vrijednost i stavlja ih sve u globalnu listu kojoj dalje u kodu pristupamo po volji
def load_planets():
    global mercury, venus, earth, mars, jupiter, saturn, uranus, neptune # deklaracija svih planeta
    global planetList # deklaracija liste koja ce da ih u sebi cuva

    mercury = {
        "name": "Merkur",
        "color": Color(165, 42, 42),
        "size": 15,
        "orbit": 150,
        "speed": 1,
    }

    venus = {
        "name": "Venera",
        "color": Color(255, 190, 200),
        "size": 30,
        "orbit": 200,
        "speed": 0.75,
    }

    earth = {
        "name": "Zemlja",
        "color": Color(104, 149, 197),
        "size": 35,
        "orbit": 300,
        "speed": 0.5,
    }

    mars = {
        "name": "Mars",
        "color": Color(223, 30, 38),
        "size": 15,
        "orbit": 400,
        "speed": 0.4,
    }

    jupiter = {
        "name": "Jupiter",
        "color": Color(148, 26, 28),
        "size": 60,
        "orbit": 500,
        "speed": 0.3,
    }

    saturn = {
        "name": "Saturn",
        "color": Color(241, 169, 78),
        "size": 50,
        "orbit": 600,
        "speed": 0.2,
    }

    uranus = {
        "name": "Uran",
        "color": Color(214, 236, 239),
        "size": 40,
        "orbit": 700,
        "speed": 0.1,
    }

    neptune = {
        "name": "Neptun",
        "color": Color(0, 105, 148),
        "size": 40,
        "orbit": 800,
        "speed": 0.075,
    }

    planetList = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

def draw_sun():
    fill(255, 255, 0) # prvo pozivamo funkcije koje diktiraju parametrima objekta, pa tek onda instanciramo objekat
    ellipse(width / 2 , height / 2, 75, 75) # elipsa sunca koju ovdje instanciramo ce biti fillovana u skladu sa
    # funkcijom pozvanom iznad

def draw_orbits():
    no_fill() # orbita je samo obim kruga, tj. nije filovana iznutra
    stroke(255) # iscrtavanje bijele boje oko elipsi ciji obimi reprezentuju orbite

    for planet in planetList:
        ellipse(width / 2, height / 2, planet["orbit"], planet["orbit"])

def draw_planets():
    for planet in planetList:
        color = planet["color"]
        orbit = planet["orbit"]
        size = planet["size"]
        speed = planet["speed"]

        make_planet(
            color,
            orbit,
            size,
            speed
        )

run(frame_rate=60) # pokretanje