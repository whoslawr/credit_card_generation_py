def check_luhn(card_number):

	nDigits = len(card_number)
	numSum = 0
	isSecond = False

	for i in range(nDigits - 1, -1, -1):
		d = ord(card_number[i]) - ord('0')

		if isSecond == True:
			d *= 2

		numSum += d // 10
		numSum += d % 10

		isSecond = not isSecond

	if numSum % 10 == 0:
		return True
	else:
		return False

if __name__ == "__main__":
	card_number = "79927398713"

	if check_luhn(card_number):
		print("Valid card number.")
	else:
		print("Invalid card number.")