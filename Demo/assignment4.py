# Class 1: Business 
class Business:
#Business attributes
    def __init__(self, name, owner, sector, location, capital, employees, revenue):
        self.name = name          # Name of the business
        self.owner = owner        # Owner's name
        self.sector = sector      # Business sector 
        self.location = location  # Town 
        self.capital = capital    # Initial investment in UGX
        self.employees = employees # Number of employees
        self.revenue = revenue    # Annual revenue in UGX

# Business objects
b1 = Business("Green Farms", "Julius", "Agriculture", "Ggaba", 50000000, 10, 12000000)
b2 = Business("Sunshine Bakery", "Christine", "Food", "Mukono", 30000000, 5, 80000000)
b3 = Business("Tech Solutions", "Samson", "IT", "Kampala", 100000000, 8, 250000000)
b4 = Business("Fresh Veggies", "Amina", "Agriculture", "Jinja", 20000000, 4, 50000000)
b5 = Business("Coffee Corner", "David", "Food", "Masaka", 40000000, 6, 10000000)
b6 = Business("Craft Hub", "Lydia", "Handicraft", "Mbale", 15000000, 3, 350000000)
b7 = Business("Bookstore Plus", "Kevin", "Retail", "Fort Portal", 35000000, 5, 90000000)

# Class 2: Student
class Student:
#Students attributes
    def __init__(self, name, age, grade, student_id, course, email, country):
        self.name = name #name of a student
        self.age = age #age of a student
        self.grade = grade  #grade of a student
        self.student_id = student_id #student identification number
        self.major = course   #course persued
        self.email = email  #student email
        self.country = country #country of origin

#  Student objects
s1 = Student("Janet", 20, "A", "S001", "Computer Science", "janet@email.com", "Uganda")
s2 = Student("Mukasa", 21, "B", "S002", "Education in Mathematics", "mukasa@email.com", "kenya")
s3 = Student("Aisha", 19, "A", "S003", "Electrical Engineering", "aisha@email.com", "Tanzania")
s4 = Student("Kato", 22, "C", "S004", "Medicine and surgery", "kato@email.com", "Uganda")
s5 = Student("Eriya", 20, "B", "S005", "Chemical Engineering", "eriya@email.com", "Burundi")
s6 = Student("Samson", 23, "A", "S006", "Software Engineering", "samson@email.com", "Uganda")
s7 = Student("Lillian", 21, "B", "S007", "Business Administration", "lillian@email.com", "Uganda")

# Class 3: Book
class Book:
#book attributes
    def __init__(self, title, author, genre, pages, publisher, price, year):
        self.title = title #book title
        self.author = author # author of the book
        self.genre = genre #genre of the book
        self.pages = pages   #pages in the book
        self.publisher = publisher # the publishers of the book
        self.price = price  #price of thr book in UGX
        self.year = year  #yeah the book was published

# Book objects
b1 = Book("Python Basics", "Julie Marie", "Education", 250, "TechPub", 30000, 2020)
b2 = Book("Data Science 101", "Jane Smith", "Education", 300, "EduPub", 35000, 2021)
b3 = Book("World History", "Mike Brown", "History", 500, "HistPub", 40000, 2018)
b4 = Book("Fiction Tales", "Anna White", "Fiction", 200, "FicPub", 25000, 2019)
b5 = Book("Math Made Easy", "Peter Green", "Education", 150, "MathPub", 20000, 2020)
b6 = Book("Cooking Mastery", "Lucy Grey", "Cooking", 180, "CookPub", 28000, 2021)
b7 = Book("Gardening Tips", "Tom Blue", "Lifestyle", 120, "LifePub", 18000, 2022)

# Class 4: Laptop
class Laptop:
#Laptop attributes
    def __init__(self, brand, model, cpu, ram, storage, color, price):
        self.brand = brand  #laptop brand
        self.model = model  # laptop mode
        self.cpu = cpu  #Central processing Unit of the Laptop
        self.ram = ram #Random access memory of the laptop
        self.storage = storage #internal storage of the laptop
        self.color = color  #color of the laptop
        self.price = price  #price of the laptop in UGX

# Laptop objects
l1 = Laptop("Dell", "Inspiron", "i5", 8, 512, "Black", 800000)
l2 = Laptop("HP", "Pavilion", "i7", 16, 1024, "Silver", 1200000)
l3 = Laptop("Apple", "MacBook Air", "M1", 8, 512, "Grey", 1500000)
l4 = Laptop("Lenovo", "ThinkPad", "i5", 8, 256, "Black", 900000)
l5 = Laptop("Asus", "VivoBook", "i3", 4, 512, "Blue", 700000)
l6 = Laptop("Acer", "Aspire", "i7", 16, 1024, "White", 1100000)
l7 = Laptop("MSI", "Stealth", "i9", 32, 2048, "Black", 2500000)

# Class 5: MobilePhone
class MobilePhone:
#Mobilephone attributes
    def __init__(self, brand, model, os, ram, storage, color, price):
        self.brand = brand  #phone brand
        self.model = model  #phone model
        self.os = os   #operating system the phone uses
        self.ram = ram  #Random acess memory of the phone
        self.storage = storage  #phone internal storage
        self.color = color  #phone color
        self.price = price #price of the phone in UGX

#  MobilePhone objects
m1 = MobilePhone("Samsung", "Galaxy S21", "Android", 8, 128, "Black", 900)
m2 = MobilePhone("Apple", "iPhone 14", "iOS", 6, 256, "White", 1200)
m3 = MobilePhone("Xiaomi", "Redmi Note 12", "Android", 4, 128, "Blue", 300)
m4 = MobilePhone("OnePlus", "9 Pro", "Android", 12, 256, "Green", 1000)
m5 = MobilePhone("Google", "Pixel 7", "Android", 8, 128, "Black", 800)
m6 = MobilePhone("Nokia", "G50", "Android", 4, 64, "Grey", 250)
m7 = MobilePhone("Huawei", "P50", "Android", 8, 256, "Silver", 700)

# Class 6: Employee
class Employee:
#Employee atributes
    def __init__(self, name, emp_id, department, position, salary, age, country):
        self.name = name  #Employee's name
        self.emp_id = emp_id #Employee identification number
        self.department = department  #department of the employee
        self.position = position  # position of the employee
        self.salary = salary    #Salary the employee is paid in UGX
        self.age = age   #age of an employee
        self.country = country  #Country of birth of the employee

#  Employee objects 
e1 = Employee("Alice", "E001", "HR", "Manager", 5000000, 30, "Uganda")
e2 = Employee("Mukisa", "E002", "IT", "Developer", 4000000, 28, "Uganda")
e3 = Employee("Aisha", "E003", "Finance", "Analyst", 4500000, 32, "Uganda")
e4 = Employee("Kato", "E004", "Marketing", "Executive", 3500000, 29, "Uganda")
e5 = Employee("Eriya", "E005", "IT", "Designer", 3800000, 27, "Uganda")
e6 = Employee("Samson", "E006", "HR", "Assistant", 3000000, 26, "Uganda")
e7 = Employee("Lillian", "E007", "Finance", "Manager", 5500000, 35, "Uganda")

# Class 7: Farmer 
class Farmer:
# farmer attributes
    def __init__(self, name, age, village, farm_size, crops, livestock, experience_years):
        self.name = name  #name of the farmer
        self.age = age   #age of the farmer
        self.village = village  #village where the farm is found
        self.farm_size = farm_size  #size of land in acres
        self.crops = crops    #type of crop grown in the farm
        self.livestock = livestock   #type of animals kept in the farm
        self.experience_years = experience_years  #Years the farmer has spent in the farming business

# Farmer objects 
f1 = Farmer("Julius", 40, "Ggaba", 5, "Beans", "Goats", 15)
f2 = Farmer("Christine", 35, "Mukono", 3, "Cassava",  "Cows", 10)
f3 = Farmer("Patrick", 50, "Entebbe", 10,  "Sugarcane", "Chickens", 25)
f4 = Farmer("Amina", 28, "Jinja", 2, "Onions", "Pigs", 5)
f5 = Farmer("David", 45, "Masaka", 8, "Groundnuts", "Goats", 20)
f6 = Farmer("Lydia", 30, "Mbale", 4, "Coffee", "Cows", 12)
f7 = Farmer("Kevin", 38, "Fort Portal", 6, "Maize", "Sheep", 18)
