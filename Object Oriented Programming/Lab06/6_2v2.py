import datetime

# Class Code
class User:
       def __init__(self, id_card: str, name_surname: str, bank_id_list : str):
              if len(id_card.split('-')) == 13:
                     self.__id_card = id_card
              else:
                     return
              self.__name_surname = name_surname
              self.__bank_id_list = []
              if len(bank_id_list) == 10:
                     self.__bank_id_list.append(bank_id_list)
              else:
                     return

       def get_bank_id(self):
              return self.__bank_id

       bank_id = property(get_bank_id)

class Bank():
    def __init__(self) -> None:
        self.__user_list = []
        self.__bank_account_list = []
        self.__atm_card_list = []

    def add_user_list(self, user):
        self.__user_list.append(user)

    def add_bank_account(self, account):
        self.__bank_account_list.append(account)

    def add_atm_card_list(self, atm):
        self.__atm_card_list.append(atm)

    def get_user_list(self):
          return self.__user_list
    
    def get_bank_account_list(self):
          return self.__bank_account_list
    
    def get_atm_card_list(self):
          return self.__atm_card_list
    
    user_list = property(get_user_list,add_user_list)
    bank_account_list = property(get_bank_account_list,add_bank_account)
    atm_card_list = property(get_atm_card_list,add_atm_card_list)

    def create_instance(self, user_data: dict):
        for key, data in user_data.items():
            user = User(key, data[0], data[1])
            self.add_user_list(user)
            self.add_bank_account(SavingAccount(data[1], user, data[3]))
            self.add_atm_card_list(ATMCard(data[1], data[2]))
        return self

class SavingAccount:
       def __init__(self,  bank_id  : str, account_owner: User, balance : int):
              if len(bank_id) == 10:
                     self.__bank_id = bank_id
              self.__account_owner = account_owner
              self.__balance = balance
              self.__transaction_list = []

       def get_balance(self):
              return self.__balance
       
       def get_bank_id(self):
              return self.__bank_id
       
       def get_transaction_list(self):
              return self.__transaction_list
       
       def set_transaction_list(self, transaction):
              self.__transaction_list.append(transaction)
       
       bank_id = property(get_bank_id)
       
       
       def deposit_money(self, money : int, atm_id : str):
              self.__balance += money
              #if atm_id != None : self.__transaction_list.append("D-ATM:" + str(atm_id) + "-" + str(money) + "-" + str(self.get_balance()))
              if atm_id != None : self.__transaction_list.append(Transaction("D", str(money), datetime.datetime.now() , str(atm_id)))
              #   def __init__(self, type_of_service: str, amount: int, time, atm_id : str, transfer_account):
       def withdraw_money(self, money : int, atm_id : str):
              self.__balance -= money
              if atm_id != None : self.__transaction_list.append(Transaction("W", str(money), datetime.datetime.now() , str(atm_id)))

# class FixedDepositAccount(SavingAccount):
#        def __init__(self, bank_id: str, account_owner: User, balance: int):
#               super().__init__(bank_id, account_owner, balance)

class ATMCard:
       yearly_fee = 150
       daily_withdraw_limit = 40000

       def __init__(self,bank_id: str, pin_number: str):
              self.__bank_id = bank_id
              if len(pin_number) == 5:
                self.__pin_number = pin_number
       
       def get_bank_id(self):
              return self.__bank_id

       bank_id = property(get_bank_id)

class ATMBox:
       def __init__(self, atm_id: str, balance_in_box: int = 1000000):
              if len(atm_id) == 4:
                self.__atm_id = atm_id
              self.__balance_in_box = balance_in_box
       def get_atm_id(self):
              return self.__atm_id

       atm_id = property(get_atm_id)

       def insert_card(self,bank : Bank ,atm_card: int):
                for card in bank.atm_card_list:
                         if card.bank_id == atm_card.bank_id:
                                return card
                return "Error"
        
       def deposit_money(self, account : SavingAccount, money : int):
              if money > 0:
                     self.__balance_in_box += money
                     account.deposit_money(money, self.__atm_id)
              else:
                     return "Error"
        
       def withdraw_money(self, account : SavingAccount, money : int):
             if money > 0 and money <= account.get_balance() and money <= self.__balance_in_box:
                     self.__balance_in_box -= money
                     account.withdraw_money(money, self.__atm_id)
             else:
                     return "Error"
             
       def tranfer_money(self , account : SavingAccount, account_to : SavingAccount, money : int):
              if money > 0 and money <= account.get_balance():
                     account.withdraw_money(money, None)
                     account_to.deposit_money(money, None)
                     account.set_transaction_list(Transaction("T", str(money), datetime.datetime.now() , str(self.__atm_id), {account.bank_id, account_to.bank_id}))
                     account_to.set_transaction_list(Transaction("T", str(money), datetime.datetime.now() , str(self.__atm_id), {account.bank_id, account_to.bank_id}))
                     return "Success"
              else:
                     return "Error"

class Transaction:
      def __init__(self, type_of_service: str, amount: int, time, atm_id : str, transfer_account : tuple = None):
             self.__type_of_service = type_of_service
             self.__amount = amount
             self.__time = time
             self.__atm_id = atm_id
             self.__transfer_account = transfer_account

      def get_type_of_service(self):
              return self.__type_of_service
      
      def get_amount(self):
              return self.__amount
      
      def get_time(self):
              return self.__time
      
      def get_atm_id(self):
              return self.__atm_id
      
      def get_transfer_account(self):
              return self.__transfer_account
# class DebitCard(ATMCard):
#        yearly_fee = 150
#        daily_withdraw_limit = 40000

#        def __init__(self, bank_id: str, pin_number: str):
#               super().__init__(bank_id, pin_number)       

#        def get_bank_id(self):
#               return super().get_bank_id()
             
##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user ={'1-1101-12345-12-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','12346',1000]}

atm ={'1001':1000000,'1002':200000}

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

Bank1 = Bank()
Bank1.create_instance(user)

atm_box1 = ATMBox("1001",atm['1001'])
atm_box2 = ATMBox("1002",atm['1002'])

# debit_card1 = DebitCard(Bank1.user_list[0].bank_id,'12367')
# debit_card2 = DebitCard(Bank1.user_list[1].bank_id,'12368')

# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM 

# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0

#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
       
# # #TODO 6 : method ซื้อของโดยใช้ Debit Card
# def purchase_product(debit_card : DebitCard, price : int):
#        for account in Bank1.bank_account_list:
#               if account.bank_id == debit_card.bank_id:
#                      account.add_balance(-price)
#                      account.set_transaction_list("P-"+ str(price) + "-" + str(account.get_balance()))
#                      return "Success"
#        return "Error"

# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print("Test case #1")
print(atm_box1.insert_card(Bank1,Bank1.atm_card_list[0]).bank_id)


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("\nTest case #2")
print("Hermione account before test : " + str(Bank1.bank_account_list[1].get_balance()))
atm_box1.deposit_money(Bank1.bank_account_list[1],1000)
print("Hermione account after test : " + str(Bank1.bank_account_list[1].get_balance()))

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("\nTest case #3")
print(atm_box2.deposit_money(Bank1.bank_account_list[1],-1))

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("\nTest case #4")
print("Hermione account before test : " + str(Bank1.bank_account_list[1].get_balance()))
atm_box2.withdraw_money(Bank1.bank_account_list[1],500)
print("Hermione account after test : " + str(Bank1.bank_account_list[1].get_balance()))


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print("\nTest case #5")
print(atm_box2.withdraw_money(Bank1.bank_account_list[1],2000))

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print("\nTest case #6")
print("Harry account before test : " + str(Bank1.bank_account_list[0].get_balance()))
print("Hermione account before test : " + str(Bank1.bank_account_list[1].get_balance()))
atm_box2.tranfer_money(Bank1.bank_account_list[0],Bank1.bank_account_list[1],10000)
print("Harry account after test : " + str(Bank1.bank_account_list[0].get_balance()))
print("Hermione account after test : " + str(Bank1.bank_account_list[1].get_balance()))


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500

print("\nTest case #7")
print("Hermione transaction : ")
for transaction in Bank1.bank_account_list[1].get_transaction_list():
       print(transaction.get_type_of_service() + "-ATM:" + transaction.get_atm_id() + "-" + transaction.get_amount() + "-" + str(Bank1.bank_account_list[1].get_balance()))
              
       
# #Test case #8 : แสดง purchase product
# print("\nTest case #8")    
# print(purchase_product(debit_card2,0))
