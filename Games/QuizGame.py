
Questions=[
    {
        'prompt':'Where is Sagarmatha located ?',
        'Options':['A.India','B.China','C.Nepal','D.Pakistan'],
        'answer':'C'
    },
    {
        'prompt':'What is the capital of Nepal?',
        'Options':['A.Kathmandu','B.New Delhi','C.Beijing','D.Kuala Lumpur'],
        'answer': 'A'
    },
    {
        'prompt': 'What is the capital of France?',
        'Options': ['A. Paris', 'B. Berlin', 'C. Madrid', 'D. Rome'],
        'answer': 'A'
    },
    {
        'prompt': 'Which planet is known as the Red Planet?',
        'Options': ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Venus'],
        'answer': 'B'
    }
]


def Quiz(Questions):
    score=0
    for question in Questions:
        print(question['prompt'])
        for option in question['Options']:
            print(option)
        answer=input("Enter Your Answer (A,B,C,D) \n").upper()
        if answer==question['answer']:
            print("Correct")
            score+=1
        else:
            print("Wrong Answer. Correct is ",question['answer'],"\n")
    print(f"You have {score} out of {len(Questions)}")

Quiz(Questions)
