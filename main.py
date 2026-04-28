class User:
  count = 0

  def __init__(self, name:str, login:str, password:str, grade:int):
    self.name = name
    self._login = login
    self._password = password

    if not isinstance(grade, int) or grade <= 0:
            raise ValueError("Параметр должен быть целым числом больше 0")
    self.__grade = grade
    type(self).count += 1

  # login
  @property
  def login(self):
    return self._login

  @login.setter
  def login(self, login):
    print('Невозможно изменить логин!')

  # password
  @property
  def password(self):
    print('***********')

  @password.setter
  def password(self, password):
    self._password = password

  # grade
  @property
  def grade(self):
      return "Неизвестное свойство grade"

  @grade.setter
  def grade(self, value):
      print("Неизвестное свойство grade")

  # методы
  def show_info(self):
     print(f"User Info -> Name: {self.name}, Login: {self.login}")

  # Сравнение объектов
  def __eq__(self, other):
    if isinstance(other, User):
      return self.__grade == other.__grade
    return NotImplemented

  def __lt__(self, other):
      if isinstance(other, User):
          return self.__grade < other.__grade
      return NotImplemented

  def __gt__(self, other):
      if isinstance(other, User):
          return self.__grade > other.__grade
      return NotImplemented

class SuperUser(User):
  def __init__(self, name:str, login:str, password:str, role:str, grade:int):
    super().__init__(name, login, password, grade)

    self.role = role

  def show_info(self):
        super().show_info()
        print(f"Role: {self.role}")

#-------- Вывод --------

user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)
admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

users = User.count
admins = SuperUser.count

print(user1.show_info())
print(admin.show_info())
print('------------------')
print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}')
print('------------------')
print(user1 < user2)
print(admin > user3)
print(user1 == user3)
print('------------------')
user3.name = 'Ringo Star'
user1.password = 'Pa$$w0rd'

print(user3.name)
print(user2.password)
print(user2.login)

user2.login = 'geo'

print(user1.grade)
admin.grade = 10

input('Нажмите Enter, чтобы выйти....')