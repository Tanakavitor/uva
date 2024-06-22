def main():
     n = int(input().strip())
     for _ in range(n):
          placar1 , placar2 = input().strip()
          if placar1 < placar2:
               print("impossible")
          else:
               a = placar1/2
               b = placar1 - a
               print({a} + {b})
               
            

if __name__ == "__main__":
    main()
