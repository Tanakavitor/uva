def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n_test = int(data[0].strip())
    index = 1
    
    results = []
    
    for _ in range(n_test):
        species_count = {}
        total_trees = 0
        
        while index < len(data) and data[index].strip() == "":  
            index += 1
        
        while index < len(data) and data[index].strip() != "":
            species = data[index].strip()
            if species in species_count:
                species_count[species] += 1
            else:
                species_count[species] = 1
            total_trees += 1
            index += 1
        
        while index < len(data) and data[index].strip() == "":  
            index += 1
        
        result = []
        for species in sorted(species_count.keys()):
            percentage = (species_count[species] / total_trees) * 100
            result.append(f"{species} {percentage:.4f}")
        
        results.append("\n".join(result))
    
    print("\n\n".join(results))

if __name__ == "__main__":
    main()
