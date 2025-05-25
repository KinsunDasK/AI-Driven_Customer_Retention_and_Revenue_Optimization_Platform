file_path = "Kinsun\datasets\WA_Fn-UseC_-Telco-Customer-Churn.csv"
try:
    with open(file_path, 'r') as file:
        print("success")
        #read_data(file) # Correct: Passing the opened file object
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")