
# Exercise: File Manipulation
def file_exercise():
    test_file = "sae24_test.txt"
    with open(test_file, "w") as f:
        f.write("Line 1: Network Analysis\nLine 2: Scapy is powerful\nLine 3: Python is great")
    
    with open(test_file, "r") as f:
        lines = f.readlines()
        processed = [line.upper() for line in lines]
    
    print("File Processed: ", processed)

# Exercise: String Manipulation
def string_exercise():
    data = "USER touriste\nPASS 3aboqphie=3qbc!"
    lines = data.split("\n")
    user = lines[0].replace("USER ", "")
    password = lines[1].replace("PASS ", "")
    print(f"Parsed -> User: {user}, Pass: {password}")

if __name__ == "__main__":
    print("--- File Exercise ---")
    file_exercise()
    print("\n--- String Exercise ---")
    string_exercise()
