
from main import main
import pytest
from src.Logica_python.filter import high_filter, low_filter, medium_filter
lista = [
    {
        "name": "Dragon",
        "plates": [
            "Rollitos de primavera",
            "Ternera con salsa de ostras",
            "helado frito"
        ],
        "drink": "agua, vino",
        "stock": 53,
        "price": 12.95,
        "discount": 5,
        "valoration": 4.2
    },
    {
        "name": "Hainan",
        "plates": [
            "Ensalada china",
            "Pollo con setas chinas y bambú",
            "Helado frito"
        ],
        "drink": "agua o refresco",
        "stock": 50,
        "price": 25.95,
        "discount": 5,
        "valoration": 2.2
    },
    {
        "name": "Sichuan",
        "plates": [
            "Cerdo agridulce",
            "Chop Suwy de gambas",
            "Helado con almendras"
        ],
        "drink": "refresco",
        "stock": 50,
        "price": 48.95,
        "discount": 5,
        "valoration": 3.6
    },
    {
        "name": "Pekín",
        "plates": [
            "Sopa de tiburón",
            "Pato Pekín",
            "Liche en su jugo"
        ],
        "drink": "Ramune",
        "stock": 32,
        "price": 23.59,
        "discount": 5,
        "valoration": 4.4
    },
    {
        "name": "Roma",
        "plates": [
            "Lasaña",
            "Risotto alla milanese",
            "Carpaccio"
        ],
        "drink": "Agua o refresco",
        "stock": 50,
        "price": 14.99,
        "discount": 5,
        "valoration": 4.6
    },
    {
        "name": "Pizza",
        "plates": [
            "Pizza",
            "Ensalada carpresse",
            "Ossobuco"
        ],
        "drink": "Agua o refresco",
        "stock": 50,
        "price": 16.50,
        "discount": 5,
        "valoration": 3.2
    },
    {
        "name": "Venecia",
        "plates": [
            "Agnolotti",
            "Bucatini",
            "La polenta"
        ],
        "drink": "Agua o refresco",
        "stock": 35,
        "price": 20,
        "discount": 5,
        "valoration": 5.0
    },
    {
        "name": "De la casa",
        "plates": [
            "Arroz a la mexicana",
            "Albondigas de pollo en salsa de chile chipodle",
            "Platanos con crema y canela"
        ],
        "drink": "refresco",
        "stock": 10,
        "price": 17.90,
        "discount": 0,
        "valoration": 4.0
    },
    {
        "name": "Macho",
        "plates": [
            "Chiles en nogada",
            "Tortas ahogadas",
            "Carlota de Limón"
        ],
        "drink": "Cerveza con tequila y limón",
        "stock": 7,
        "price": 15.10,
        "discount": 10,
        "valoration": 1.8
    },
    {
        "name": "Borgoña",
        "plates": [
            "Baguette tostada con queso de cabra",
            "Le mique",
            "Tarta Tartin"
        ],
        "drink": "Vino, gaseosa o refresco",
        "stock": 62,
        "price": 15.25,
        "discount": 5,
        "valoration": 4.0
    },
    {
        "name": "Auvernia",
        "plates": [
            "La potée",
            "Gallo al vino",
            "Pastel de cerezas"
        ],
        "drink": "Vino, gaseosa o Agua",
        "stock": 15,
        "price": 22.95,
        "discount": 0,
        "valoration": 4.2
    }
]
@pytest.mark.filtro_listas
def test_low_filter():
    assert isinstance(low_filter(lista), list)

@pytest.mark.filtro_listas
def test_medium_filter():
    assert isinstance(medium_filter(lista), list)

@pytest.mark.filtro_listas
def test_high_filter():
    assert isinstance(high_filter(lista), list)