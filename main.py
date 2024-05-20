import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv')


def search_data(query):
    return data[data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]

# Function to visualize dataset
def visualize_data(column):
    plt.figure(figsize=(10, 6))
    data[column].value_counts().plot(kind='bar')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

# Main function
def main():
    print("Dataset Analysis Tool")
    while True:
        print("\nOptions:")
        print("1. Search Data")
        print("2. Visualize Data")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            query = input("Enter search query: ")
            print(search_data(query))
        elif choice == '2':
            column = input("Enter column name to visualize: ")
            visualize_data(column)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
