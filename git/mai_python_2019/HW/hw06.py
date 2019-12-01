import sys
from datetime import datetime
import argparse
import random
import logging



def log(func):
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler("%s.log" % name)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("Вызов функции: %s" % name)
        # info("Вызов функции: %s" % name)
        result = func(*args, **kwargs)
        # logger.info("Результат: %s" % result)
        logger.info("Результат: %s" % result)
        return func

    return wrap_log



class Parser():
    __parser = None
    __args = None

    def __init__(self, sysargs):
        self.__parser = self.__create_parser()
        self.__args = vars(self.__parser.parse_args(sysargs))
        print(f"Аргументы командной строки внутри класса: {self.__args}")

    def __create_parser(self):
        parser = argparse.ArgumentParser(description="main.py -digits [--fullmatch_sign --match_sign")
        parser.add_argument("-digits", type=int, default=4, help="")
        parser.add_argument("--fullmatch_sign", type=str, default="B", help="")
        parser.add_argument("--match_sign", type=str, default="K", help="")

        return parser

    def show_args(self):
        print(self.__args)


def main():
    #class_parser = Parser(sys.argv[1:])
    #print(f"Аргументы командной строки вне класса: {sys.argv}")
    #print(f"Из командной строки мы получили следующие аргументы: {class_parser.show_args()}")
    #class_game1 = Game(3, "B", "K")
    #class_game2 = Game(4, "B", "S")
    #class_game1.show_parameters()
    #class_game2.show_parameters()
    #print(f"А эта фукция вернет нам количество цифр, умноженное на три: {class_game1.game_count_triplet()}")
    Round()
# функция может быть создана вне класса и добавлена в него
def count_triplet(self):
    return self.digits_public*3

class Gamer():
    __history = None
    __counter = 0
    __name=""
    
    def __init__(self):
        self.__counter = 0
        self.__history = dict()

    def next_move(self):
        user_number = self.__get_user_number()
        self.__counter += 1
        self.__history[self.__counter] = {"user_number": user_number,
                    "match_result":""}
        return user_number

    def set_result(self, result):
        self.__history[self.__counter]["match_result": result]

    def __get_user_number(self):
        user_number =  input("Введите число: ")
        if user_number.isdecimal():
            return user_number
        else:
            print("Вы ввели не число")
            return "0000"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name=value
  
class Game():
    __fullmatch = ""
    __match = ""
    __digits = 4
    digits_public = 4
    __number = "0000"
    
    @property
    def number(self):
        return self.__number
    
    @property
    def match(self):
        return self.__match
    
    @match.setter
    def match(self, value):
        self.__match = value
    
    @property
    def fullmatch(self):
        return self.__fullmatch
    
    @fullmatch.setter
    def fullmatch(self, value):
        self.__fullmatch = value 
    
    game_count_triplet = count_triplet

    def __rand_generator(self, digits):
        random.seed()
        s = ""
        for r in range(digits+1):
            s += str(random.randrange(10))
        return s

    def __init__(self, digits, fullmatch, match):
        self.fullmatch = fullmatch
        self.match = match
        self.__digits = digits
        self.digits_public = digits
        self.__number = self.__rand_generator(digits)

    def show_parameters(self):
        print(f"{self.__class__} Количество цифр в числе: {self.__digits}, знак полного совпадения: {self.__fullmatch}, знак частичного совпадения: {self.__match}, сгенерированное число: {self.__number}")
    

        
class Round():
    __game = None
    __gamer = None
    __fullmatch = ""
    __match = ""
    
    @property
    def match(self):
        return self.__game.match
    
       
    @property
    def fullmatch(self):
        return self.__game.fullmatch
    
       
    
    def __init__(self):
        self.__game = Game(3, "B", "K")
        self.__gamer = Gamer()
        self.worker()
        #self.fullmatch = self.__game.fullmatch
        #self.match = self.__game.match        
                
    def __compare(self, number, user_number):
        
        n1 = list(number)
        n2 = list(user_number)
        if len(n1) != len(n2):
            print(f"вы не угадали с количеством цифр в числе, в загаданном числе их {len(n1)}")
            return False
        coincidence = 0
        c=0
        out=""
        while c<len(n1) and c<len(n2):
            if n1[c] == n2[c]:
                out+=self.fullmatch
                coincidence += 1
            else:
                out+=self.match
            c+=1
        print(out)
        if len(n1) == len(n2) and coincidence==len(n1):
            #print(self.fullmatch)
            return True
        elif coincidence > 0:
            #print(f"{self.match}, угадал {coincidence} символов")
            return False
        else:
            #print(f"{self.match},совсем дурак чёли?")
            return False
    @log
    def worker(self):
        n1 = self.__game.number
        print(n1)
        while True:
            n2 = self.__gamer.next_move()
            won = self.__compare(n1, n2)
            if won:
                print("Game over. You win. Красава")
                break
            #else:
                #print(self.match)


if __name__ == "__main__":
    main()