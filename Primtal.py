import math


def primtal_calc(amount_of_primes: int) -> None:
    primtal = True
    tal = 1
    prime_numbers = [1, 2]
    while len(prime_numbers) <= amount_of_primes:
        tal += 2
        primtal = True
        övre_gräns = int(math.sqrt(tal) + 1)
        for i in range(3, övre_gräns, 2):
            check = tal % i
            if check == 0:
                primtal = False
                break
        if primtal:
            prime_numbers.append(str(tal) + " ")
    return f"Det här är det {(len(prime_numbers) -1)}de primtalet: {prime_numbers[-1]}"
    

if __name__ == "__main__":
    lista = primtal_calc(10000)
    print(f"This is the {len(lista)}th prime number: {lista[-1]}")

