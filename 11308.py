def main():
    t = int(input().strip())  
    for _ in range(t):
        title = input().strip()
        m, n, b = map(int, input().strip().split())  
        ingredientes = {}
        for _ in range(m):
            ingred, preco = input().strip().split()
            preco = int(preco)
            ingredientes[ingred] = preco
        recipes = {}
        for _ in range(n):
            recipe_name = input().strip()
            k = int(input().strip())  
            total_cost = 0
            for _ in range(k):
                ingred, quant = input().strip().split()
                quant = int(quant)
                total_cost += ingredientes[ingred] * quant
            if total_cost <= b:
                recipes[recipe_name] = total_cost
        print(title.upper())
        if recipes:
            for recipe in sorted(recipes, key=lambda x: (recipes[x], x)):
                print(recipe)
        else:
            print("Too expensive!")
        print()

if __name__ == "__main__":
    main()