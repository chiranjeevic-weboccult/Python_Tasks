def match_questions_answers(question_file, answer_file, output_file):
    #Read and parse the question file
    with open(question_file, 'r') as qf:
        questions = {}
        for line in qf:
            line = line.strip()
            if line:  
                num, question = line.split('.', 1) 
                questions[int(num)] = question.strip()

    #Read and parse the answer file
    with open(answer_file, 'r') as af:
        answers = {}
        for line in af:
            line = line.strip()
            if line:  
                num, answer = line.split('.', 1)  
                answers[int(num)] = answer.strip()

    #Match questions and answers based on numeric keys
    with open(output_file, 'w') as of:
        for num in sorted(questions.keys()):  
            if num in answers:
                of.write(f"{num}. {questions[num]}\n")
                of.write(f"{answers[num]}\n\n")  


if __name__ == "__main__":
    question_file = "matching_qn_ans/questions.txt"
    answer_file = "matching_qn_ans/answers.txt"
    output_file = "matching_qn_ans/output.txt"

    match_questions_answers(question_file, answer_file, output_file)
    print(f"Questions and answers have been matched and saved to {output_file}.")