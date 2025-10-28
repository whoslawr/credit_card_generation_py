import random

def getBank():
    banks = ["Banca Transilvania", "BRD", "Raiffeisen Bank", "CEC Bank", "BCR"]
    bank = random.choice(banks)
    return bank

def getName():
    name = ""
    first_name = ["Laurentiu", "Andrei", "Bogdan", "Alexandru", "Marius", "Cosmin", "Darius", "Alin", "Daniel", "Vlad", "David"]
    middle_name = ["Ioan", "Nicolae", "Dumitru", "Gabriel", "Sebastian", "Mihai"]
    last_name = ["Molnar", "Popescu", "Ignat", "Dulau", "Maier", "Barbu", "Chiorean", "Strajan", "Moldovan"]
    name = random.choice(first_name) + "-" + random.choice(middle_name) + " " + random.choice(last_name)
    return name

def createCARDNUMBER():
    card_number = ""
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(numbers)
    for i in range(16):
        card_number = card_number + random.choice(numbers)
    card_number = card_number[:4] + ' ' + card_number[4:]
    card_number = card_number[:9] + ' ' + card_number[9:]
    card_number = card_number[:14] + ' ' + card_number[14:]
    return card_number

def createExpDate():
    EXPdate = ""
    number_of_months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    year_possibilities = ['22', '23', '24', '25', '26', '27', '28', '29', '30']
    month = random.choice(number_of_months)
    year = random.choice(year_possibilities)
    EXPdate = month + '/' + year
    return EXPdate

def createCVV():
    cvv = ""
    cvvNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(cvvNumbers)
    for i in range(3):
        cvv = cvv + random.choice(cvvNumbers)
    return cvv

BANK = getBank()
Name = getName()
cardNumber = createCARDNUMBER()
expDate = createExpDate()
cVv = createCVV()
print()
print('\033[1m' + "Your card information is:" + '\033[0m\n')
print("BANK: " + BANK)
print("NAME: " + Name)
print("CARD NUMBER:", cardNumber)
print("EXP DATE:", expDate)
print("CVV:", cVv)
print()
