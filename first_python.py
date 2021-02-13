import os

def main():
    os.system("cls")
    print("-----------------------------------")
    print("Program Python Saya")
    print("-----------------------------------")
    print("1. Program Pertama Saya")
    print("2. Kalkulator")
    print("-----------------------------------")
    print("00. Keluar")
    print("-----------------------------------")
    program = input("Pilih salah satu program diatas: ")
    if program == "1":
        first_app()
    elif program == "2":
        calculator_app()
    elif program == "00":
        os.system("cls")
        os.system("pause")
        os.system("exit")
    else:
        os.system("cls")
        print("-----------------------------------")
        print("Nomor yang anda input salah!")
        print("-----------------------------------")
        os.system("pause")
        main()

def first_app():
    os.system("cls")
    print("-----------------------------------")
    print("Program Python Pertama Saya")
    print("-----------------------------------")
    print("Hello World")
    print("-----------------------------------")
    print("98. Kembali")
    print("99. Keluar")
    print("-----------------------------------")
    program = input("Pilih salah satu program diatas: ")
    if program == "98":
        main()
    elif program == "99":
        os.system("cls")
        os.system("pause")
    else:
        os.system("cls")
        print("-----------------------------------")
        print("Nomor yang anda input salah!")
        print("-----------------------------------")
        os.system("pause")
        first_app()

def calculator_app():
    # fungsi penjumlahan
    def add(x, y):
        return x + y
    # fungsi pengurangan
    def subtract(x, y):
        return x - y
    # fungsi perkalian
    def multiply(x, y):
         return x * y
    # fungsi pembagian
    def divide(x, y):
       return x / y
    
    os.system("cls")
    print("-----------------------------------")
    print("Kalkulator")
    print("-----------------------------------")
    print("Pilih Operasi:")
    print("1.Penjumlahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Pembagian")
    print("-----------------------------------")
    print("98. Kembali")
    print("99. Keluar")
    print("-----------------------------------")
    program = input("Pilih salah satu program diatas: ")

    num1_list = []
    num2_list = []

    def input_number():
        number1 = input("Masukkan Bilangan Pertama: ")
        num1_list.append(number1)
        number2 = input("Masukkan Bilangan Kedua: ")
        num2_list.append(number2)

        if number1 == "":
            os.system("cls")
            print("-----------------------------------")
            print("Bilangan yang anda input salah!")
            print("-----------------------------------")
            os.system("pause")
            calculator_app()

        if number2 == "":
            os.system("cls")
            print("-----------------------------------")
            print("Bilangan yang anda input salah!")
            print("-----------------------------------")
            os.system("pause")
            calculator_app() 

    if program == "1":
        input_number()
        num1 = int(num1_list[0])
        num2 = int(num2_list[0])
        print("-----------------------------------")
        print("Hasil Penjumlahan:",num1,"+",num2,"=", add(num1,num2))
        os.system("pause")
        print("-----------------------------------")
        calculator_app()
    elif program == "2":
        input_number()
        num1 = int(num1_list[0])
        num2 = int(num2_list[0])
        print("-----------------------------------")
        print("Hasil Pengurangan:",num1,"-",num2,"=", subtract(num1,num2))
        print("-----------------------------------")
        os.system("pause")
        calculator_app()
    elif program == "3":
        input_number()
        num1 = int(num1_list[0])
        num2 = int(num2_list[0])
        print("-----------------------------------")
        print("Hasil Perkalian:",num1,"X",num2,"=", multiply(num1,num2))
        print("-----------------------------------")
        os.system("pause")
        calculator_app()
    elif program == "4":
        input_number()
        num1 = int(num1_list[0])
        num2 = int(num2_list[0])
        print("-----------------------------------")
        print("Hasil Pembagian:",num1,":",num2,"=", divide(num1,num2))
        print("-----------------------------------")
        os.system("pause")
        calculator_app()
    elif program == "98":
        main()
    elif program == "99":
        os.system("cls")
        os.system("pause")
    else:
        os.system("cls")
        print("-----------------------------------")
        print("Nomor yang anda input salah!")
        print("-----------------------------------")
        os.system("pause")
        calculator_app()


if __name__ == "__main__":
    main()