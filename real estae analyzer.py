def getFloatInput(prompt):
    
    while True:
        try:
            user_input = input(prompt + " ")
            value = float(user_input)
            
            if value <= 0:
                print("Error: Please enter a positive, non-zero number.")
                continue
            
            return value
            
        except ValueError:
            print("Error: Please enter a valid numeric value.")
            continue


def getMedian(data_list):
    """
    Calculate the median of a list without using the statistics module.
    
    Parameters:
    data_list (list): A list of numeric values
    
    Returns:
    float: The median value of the list
    """
    
    sorted_list = sorted(data_list)
    
    
    count = len(sorted_list)
    
    
    if count % 2 == 1:
        
        median_index = count // 2
        median = float(sorted_list[median_index])
    else:
        
        upper_index = count // 2
        lower_index = upper_index - 1
        
        median = float((sorted_list[lower_index] + sorted_list[upper_index]) / 2)
    
    return median


def main():
    """
    Main function for BDJ Real Estate Sales Analyzer.
    Collects sales values and performs statistical analysis.
    """
    
    sales_values = []
    
    print("BDJ Real Estate of Springfield - Sales Analyzer")
    print("=" * 50)
    
    
    while True:
        
        fSalesPrice = getFloatInput("Enter property sales value:")
        
        
        sales_values.append(fSalesPrice)
        
        
        while True:
            continue_input = input("Enter another value Y or N: ").strip()
            
            if continue_input.upper() == 'Y':
                break  
            elif continue_input.upper() == 'N':
                break  
            else:
                print("Please enter Y, y, N, or n only.")
                continue
        
        
        if continue_input.upper() == 'N':
            break
    
    
    sales_values.sort()
    
    
    print("\n" + "=" * 50)
    print("SALES ANALYSIS RESULTS")
    print("=" * 50)
    
    
    print("Property Sales Values (Sorted):")
    for i, value in enumerate(sales_values, 1):
        print(f"  Property {i}: ${value:,.2f}")
    
    
    minimum_value = min(sales_values)
    maximum_value = max(sales_values)
    total_value = sum(sales_values)
    average_value = total_value / len(sales_values)
    median_value = getMedian(sales_values)  
    commission = total_value * 0.03  
    
    print(f"\nSales Statistics:")
    print(f"  Minimum Value: ${minimum_value:,.2f}")
    print(f"  Maximum Value: ${maximum_value:,.2f}")
    print(f"  Total Value:   ${total_value:,.2f}")
    print(f"  Average Value: ${average_value:,.2f}")
    print(f"  Median Value:  ${median_value:,.2f}")
    print(f"  Commission:    ${commission:,.2f}")
    
    print("\nThank you for using BDJ Real Estate Sales Analyzer.")
if __name__ == "__main__":
    main()
