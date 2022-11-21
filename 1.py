def convertBase3(n):
    if (n == 0):
        return;
    x = n % 3;
    n //= 3;
    if (x < 0):
        n += 1;
    convertBase3(n);
    if (x < 0):
        print(x + (3 * -1), end = "");
    else:
        print(x, end = "");
def convert(n):
    if (n != 0):
        convertBase3(n);
    else:
        print("0");
n = int(input());
convert(n);
