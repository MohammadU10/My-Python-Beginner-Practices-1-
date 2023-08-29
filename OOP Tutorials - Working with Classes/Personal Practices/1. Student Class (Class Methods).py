
# Class Definition And Methods :
class Student:
    id = 0
    num_of_students = 0
    bonus_amt = 0.5
    list_of_scores = []
    
    def __init__(self, first, last, score):
        self.first = first
        self.last = last
        self.score = score
        
        self.score = self.score + self.bonus_amt
        self.score = round(self.score)
        
        self.email = f'{first}.{last}@email.com'
        Student.id += 1
        print(f'Student ({Student.id}):\tFirst Name: {self.first}\tLast Name: {self.last}\tEmail: {self.email}\tScore: {self.score}\tStatus: {Student.is_failed(self)}\n')
        
        Student.num_of_students += 1
        Student.list_of_scores.append(self.score)
    
    def is_failed(self):
        if self.score < 10:
            return "Failed!"
        else:
            return "Passed!"
    
    
    # Class Methods :
    @classmethod
    def set_bonus(cls, amount):
        cls.bonus_amt = amount
    
    @classmethod
    def average_of_scores(cls):
        total = 0
        for score in cls.list_of_scores:
            total += score
        average = total / cls.num_of_students
        return average
    
    @classmethod
    def passed_and_failed_count(cls):
        failed = 0
        passed = 0
        
        for score in cls.list_of_scores:
            if score < 10:
                failed += 1
            else:
                passed +=1
        return f'Passed Count: {passed}\nFailed Count: {failed}'
    
    @classmethod
    def max_and_min(cls):
        max = cls.list_of_scores[0]
        min = cls.list_of_scores[0]

        for num in cls.list_of_scores:
            if num > max:
                max = num
            if num < min:
                min = num
        return f'Maximum Score: {max}\nMinimum Score: {min}'


# Output And Class Objects :
Student.set_bonus(1)

std_1 = Student('Corey', 'Schafer', 19.5)
std_2 = Student('Test1', 'User1', 14.5)
std_3 = Student('Test2', 'User2', 8)
std_4 = Student('Test3', 'User3', 5)
std_5 = Student('Test4', 'User4', 10)


# print(std_1.first)
# print(std_1.last)
# print(std_1.email)
# print(std_1.score)
# print(std_1.is_failed())


print("List of the Scores:", Student.list_of_scores, '\n')

print("Average of the Scores:", round(Student.average_of_scores(), 1), '\n')

print("Students Count:", Student.num_of_students, '\n')

print(Student.passed_and_failed_count(), '\n')

print(Student.max_and_min())