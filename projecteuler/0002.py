from functools import reduce

def generate_fib_seq(stop=4000000) -> list:
    fib_terms = [1, 2]

    while True:
        next_term = fib_terms[-1] + fib_terms[-2]
        
        if next_term > stop:
            break
        
        fib_terms.append(next_term)
    
    return fib_terms

sum_even_terms = reduce(
    lambda sum, t: sum + t if not t % 2 else sum,
    generate_fib_seq(), 0)

print(sum_even_terms)