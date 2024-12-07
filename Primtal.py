import math


def primtal_calc(amount_of_primes: int) -> str:
    primtal = True
    tal = 1
    prime_numbers = [1, 2]
    while len(prime_numbers) <= amount_of_primes:
        tal += 2
        primtal = True
        övre_gräns = int(math.sqrt(tal) + 1) #  eftersom divisoner alltid kommer i par t.ex 100/2 = 50 och 100/50 = 2 kan vi ta roten ur talet för att hitta paret som är i mitten. 100^0.5 = 10 alltså 10 * 10 = 100 eller 100/10 = 10
        for i in range(3, övre_gräns, 2):
            check = tal % i
            if check == 0:
                primtal = False
                break
        if primtal:
            prime_numbers.append(str(tal) + " ")
    return f"Det här är det {(len(prime_numbers) -1)}de primtalet: {prime_numbers[-1]}"
    


