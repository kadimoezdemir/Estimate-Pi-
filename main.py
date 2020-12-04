import random


def estimate_pi(rand_call_amounts):
    total_points = 0
    circle_points = 0

    for n in range(rand_call_amounts):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Normalerweise: math.sqrt(x²+y²),
        # aber da math.sqrt(1) = 1 ist und wir Zahlen kleinergleich 1 suchen, ist es hier egal!
        distance = x ** 2 + y ** 2

        if distance <= 1:
            circle_points += 1
        total_points += 1

    # Funkt: Kreisfläche = πr², Quadratfläche = a * a = (2*r) * (2*r) = (2*r)²
    # Kreisfläche/Quadratfläche == circle_points/total_points => Algebra= 4 * circle_points/total_points
    return 4 * circle_points / total_points


if __name__ == '__main__':
    rand_call_amounts = int(input("The Higher The Number The Better:"))
    print(estimate_pi(rand_call_amounts))
