def add(a, b):
    return a + b


def sub(a, b):
    return a - b
def div(a, b):
    if b == 0:
        raise ValueError("Khong chia duoc")
    return a / b

def div(a, b):
    if b == 0:
       return "Loi: chia cho 0"
    return a / b