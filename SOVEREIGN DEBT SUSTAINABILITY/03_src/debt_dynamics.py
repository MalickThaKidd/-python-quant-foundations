def main():
    d = float(input("What's your debt to PIB ratio ? "))
    r = float(input("What's your interest rate ? "))
    g = float(input("What's your GDP growth ? "))
    s = float(input("What's your solde primaire ? "))
    y = int(input("Enter de Horizon : "))

    result = simulate_debt(d,r,g,s,y)
    print(result)

def simulate_debt(d0, r, g, s, years):

    debt = d0
    trajectory = [d0]

    for year in range(years):

        debt = ((1+r)/(1+g))*debt - s 
        
        trajectory.append(debt)

    return trajectory

if __name__ == "__main__":
    main()