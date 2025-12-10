

class Valid:
    def check_10(self, number: str):
       if len(number) == 10:# בדיקה שיש 10 ספרות
          return True
       print('most by 10 digit')
       return False
    

    def in_1023(self,number):
        try:
            if int(number) > 1023 or int(number) < 0:
                print('valid number')
                return False
            else:
                return True
        except TypeError:
            print('valid number')
            return False 
           

                       
                   


