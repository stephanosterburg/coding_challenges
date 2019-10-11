def flippingBits(n):
    for i in n:
        x = int(bin(i)[2:])
        flipped = ~x & 0xffffffff
        print(x, ~x)


n = [0, 802743475, 35601423]
flippingBits(n) # 4294967295, 3492223820, 4259365872
