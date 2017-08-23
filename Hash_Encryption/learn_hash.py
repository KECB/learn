
def bkdr_hash(code):
    seed = 131  # 通常使用素数, 31, 131, 1313, 13131, 131313 等
    hash_result = 0
    for i in range(len(code)):
        hash_result = (hash_result * seed) + ord(code[i])
    return hash_result


print(bkdr_hash('JKiidalk'))
