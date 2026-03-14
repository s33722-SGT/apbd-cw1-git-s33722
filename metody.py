def dzielenie(a, b):
    if b == 0:
        print("nie mozna dzielic przez zero")
        return None;
    return a/b;

def CalculateAverage(values):
    return sum(values) / len(values)

print(CalculateAverage([1,9,3,4,6,7,6,7]))
