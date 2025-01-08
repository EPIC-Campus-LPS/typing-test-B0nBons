import time

def typ():
    sentence = "The quick brown fox jumps over the lazy dog."    
    print("Type the following sentence:")
    print(f"\n{sentence}\n")
    
    start_time = time.time()
    user_input = input("Your input: ")

    end_time = time.time()
    time_taken = end_time - start_time
    
    mistakes = 0
    for i in range(min(len(sentence), len(user_input))):
        if sentence[i] != user_input[i]:
            mistakes += 1
    mistakes += abs(len(sentence) - len(user_input))
    
    print("\nYour results:")
    print(f"Time taken: {time_taken:.2f} seconds, with {mistakes} mistake(s).")
    
if __name__ == "__main__":
    typ()
