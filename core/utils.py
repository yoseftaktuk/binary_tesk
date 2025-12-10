import json

class Utils:
    def binary_to_decimal(self, number: str):
        power = len(number) - 1
        result = 0
        for num in number:
            if num == '1':
                result += 2 ** power
                power -= 1
            else:
                power -= 1
                continue    
        return result    


    def decimal_to_binary(self, number: int):
        binary = ""
        for _ in range(10):
            binary += str(number % 2)
            number = number // 2
        return binary[::-1]

    def validate_mask(self, number):
        flags = True
        for num in number:
          if flags:
                if num == '1':# אם זה 1 חוזר לאתחלה
                    continue
                else:# אחרת משנה את הדגל ובסיבוב הבא ילך לelse
                    flags = False
          else:
              if num == '0':
                  continue
              else:#אם יש 1 מחזיר False
                  print('valid binary number')
                  return False
        return True
    

    def split_by_mask(self, binary_musk: str, number: int):
        binary = self.decimal_to_binary(number)
        counter = 0
        for num in binary_musk:
            if num == '1':
                counter += 1
                continue
            else:
                break
        # חילוק המספר לפי המאסק    
        left = binary[0:counter]
        right = binary[counter:]
        return {'left': left,
                'right': right}
        


class File_maneger:
    def seve_data(self, data):
        file_path = 'C:\\Users\\Yosef\\vsc_project\\binary_tesk\\bit_mask_result_209265933.txt'
        with open(file_path,'w',encoding="utf-8") as f:
            json.dump(data,f)    

