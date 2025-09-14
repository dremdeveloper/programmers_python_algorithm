# 제목: 에라토스테네스의 체로 소수 빠르게 판별하기

# 에라토스테네스의 체는 특정 범위(1부터 N까지) 내의 모든 소수를
# 매우 효율적으로 찾아내는 알고리즘입니다.

def sieve(n):
    # 1. n+1 크기의 리스트를 만들어 True로 초기화 (모두 소수라고 가정)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아님

    # 2. 2부터 n의 제곱근까지만 확인
    for i in range(2, int(n**0.5) + 1):
        # 만약 i가 소수라면
        if is_prime[i]:
            # i의 배수들을 모두 소수가 아니라고 표시 (i 자신은 제외)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    # 3. is_prime 리스트에서 True인 인덱스만 추출
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

# 테스트
N = 100
prime_numbers = sieve(N)
print(f"1부터 {N}까지의 소수:")
print(prime_numbers)