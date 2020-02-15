def best_stock(a):
    # your code here
    sorted_by_value = sorted(a.items(), key=lambda kv: kv[1])
    
    return sorted_by_value[-1][0]


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))