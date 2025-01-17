# BOT assistent
# CLI - Command Line Interface
#              Architecture :
#                   - command`s parser
#                   - decorator --> Rise exceptions
#                   - command`s processing functions (Handlers):
#                           - hello_func                            --- first greeting
#                           - add_func         --> add_record       --- create new contact
#                           - change_func      --> edit_phone       --- change  telephone number for existed contact
#                           - phone_func                            --- show telephone number
#                           - show_func                             --- show all contacts (name telephone number)
#update                     - see_func                              --- show n records (you could use this command several times)
#                           - addnum_func      --> add_phone        --- add aditional tel number for certain contact
#                           - del_func         --> del_phone        --- del tel number for certain contact
#                           - birth_func                            --- add date of birthday in data format
#                           - nextbirth_func   --> days_to_birthday --- show how many days left up to next birthday
#                           - help_func                             --- bot show commands explanations
#                           - save_func                             --- save data base in file: name (without extention) 
#                           - load_func                                       --- load data base from file: name (without extention)
#                           - lookup_func                                     --- find text in records (no difference which case of characters)
#                           - good_buy_func                                   --- bot stops work and messege "Good bye!" 
#new_func                   - del_record_hand     --> del_record              --- delete record from AddressBook 
#new_func                   - add_email_head      --> add_email               --- add email to record (with regex check)
#new_func                   - add_notes_head      --> add_notes               --- add notes to record  
#new_func                   - add_adress_head     --> add_adress              --- add adress to record
#new_func                   - find_notes_by_tages_head --> find_notes_by_tages --- looking up notes by tages (#tage#) 
#new_func                   - sort_notes_by_tages_head --> sort_notes_by_tages --- sorting up notes by tages (#tage#)
#new_func                   - sort_files                                       --- sort files in folder
#new_func                   - guess_command                                    --- analizing taping and try to guess command
#new_func                   - birthday_in_days_hand    --> birthday_in_days    --- display list of contacts, who have birthday in x days   
#
#
#                   - request-answear loop

# Input - dict(name: telephone number)
# Requirements:
#              - telephone number format: 0675223345 - 10 digits;
#              - bot undestands commands:
#                          - "hello" - answear: "How can I help you?"
#                          - "add' name telephone number" - save new contact
#                          - "change' name telephone number" - change telephone number for existed contact
#                          - "phone' name" - show telephone number
#                          - "show all" - show all contacts (name telephone number)
#                          - "see' n" - show n records (you could use this command several times)
#                          - "addnum' name telephone number" - add aditional tel number for certain contact
#                          - "del' name telephone number" - del tel number for certain contact
#                          - "addbirth" name birthday - add date of birthday in data format
#                          - "nextbirth" name - show how many days left up to next birthday
#                          - "help" - bot show commands explanations
#                          - "save" name - save data base in file: name (without extention) 
#                          - "load name" - load data base from file: name (without extention) 
#                          - "lookup' text" - find text in records (no difference which case of characters)
#new                       - "delrec' name" - delete record from AddressBook 
#new                       - "addemail' name email" - add email to record
#new                       - "changeemail" name new_email - change all emails on new one 
#new                       - "addnotes' name text" - add notes to record
#new                       - "addadress' name text" - add adress to record
#new                       - "findtag' teg_text" - looking up notes by tages (#tage#)
#new                       - "sortnotes' teg_text" - sorting up notes by tages (#tage#)
#new                       - "sortfiles' folder_path" - sort files in folder
#new                       - "guess'    - switch on/ switch off guess mode ---> analizing taping and try to guess command        
#new                       - "checkbirth' days_number - display list of contacts, who have birthday in x days
#                          - "good bye" or "close" or "exit" - bot stops work and messege "Good bye!"
#
#
# Class_structure:
#                  UserDict Class:
#                         -user has Book of Contacts (AddressBook Class):
#new                              |__> required (Notes Class) - one or more
#  
#                                 |__> records (Record Class): --> dict {Record.name.value: value}
#                                                              --> Name object - separated atribute
#                                                              --> Phone objects - separated atribute
#new                                                           --> Notes objects - separated atribute
#new                                                           --> Email objects - separated atribute
#new                                                           --> Adress objects - separated atribute
#
#                                          |__> fields (Field Class):
#                                                      - required (Name Class) - only one
#                                                      - optional (Phone Class) - one or more
#                                                      - optional (Birthday Class) - only one 
#new                                                   - required (Email Class) - one or more
#new                                                   - required (Adress Class) - only one
#
#
#
#                AdressBook methods:

#                                - add_record --> add Record in self.data
#new_func                        - del_record <-- del_record_hand
#                                - iterator - return --> generator by records -N records for 1 step
#new_func                        - find_notes_by_tages <-- find_notes_by_tages_head - looking up notes by tages (#tage#) in []
#new_func                        - sort_notes_by_tages <-- sort_notes_by_tages_head - sorting up notes by tages (#tage#) in []
#new_func                        - birthday_in_days    <-- birthday_in_days_head - display list of contacts, who have birthday in x days
#new_func                        - add_notes           <-- add_notes_head - add notes to record 
#
#
#                                           Notes methods:
#new_func                                          - change_notes  <-- change_notes_head - change notes in record
#new_func                                          - del_notes     <-- del_notes_head -    delete notes in record 
#
#                                           Record methods: 
#                                                 - add_phone <-- addnum_func - add aditional tel number for certain contact (with regex check)
#                                                 - del_phone <-- del_func - del tel number for certain contact
#                                                 - edit_phone <-- change_func - change telephone number for existed contact
#                                                 - days_to_birthday <-- nextbirth_func - show how many days left up to next birthday
#new_func                                         - add_email <-- add_email_head - add email to record (with regex check)
#new_func                                         - add_adress<-- add_adress_head - add adress to record
#
# 
#                                                  Phone methods:
#                                                         - setter - check tel. num format (7777777777)
#
#                                                  Birthday methods:
#                                                         - setter - check birthday format (28.05.1978)

#
#                                                  Email methods:
#new_func                                                 - change_email <-- change_email_head - change email in record (with regex check)
#
#
#                                                  Adress methods:
#new_func                                                 - change_adress <-- change_adress_head - change adress in record 
#
#



from ast import List
from multiprocessing.sharedctypes import Value
import re
from collections import UserDict
from datetime import datetime
import pickle
from copy import copy, deepcopy


#### GLOBALS

x = 0
page = 1

class AddressBook (UserDict):
        
    def __init__(self):
        UserDict.__init__(self)
        self.notes = Notes()
            
    
    def add_record(self, name, phone):
        
        self.phone = phone        
        Name.value = name
        self.data[name] = Record()

    def iterator(self):
        
        global x
        global page

        while x <= len (self.data):
            
            for key_in, value_in in self.data[list(self.data)[x]].record_dict.items():
                    
                    if value_in:
                        if isinstance(value_in, list):
                            print (f"{key_in} : {', '.join(map(str, value_in))} | ", end = " ")
                        else:
                            print (f"{key_in} : { value_in} | ", end = " ") 

            x += 1
            page += 1
            yield x

    def del_record(self, name):
        del self.data[name]


    def add_notes(self):
        pass
    
        
    def find_notes_by_tages(self):
        pass


    def sort_notes_by_tages(self):
        pass

    
    def birthday_in_days(self):
        pass
                        
class Field:
    pass

class Name (Field):
    
    value = None

class Phone (Field):
    
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value
       
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        
        if re.match(r"^[0-9]{10,10}$", new_value):
                    
            #print ('Number format has been checked successfully!')
            self.__value = new_value

        else:
            print ('Telephone number does not match format!')

class Notes:
    
    def __init__(self) -> None:
        self.value = []
    
    def change_notes(self):
        pass

    def del_notes (self):
        pass


class Email (Field):

    def __init__(self) -> None:
        self.value = None
    
    def change_email(self, name, new_email):
        add_book.data[name].record_dict['Email'].clear()
        add_book.data[name].record_dict['Email'].append(new_email)

   


class Adress (Field):

    def __init__(self) -> None:
        self.value = None
    
    def change_adress(self):
        pass

       
class Birthday (Field):
    
    def __init__(self, value = None) -> None:
        self.__value = None
        self.value = value       

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        
        try:
        
            if re.match(r"\d{2}.\d{2}.\d{4}", new_value):
            
                birthday_data_list  = new_value.split('.')
            
                birthday_datatime = datetime(year=int(birthday_data_list[2]), month=int(birthday_data_list[1]), day=int(birthday_data_list[0])).date()
            
                self.__value = birthday_datatime
                print ('Birthday date has been added successfully!')
       
            else:
                raise BirthdayDoesNotMathFormatError

        except BirthdayDoesNotMathFormatError:

            print("You have to set date in next format: dd.mm.yyyy! ")
            BirthdayDoesNotMathFormatError.status = 1

        except KeyError:
            print("This contact does not exist! First - set up appropriate contact")
            TryAgainError.status = 1

        except ValueError:
            print("You have to set date in next format: 1-31.1-12.0000-9999!")
            TryAgainError.status = 1
        
        

class Record:
    
    def __init__(self) -> None:
        
        self.name = Name()
        self.phone = Phone(add_book.phone)
        self.email = Email()
        self.adress = Adress()
        #self.birthday = Birthday('28.05.1978') ####
        self.record_dict = {
                         'Name': self.name.value,
                         'Phone': [self.phone.value],
                         'Birthday': None,
                         'Email' : None,                            
                         'Adress' : None
                         }
        
    def add_phone (self, name, phone):
        #add_book.data[name].append(phone)
        add_book.data[name].record_dict['Phone'].append(phone)
       
    def del_phone (self, name, phone):
        add_book.data[name].record_dict['Phone'].remove(phone)

    def edit_phone (self, name, new_phone):  
        add_book.data[name].record_dict['Phone'].clear()
        add_book.data[name].record_dict['Phone'].append(new_phone)

    def days_to_birthday (self, name):
        next_year_birthday = datetime(year=datetime.now().year + 1, month=add_book.data[name].record_dict['Birthday'].month, day=add_book.data[name].record_dict['Birthday'].day)
        this_year_birthday = datetime(year=datetime.now().year, month=add_book.data[name].record_dict['Birthday'].month, day=add_book.data[name].record_dict['Birthday'].day)
        if this_year_birthday <= datetime.now():
            difference = next_year_birthday - datetime.now()
        else:
            difference = this_year_birthday - datetime.now()

        print(f'{name} should wait {difference.days} days until next birthday!')


    def add_email(self, name, email):

        if add_book.data[name].record_dict['Email']:
            add_book.data[name].record_dict['Email'].append(email)
        else:
            add_book.data[name].record_dict['Email'] = []
            add_book.data[name].record_dict['Email'].append(email)


    def add_adress(self, name, adress):
        add_book.data[name].record_dict['Adress'] = adress


class TelDoesNotMathFormatError(Exception):
    status = 0

class BirthdayDoesNotMathFormatError(Exception):
    status = 0

class NameDoesNotExistError(Exception):
    status = 0

class TryAgainError(Exception):
    status = 0

def command_parser (command): # command`s parser
    command_id = ''
    name = ''
    phone = ''
       
    parsered_list = command.split (" ")

    if len(parsered_list) == 1:
        command_id = parsered_list[0].lower() # make all letters small
    
    elif len(parsered_list) == 2:
        command_id = parsered_list[0].lower()
        name = parsered_list[1]
    elif len(parsered_list) == 3:
        command_id = parsered_list[0].lower()
        name = parsered_list[1]
        phone = parsered_list[2]
    elif len(parsered_list) > 3:
        command_id = parsered_list[0].lower()
        name = parsered_list[1]
        slice_parser = parsered_list[2:]
        phone = ' '.join(map(str, slice_parser))
        # phone = parsered_list[2]
    else:
        print ("Number of arguments do not fit to reqirements. Please try again!")
        
    return command_id, name, phone

### Decorator
def input_error(func): # decorator
    
    def inner(*args, **kwargs):

        func(*args, **kwargs) 

        if TelDoesNotMathFormatError.status == 1: # added functional zone
            print('Format does not match')
            TelDoesNotMathFormatError.status = 0
        elif NameDoesNotExistError.status == 1:
            print('Enter user name please')
            NameDoesNotExistError.status = 0
        elif TryAgainError.status == 1:
            print('Please, Try again!')
            TryAgainError.status = 0
        elif BirthdayDoesNotMathFormatError.status == 1:
            print('Please, Try again!')
            BirthdayDoesNotMathFormatError.status = 0

    return inner

### Handlers:
def hello_func ():
    print('How can I help you?')

@input_error
def add_func (name, phone):   #1&2

    try:
        if re.match(r"^[0-9]{10,10}$", phone):
            
            add_book.add_record(name, phone) ###2

            print ('Information has been added successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1

@input_error
def change_func (name, phone):    #1&2

    try:
        if name in add_book.data:
            if re.match(r"^[0-9]{10,10}$", phone):
                
                Record().edit_phone(name, phone) ### 2

                print ('Phone number has been changed successfully!')
            else:
                raise TelDoesNotMathFormatError
        
        else:
            raise NameDoesNotExistError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1 

    except NameDoesNotExistError:

        print('Name does not exist')
        NameDoesNotExistError.status = 1
    
@input_error
def phone_func (name):           #1&2

    try:

        if name in add_book.data:   ### 2

            mystring = ', '.join(map(str, add_book.data[name].record_dict['Phone']))

            print(f'Phone number assigned for requested name is: {mystring}')

        else:
            raise NameDoesNotExistError

    except NameDoesNotExistError:

        print('Name does not exist.') #  - decorator
        NameDoesNotExistError.status = 1

def show_func ():
    global x
    global page

    if len(add_book.data) == 0:
        print('Data Base is empty yet. Please add someone!')
    else:
        print('Data Base contains next contacts:')

        x = 0
        page = 1
 
        for key, value in add_book.data.items():               

            for key_in, value_in in value.record_dict.items():
                
                if value_in:
                    if isinstance(value_in, list):
                        print (f"{key_in} : {', '.join(map(str, value_in))} | ", end = " ")
                    else:
                        print (f"{key_in} : { value_in} | ", end = " ")
            print('')
     

@input_error
def see_func (n):

    try:
        global x
        global page
        if len (add_book.data) - (x+1) >= 0:
            print(f'Page #: {page}. ') ####
        else:
            print('Stop listing!')
        record_generator = add_book.iterator()
        for x in range (x, x+int(n)):
            next(record_generator) 
            
    except IndexError:

        print(f"Sorry, no more records! Use 'show all' command!")
                
@input_error
def addnum_func (name, phone):   #1&2

    try:
        if re.match(r"^[0-9]{10,10}$", phone):
            
            Record().add_phone(name, phone) ###2

            print ('Information has been added successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1

@input_error
def del_func (name, phone):   #1&2

    try:
        if re.match(r"^[0-9]{10,10}$", phone):
            
            Record().del_phone(name, phone) ###2

            print ('Telephone number has been deleted successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1

    except ValueError:
        print("Number assigned for deletion does not exist!")
        TryAgainError.status = 1

@input_error
def birth_func (name, birthday):   #1&2
                
    add_book.data[name].record_dict['Birthday'] = Birthday(birthday).value
        
@input_error
def nextbirth_func (name):   #1&2

    try:
                   
        Record().days_to_birthday(name) ###2
         
    except KeyError:
        print("This contact does not exist! First - set up appropriate contact")
        TryAgainError.status = 1

    except AttributeError:
        print("You have to add your birthday before this operation!")
        TryAgainError.status = 1


def help_func ():
    print(' Bot undestands next commands:\n'
'- "hello" - answear: "How can I help you?"\n'
'- "add" name telephone number" - save new contact\n'
'- "change" name telephone number" - save new telephone number for existed contact\n'
'- "phone" name" - show telephone number\n'
'- "show all" - show all contacts (name telephone number)\n'
'- "see" n" - show n records (you could use this command several times)\n'
'- "addnum" name telephone number" - add aditional tel number for certain contact\n'
'- "del" name telephone number" - del tel number for certain contact\n'
'- "addbirth" name birthday - add date of birthday in data format\n'
'- "nextbirth" name - show how many days left up to next birthday\n'
'- "help" - bot show commands explanations\n'
'- "save" name - save data base in file: name (without extention) \n'
'- "load name" - load data base from file (without extention) \n'
'- "lookup" text" - find text in records (no difference which case of characters)\n'
'- "delrec" name" - delete record from AddressBook \n'
'- "addemail" name email" - add email to record \n'
'- "changeemail" name new_email" - change all emails on new one \n' 
'- "addnotes" name text" - add notes to record \n'
'- "addadress" name text" - add adress to record \n'
'- "findtag" teg_text" - looking up notes by tages \n'
'- "sortnotes" teg_text" - sorting up notes by tages \n'
'- "guess" - switch on/ switch off guess mode ---> analizing taping and try to guess command \n'
'- "checkbirth" days_number - display list of contacts, who have birthday in x days \n'
'- "good bye" or "close" or "exit" - bot stops work and messege "Good bye!" ')
    
def save_func (name):

    with open(name + '.obj', 'wb') as report:
        pickle.dump(add_book.data, report)
           
    with open(name + '.txt', 'w') as report:
           
        for key, value in add_book.data.items():               

            for key_in, value_in in value.record_dict.items():
                
                if value_in:
                    if isinstance(value_in, list):
                        report.write (f"{key_in} : {', '.join(map(str, value_in))} | ")
                    else:
                        report.write (f"{key_in} : { value_in} | ")
            report.write('\n')
        
        
        
        
        """ for key, value in add_book.data.items():                   
            mystring = ', '.join(map(str, value.record_dict['Phone']))
            if value.record_dict['Birthday']:

                report.write(f"Name : {key} | Telephone numbers: {mystring} | Birthday: {value.record_dict['Birthday'].strftime('%A %d %B %Y')}\n")
            else:
                
                report.write(f"Name : {key} | Telephone numbers: {mystring}\n ")  """       
        
    print ('Data base has been saved successfully!')

def load_func (name):
    try:
        add_book.add_record('XXX', '0000000000')
        with open(name + '.obj', 'rb') as report:
            add_book.data = pickle.load(report)

            print ('Data base has been loaded successfully!')

    except FileNotFoundError:
        print("File not found! Please, make sure file is exist or name was written correctly!")

def lookup_func(text):
    if len(add_book.data) == 0:
        print('Data Base is empty yet. Please add someone!')
    else:
        flag_found = 0
        for key, value in add_book.data.items():                   
            dict_for_lookup = deepcopy(value.record_dict)
            if value.record_dict['Birthday']:
                datetimestring =  copy(value.record_dict['Birthday'])
                dict_for_lookup['Birthday']  = datetimestring.strftime('%A %d %B %Y')
            else:
                dict_for_lookup['Birthday'] = ''
            
            dict_for_lookup['Phone'] = list_string(value.record_dict['Phone'])
            
            dict_for_lookup['Email'] = list_string(value.record_dict['Email'])
            dict_for_lookup['Adress'] = list_string(value.record_dict['Adress'])
            

            for key_in, value_in in dict_for_lookup.items():
                if  value_in.lower().find(text.lower()) >= 0:
                    print(f'Looked up text was found in "{key}" Record, in "{key_in}" Field. in next text: "{value_in}" ')
                    flag_found += 1


        #### Add lookup by Notes            

        if flag_found != 0:
            print(f'Summary: There were found {flag_found} results')
        else:
            print('No information was found')
        
@input_error
def del_record_hand(name):   #### ---- !!!!!
    try:

        if name in add_book.data:   

            add_book.del_record(name)

            print(f'Record :{name} has been deleted successfully!')

        else:
            raise NameDoesNotExistError

    except NameDoesNotExistError:

        print('Record does not exist.') #  
        NameDoesNotExistError.status = 1

@input_error
def add_email_head(name, email):

    try:
        if re.match(r"[a-z0-9]+@[a-z]+\.[a-z]{2,3}", email):
            
            Record().add_email(name, email) ###2

            print ('Email has been added successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Email does not match format - should be 1@1.1")
        TelDoesNotMathFormatError.status = 1

@input_error
def change_email_head(name, email):

    try:
        if re.match(r"[a-z0-9]+@[a-z]+\.[a-z]{2,3}", email):
            
            Email().change_email(name, email) ###2

            print ('Email has been changed successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Email does not match format - should be 1@1.1")
        TelDoesNotMathFormatError.status = 1



@input_error
def add_notes_head():
    pass

@input_error
def add_adress_head(name, adress):
    try:
        Record().add_adress(name, adress) ###2
        print ('Adress has been added successfully!')   

    except:

        print("Adress format problem")
        


@input_error
def find_notes_by_tages_head():
    pass

@input_error
def sort_notes_by_tages_head():
    pass

@input_error
def sort_files():
    pass

def guess_command():
    pass

@input_error
def birthday_in_days_hand():
    pass


def list_string(list): ### servise function for lookup function
    if list is List: 
        return ', '.join(map(str, list))
    else:
        return str(list)


def good_buy_func ():
    print('Good bye!')
    return 'stop'

### MAIN BODY FUNCTION
def main():

    global add_book
    add_book = AddressBook()


    commands_dict = {'hello': hello_func, 'add': add_func, 'change': change_func,\
         'phone': phone_func, 'show': show_func, 'good': good_buy_func,\
         'close': good_buy_func, 'exit': good_buy_func, 'addnum': addnum_func, 'del': del_func,\
         'addbirth': birth_func, 'nextbirth': nextbirth_func, 'see': see_func, 'help': help_func,\
          'save': save_func, 'load': load_func, 'lookup': lookup_func,\
          
          'delrec': del_record_hand, 'addemail': add_email_head, 'addnotes': add_notes_head,\
           'addadress': add_adress_head, 'findtag': find_notes_by_tages_head, 'sortnotes': sort_notes_by_tages_head, 
           'sortfiles': sort_files, 'guess': guess_command, 'checkbirth': birthday_in_days_hand,\
            'changeemail': change_email_head  
                     }
    
    stop_flag = ''
      
    print ("Bot has been started!\nFor additional information enter 'help'")
    while True:
        try:
            
            print('')

            """ if len(add_book) == 0: # Print_to_check_addressbook
                print(add_book)
            else: 
                for key, value in add_book.items():
                    print(f'Name: {key}, Record: {value.record_dict}') """
            
            command = input("Please, put you command in Command line! (from 1 to 3 arguments): ")   
            command_id, name, phone = command_parser (command) # passing vars to another func

            for key, value in commands_dict.items():
                if command_id == key and name == '' and phone == '':
                    res = value()
                    stop_flag = res

                elif command_id == key and name.lower() == 'bay' and phone == '':
                    res = value()
                    stop_flag = res

                elif command_id == key and name.lower() == 'all' and phone == '':
                    res = value()
                        
                elif command_id == key and name != '' and phone == '':
                    res = value(name)

                elif command_id == key and name != '' and phone != '':
                    res = value(name, phone)

            if command_id not in commands_dict:
                print('I do not know this command!')
                                               
            if stop_flag == 'stop':
                break

        except TypeError:
            print('Unsuccessful operation. Please, try again')
        
if __name__ == '__main__':
    
    main()