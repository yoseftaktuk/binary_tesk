from core.utils import Utils, File_maneger
from core.io import Io
from core.valid import Valid

def run():
    io = Io()
    utils = Utils()
    valid = Valid()
    file_maneger = File_maneger()
    flag = True
    while flag:
        binary_input = io.get_input_binary()
        if valid.check_10(binary_input) and utils.validate_mask(binary_input):# בדיקה שיש 10 מספרים ושהם בסדר הנכון
            while flag:
                number_input = io.get_input_number()
                if valid.in_1023(number_input):# בדיקה שהמספר גדול מ0 וקטן או שווה ל1023
                    data = utils.split_by_mask(binary_musk=binary_input, number=number_input)
                    data = {'Binary Mask Input': binary_input,
                            'Decimal Input': number_input,
                            'Input in Binary': utils.decimal_to_binary(number=number_input),
                            'Left Part (Binary)':data['left'],
                            'Right Part (Binary)': data['right'],
                            'Result in Decimal':[utils.binary_to_decimal(data['left']), utils.binary_to_decimal(data['right'])]}
                    file_maneger.seve_data(data=data)#כתיבה לקובץ
                    print(data)
                    user_input = input('Do you want to enter another number(y/n)?')
                    if user_input == 'y':
                        break
                    else:
                        flag = False
                else:
                    continue
        else:
            continue            
            
if __name__ == '__main__':
    run()
    