from typing import Union

class Polynomial:
	def __init__(self, coeffs = [0]):
		assert len(coeffs) >= 1
		self.coeffs = coeffs

	def __len__(self):
		return len(self.coeffs)

	def __str__(self):
		arr = []
		for enum, elem in enumerate(self.coeffs):
			if enum == 0:
				arr.append(str(elem))
			elif enum == 1:
				arr.append(str(elem) + 'x')
			else:
				arr.append(str(elem) + 'x^{}'.format(enum))
		return ' + '.join(map(str, arr[::-1]))

	def __repr__(self):
		return 'Polynomial({})'.format(self.coeffs)

	def __call__(self, x):
		res = 0
		for enum, coeff in enumerate(self.coeffs):
			res += coeff * pow(x, enum)
		return res

	def __eq__(self, other):
		return self.coeffs == other.coeffs

	def __add__(self, other):
		if type(other) == int:
			coeffs = self.coeffs
			coeffs[0] += other
			return Polynomial(coeffs)

		coeffs = [0] * max(len(self), len(other))
		for enum, coeff in enumerate(self.coeffs):
			coeffs[enum] += coeff
		for enum, coeff in enumerate(other.coeffs):
			coeffs[enum] += coeff
		return Polynomial(coeffs)

	def __mul__(self, other):
		if type(other) == int:
			coeffs = [elem * other for elem in self.coeffs]
			return Polynomial(coeffs)

		coeffs = [0] * (self.degree() + other.degree() + 1)
		for enum0, coeff0 in enumerate(self.coeffs):
			for enum1, coeff1 in enumerate(other.coeffs):
				coeffs[enum0 + enum1] += coeff0 * coeff1

		return Polynomial(coeffs)

	def degree(self):
		return len(self) - 1

