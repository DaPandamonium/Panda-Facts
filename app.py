from flask import Flask, jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)

# List of panda facts
panda_facts = [
    "A giant panda's appetite for bamboo is insatiable. They eat bamboo up to 12 hours a day. That’s over 28 pounds (12.5 kilograms) of bamboo!",
    "Pandas can stand upright, but their short hind legs aren't strong enough to support their hefty bodies. A panda's bones are twice as heavy as the bones of other animals the same size.",
    "Giant pandas are good at climbing trees and can also swim.",
    "Pandas have been known to eat up to 14 different species of bamboo.",
    "Unlike most other bears, pandas do not hibernate. When winter approaches, they move lower down their mountain habitats to warmer temperatures, where they continue to chomp away on bamboo!",
    "Giant pandas have a unique thumb - actually a modified wrist bone - that helps them hold bamboo while eating.",
    "Baby pandas are born pink, blind, and hairless. The iconic black and white coloring comes later, after about three weeks.",
    "Giant pandas spend around 55% of their life collecting, preparing, and eating bamboo.",
    "The life span of giant pandas in the wild is approximately 20 years. However, in captivity, they can live up to 30 years or more.",
    "Despite their exalted status and relative lack of natural predators, pandas are endangered. Only about 1,800 pandas live in the wild, with another few hundred in zoos and breeding centers around the world.",
    "Pandas are solitary animals, and they have territories that they mark with urine and claw marks.",
    "The giant panda is a symbol of peace in China. Hundreds of years ago, tribes would raise a flag with a picture of a panda on it to stop a battle or declare a truce.",
    "Giant pandas have a very slow reproductive rate, typically giving birth to one cub every two years. Cubs stay with their mothers for up to three years before venturing off on their own, which means a panda may only raise two or three cubs in her lifetime.",
    "Pandas have a carnivorous digestive system but have evolved to depend almost entirely on bamboo. This diet is not very nutritious, so they have to eat a lot to get enough nutrients."
]


@app.route('/')
def index():
    fact = random.choice(panda_facts)
    return jsonify(fact=fact)

if __name__ == '__main__':
    app.run(debug=True)
