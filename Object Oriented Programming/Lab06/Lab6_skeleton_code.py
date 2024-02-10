# Class Code
from datetime import datetime

class Bank_Headquarter:
    def __init__(self):
        self.__bank_user = []
        self.__bank_account = []
        self.__bank_atm_card = []
        self.__bank_atm_machine = []
        
    def add_user(self, user):
        self.__bank_user.append(user)
    def add_account(self, account):
        self.__bank_account.append(account)
    def add_atm_card(self, atm_card):
        self.__bank_atm_card.append(atm_card)
    def add_atm_machine(self, atm_machine):
        self.__bank_atm_machine.append(atm_machine)
        
    def get_user(self):
        return self.__bank_user
    def get_account(self):
        return self.__bank_account
    def get_atm_card(self):
        return self.__bank_atm_card
    def get_atm_machine(self):
        return self.__bank_atm_machine
    
    def set_bank(self, user_data):
        for key, value in user_data.items():
            user_detail = Bank_User(key, value[0], value[1])
            self.add_user(user_detail)
            self.add_account(Bank_Account(value[1], user_detail, value[3]))
            self.add_atm_card(ATM_Card(value[1], value[2]))
        return self
        
class Bank_User:
    def __init__(self, user_id, user_name, account_id):
        self.__user_id = user_id if len(user_id.split('-')) == 13 else None
        self.__user_name = user_name
        self.__user_accounts = []
        if len(account_id) == 10:
            self.__user_accounts.append(account_id)
            
    def add_account(self, account_id):
        if len(account_id) == 10:
            self.__user_accounts.append(account_id)
            
    def get_name(self):
        return self.__user_name
            
class Bank_Account:
    def __init__(self, account_id, owner_account, balance):
        self.__account_id = account_id if len(account_id) == 10 else None
        self.__owner_account = owner_account
        self.__balance = balance if balance > 0 else 0
        self.__transaction_list = []
    def set_balance(self, balance):
        self.__balance = balance
        
    def add_transaction(self, transaction):
        self.__transaction_list.append(transaction)
        
    def get_owner_account(self):
        return self.__owner_account
    def get_account_id(self):
        return self.__account_id
    def get_balance(self):
        return self.__balance
    def get_transaction_list(self):
        return self.__transaction_list
    
    def account_deposit(self, atm_machine, account, amount):
        if amount < 0:
            return 'Error-amount false'
        for atm_box in bank.get_atm_machine():
            if atm_box == atm_machine:
                for acc in bank.get_account():
                    if acc == account:
                        box_deposit = []
                        temp_user = [user for user in bank.get_user() if acc.get_owner_account() == user]
                        box_deposit.append(f'{temp_user[0].get_name()} account before test (deposit) : {acc.get_balance()}')
                        acc.set_balance(acc.get_balance() + amount)
                        box_deposit.append(f'{temp_user[0].get_name()} account after test (deposit) : {acc.get_balance()}')
                        atm_box.machine_has_been_deposited(atm_machine, amount)
                        transaction = Transaction('deposit', atm_machine.get_atm_id(), amount, acc.get_balance())
                        acc.add_transaction(transaction)
                        return box_deposit
                return 'Error-from searching Account'
        return 'Error-from searching ATM machine'
            
    def account_withdraw(self, atm_machine, account, amount):
        if amount < 0:
            return 'Error-amount false'
        for atm_box in bank.get_atm_machine():
            if atm_box == atm_machine:
                for acc in bank.get_account():
                    if acc == account:
                        if (acc.get_balance() - amount) < 0:
                            return 'Error-balance not enough'
                        box_withdraw = []
                        temp_user = [user for user in bank.get_user() if acc.get_owner_account() == user]
                        box_withdraw.append(f'{temp_user[0].get_name()} account before test (withdraw) : {acc.get_balance()}')
                        acc.set_balance(acc.get_balance() - amount)
                        box_withdraw.append(f'{temp_user[0].get_name()} account after test (withdraw) : {acc.get_balance()}')
                        atm_box.machine_has_been_withdrawn(atm_machine, amount)
                        transaction = Transaction('withdraw', atm_machine.get_atm_id(), amount, acc.get_balance())
                        acc.add_transaction(transaction)
                        return box_withdraw
                return 'Error-from searching Account'
        return 'Error-from searching ATM machine'
    
    def account_transfer(self, atm_machine, transferer, transferee, amount):
        if amount < 0:
            return 'Error-amount false'
        for atm_box in bank.get_atm_machine():
            if atm_box == atm_machine:
                for acc_transferer in bank.get_account():
                    if acc_transferer == transferer:
                        if (acc_transferer.get_balance() - amount) < 0:
                            return 'Error-balance not enough'
                        box_transfer = []
                        temp_user = [user for user in bank.get_user() if acc_transferer.get_owner_account() == user]
                        box_transfer.append(f'{temp_user[0].get_name()} account before test (transfer) : {acc_transferer.get_balance()}')
                        acc_transferer.set_balance(acc_transferer.get_balance() - amount)
                        box_transfer.append(f'{temp_user[0].get_name()} account after test (transfer) : {acc_transferer.get_balance()}')
                        transaction = Transaction('transferer', atm_machine.get_atm_id(), amount, acc_transferer.get_balance())
                        acc_transferer.add_transaction(transaction)
                for acc_transferee in bank.get_account():
                    if acc_transferee == transferee:
                        box_transfee = []
                        temp_user = [user for user in bank.get_user() if acc_transferee.get_owner_account() == user]
                        box_transfee.append(f'{temp_user[0].get_name()} account before test (transfer) : {acc_transferee.get_balance()}')
                        acc_transferee.set_balance(acc_transferee.get_balance() + amount)
                        box_transfee.append(f'{temp_user[0].get_name()} account after test (transfer) : {acc_transferee.get_balance()}')
                        transaction = Transaction('transferee', atm_machine.get_atm_id(), amount, acc_transferee.get_balance())
                        acc_transferee.add_transaction(transaction)
                        return [box_transfer, box_transfee]
                return 'Error-from searching Account'
        return 'Error-from searching ATM machine'
    
    def transaction_list_performance(self, account):
        transaction_list = []
        for transaction in account.get_transaction_list():
            name = account.get_owner_account().get_name()
            atm_id = transaction.get_transaction_atm_id()
            mark = ''
            if transaction.get_transaction_type() == 'deposit':
                type_of_transaction = 'D'
            if transaction.get_transaction_type() == 'withdraw':
                type_of_transaction = 'W'
            if transaction.get_transaction_type() == 'transferer' or transaction.get_transaction_type() == 'transferee':
                type_of_transaction = 'T'
                if transaction.get_transaction_type() == 'transferer':
                    mark = '-'
                if transaction.get_transaction_type() == 'transferee':
                    mark = '+'
            before_amount = transaction.get_transaction_before_amount()
            after_amount = transaction.get_transaction_after_amount()
            time = transaction.get_transaction_time()
            transaction_list.append(f'{name} transaction : {type_of_transaction}-ATM:{atm_id}-{mark}{before_amount}-{after_amount} time:{time}')
        return transaction_list
        
class ATM_Card:
    def __init__(self, account_id, pin_number):
        self.__account_id = account_id
        self.__pin_number = pin_number if len(pin_number) == 5 else None
        
    def get_account_id(self):
        return self.__account_id
    def get_pin_number(self):
        return self.__pin_number
        
class ATM_Machine:
    def __init__(self, atm_id, atm_bucket):
        self.__atm_id = atm_id
        self.__atm_bucket = atm_bucket
    
    def set_atm_bucket(self, atm_bucket):
        self.__atm_bucket = atm_bucket
        
    def get_atm_id(self):
        return self.__atm_id
    def get_atm_bucket(self):
        return self.__atm_bucket
    
    def insert_atm_card_from_machine(self, account_id: str, pin_number: str):
        for atm_card in bank.get_atm_card():
            if atm_card.get_account_id() == account_id and atm_card.get_pin_number() == pin_number:
                result = [account for account in bank.get_account() if account.get_account_id() == account_id]
                return f"{account_id}, {pin_number}, Success".format(account_id, pin_number)
        return None
    
    def machine_has_been_deposited(self, atm_machine, amount):
        bucket_temp = atm_machine.get_atm_bucket()
        bucket_temp += amount
        atm_machine.set_atm_bucket(bucket_temp)
        
    def machine_has_been_withdrawn(self, atm_machine, amount):
        bucket_temp = atm_machine.get_atm_bucket()
        bucket_temp -= amount
        atm_machine.set_atm_bucket(bucket_temp)
    
class Transaction:
    def __init__(self, transaction_type, transaction_atm_id, transaction_before_amount, transaction_after_amount):
        self.__transaction_type = transaction_type
        self.__transaction_atm_id = transaction_atm_id
        self.__transaction_before_amount = transaction_before_amount
        self.__transaction_after_amount = transaction_after_amount
        self.__transaction_time = datetime.now() 
        
    def get_transaction_type(self):
        return self.__transaction_type
    def get_transaction_atm_id(self):
        return self.__transaction_atm_id
    def get_transaction_before_amount(self):
        return self.__transaction_before_amount
    def get_transaction_after_amount(self):
        return self.__transaction_after_amount
    def get_transaction_time(self):
        return self.__transaction_time
    
##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user = {'1-1101-12345-38-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-39-0':['Hermione Jean Granger','0987654321','12346',1000]}
atm = {'1001':1000000, '1002':200000}

fake_user = {'1-9999-12345-38-0':['Ronton','5050505050','55555',59999], 
             '1-9999-12345-39-0':['Snakey','3636363636','99999',25000]}
fake_atm = {'1003':300000, '1004':400000}

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

bank = Bank_Headquarter()
bank.set_bank(user)
atm_01 = ATM_Machine('1001', atm['1001'])
atm_02 = ATM_Machine('1002', atm['1002'])
bank.add_atm_machine(atm_01)
bank.add_atm_machine(atm_02)

fake_bank = Bank_Headquarter()
fake_bank.set_bank(fake_user)
fake_atm_01 = ATM_Machine('1003', fake_atm['1003'])
fake_atm_02 = ATM_Machine('1004', fake_atm['1004'])
fake_bank.add_atm_machine(fake_atm_01)
fake_bank.add_atm_machine(fake_atm_02)

# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM

# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0

# TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

# TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success

print('Test case #1 --------------------------------------------------')
print(atm_01.insert_atm_card_from_machine('1234567890', '12345'))

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000

print('Test case #2 --------------------------------------------------')
# print(bank.get_account()[0].account_deposit(atm_02, bank.get_account()[1], 1000))
for item in bank.get_account()[0].account_deposit(atm_02, bank.get_account()[1], 1000):
    print(item)

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error

print('Test case #3 --------------------------------------------------')
print(bank.get_account()[0].account_deposit(atm_02, bank.get_account()[1], -1000))
print(bank.get_atm_machine()[1].get_atm_bucket())

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500

print('Test case #4 --------------------------------------------------')
# print(bank.get_account()[0].account_withdraw(atm_02, bank.get_account()[1], 500))
for item in bank.get_account()[0].account_withdraw(atm_02, bank.get_account()[1], 500):
    print(item)

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error

print('Test case #5 --------------------------------------------------')
print(bank.get_account()[0].account_withdraw(atm_02, bank.get_account()[1], 2000))
print(bank.get_atm_machine()[1].get_atm_bucket())

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500

print('Test case #6 --------------------------------------------------')
# print(bank.get_account()[0].account_transfer(atm_02, bank.get_account()[0], bank.get_account()[1], 10000))
for item in bank.get_account()[0].account_transfer(atm_02, bank.get_account()[0], bank.get_account()[1], 10000):
    for i in item:
        print(i)

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500

print('Test case #7 --------------------------------------------------')
# bank.get_account()[1].transaction_list_performance(bank.get_account()[1])
for item in bank.get_account()[1].transaction_list_performance(bank.get_account()[1]):
    print(item)
