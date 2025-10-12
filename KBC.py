questions = [
    "What is the capital of India?",
    "Which planet is known as the Red Planet?",
    "Who painted the Mona Lisa?",
    "What is the national animal of India?",
    "Which is the smallest prime number?"
]

options = [
    ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
    ["A. Jupiter", "B. Venus", "C. Mars", "D. Saturn"],
    ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
    ["A. Tiger", "B. Lion", "C. Elephant", "D. Peacock"],
    ["A. 0", "B. 1", "C. 2", "D. 3"]
]
# opt = list(options)
# opt[0] = "पीलिया"
# opt[2] = "मस्तिष्क ज्वर"
answers = [1,3,3,1,3]
prize_money = [1000, 2000, 3000, 5000, 10000]


total = 0

print("welcome to KBC game \n")
print("play carefully! One wrong answer and you will lose everything\n")

for i in range(len(questions)):
    print(f"\nQ{i+1}: {questions[i]}")
    for opt in options[i]:
        print(opt)
        
    ans = input("your ans (A/B/C/D): ").strip().upper()
    mapping = {"A":1,"B":2,"C":3,"D":4}

    if ans not in mapping:
     print("invaled choise game over.")
     break
     
    if mapping[ans] == answers[i]:
     print("correct answer")
     total += prize_money[i]
     print(f"you have won ${total}\n")

    else:
     print("wrong answer")
     print(f"correct answer was {options[i][answers[i]-1]}") 
     break
    
    

print(f"\n game over . you won a total of ${total}")