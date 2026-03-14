def dzielenie(a, b):
    if b == 0:
        print("nie mozna dzielic przez zero")
        return None;
    return a/b;

def CalculateAverage(values):
    srednia = 0
    dlugosc = 0
    for v in values:
        srednia += v
        dlugosc += 1
    return srednia/dlugosc
