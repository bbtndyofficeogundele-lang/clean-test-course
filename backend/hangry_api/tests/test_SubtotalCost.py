from types import SimpleNamespace

from api.controllers import Subtotal


def item(quantity, price):
  return SimpleNamespace(quantity=quantity, item=SimpleNamespace(price=price))


def test_SimpleCost():
  #Arrange
  order = [item(5, 1.0), item(5, 1.0), item(5, 1.0)]
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 15


def test_ComplexCost():
  #Arrange
  order = [item(2, 3.5), item(1, 4.5)]
  #Act
  cost = Subtotal.calculate(order)
  #Assert
  assert cost == 11.5
