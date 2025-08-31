import os
import random
import matplotlib.pyplot as plt

# Create output folder if not exists
OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def generate_bar_chart():
    # Sample categories
    categories = ["A", "B", "C", "D", "E"]
    
    # Generate random data for each category
    values = [random.randint(10, 100) for _ in categories]
    
    # Create the bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(categories, values)
    plt.title("Random Bar Chart")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    
    # Save chart in PNG format inside output folder
    file_path = os.path.join(OUTPUT_FOLDER, "bar_chart.png")
    plt.savefig(file_path)
    plt.close()
    
    print(f"Bar chart saved at: {file_path}")
