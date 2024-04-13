from os import system

menu = {
    'file_manager': '💾 Files Manager',
    'wifi_password': '🔓 Listing Wifi Passwords',
    'mikrotik_password': '🔓 Listing Mikrotik Passwords',
    'totalcommander_password': '🔓 Listing TotalCommander Passwords',
}

def show_list(menu):
    i = 0
    for element in menu:
        i += 1
        print(f"{i}. {menu[element]}")

if __name__ == '__main__':
    i = 0
    while True:
        system('cls')
        print("🔍 TOOLS MANAGER 🔍")
        show_list(menu)
        menu_list  = list(menu)
        input_choose = input("▶️  Choose tool: ")
        numeric_choose = int(input_choose) - 1 if input_choose.isnumeric() else -1
        if input_choose in ['x', 'q']:
            print('close program')
            break
        elif menu_list[numeric_choose] == 'file_manager':
            print('import file_manager')
            import file_manager
            file_manager.main()
            del file_manager
        continue