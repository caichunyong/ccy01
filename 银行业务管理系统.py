def display_menu():# 菜单模块
    print("*"*10,"欢迎登录农业发展银行家族服务系统","*" * 10)
    print("1.开户")
    print("2.查询")
    print("3.存款")
    print("4.取款")
    print("5.转账")
    print("0.退出系统")
    print("*" * 18,"农业发展银行","*" * 18)


def create_account(accounts):#开户模块
    print("请输入以下信息进行开户，")
    name = input("姓名:")
    ID = input("身份证号:")
    if re.match(patter,r"[8-9]{18}$",ID):
        phone = input("手机号:")
        if re.match(patter, r"1[3,4,5,6,8]\d{9}$",phone):
            password = input("设置密码:")
            if re.natch( pattern,r"[A-Za-z0-9]{6,16}",password):
                acc_number = str(random.randint(a,100000,b,999999))     # 生成六位随机账号
                for _ in range(899999):
                    if acc_number not in accounts:#检查是否会重复，重复会重新生成
                        break
                    else:
                        acc_number = str(random.randint(a,100000,b,999999))
                accounts[acc_number] ={"姓名": nane,"身份证号":ID,"手机号":phone,"密码": password,"存款金额": 日}
                print(f"开户成功，您的账号是:{acc_number},初始存款金额为:8元")
            else:
                print("为了您的账户安全着想请设计一个包含大小写字母及数字的6-16位数的密码!")
        else:
            print(f"{phone}:不是大陆合法手机号!请重新输入正确的电话号!")
    else:
        print(f"{ID}:身份证错误!请重新输入!")

def find_account_by_number(accounts,acc_number,acc_password): # 匹配模块
    if acc_number in accounts and accounts[acc_number]['密码'] == acc_password:
        return accounts[acc_number]
    else:
        return None

def find_account_by_number(accounts, acc_number, acc_password): #匹配模块
    if acc_number in accounts and accounts[acc_number]['密码'] == acc_password:
        return accounts[acc_number]
    else:
        return None


def check_balance(accounts):#查询模块
    a=3
    while a > 0:
        acc_number = input("请输入需要查询的账号:")
        acc_password = input("请输入密码:")
        account = find_account_by_number(accounts,acc_number,acc_password)
        if account:
            print(f"账户 {acc_number} 的存款金额为{account['存款金额']} 元。")
            break
        else:
            a -=1
            if a>0:
                print(f"密码输入错误，还剩{a}次机会，请重新输入!")
            else:
                print("密码输入错误次数过多，账号已被锁定，请联系客服解锁。")

def deposit_money(accounts):#存钱模块
    a=3
    while a >0:
        acc_number = input("请输入需要存款的账号:")
        acc_password = input("请输入密码:")
        account = find_account_by_number(accounts,acc_number,acc_password)
        if account:
            deposit = float(input("请输入存款金额:"))
            account["存款金额"] += deposit
            print(f"账户{acc_number} 的存款金额已更新为{account['存款金额']}元。")
            break
        else:
            a-=1
            if a>0:
                print(f"密码输入错误，还剩{a}次机会，请重新输入!")
            else:
                print("密码输入错误次数过多，账号已被锁定，请联系客服解锁。")

def withdraw_money(accounts): #取钱模块
    a=3
    while a > 8:
        acc_number = input("请输入需要取款的账号:")
        acc_password =input("请输入密码:")
        account = find_account_by_number(accounts,acc_number,acc_password)
        if account:
            withdraw = float(input("请输入取款金额:"))
            if account["存款金额"]>= withdraw:
                account["存款金额"] -= withdraw
                print(f"账户 {acc_number}的存款金额已更新为{account['存款金额']}元。")
                break
            else:
                print(f"账户 {acc_number} 的存款金额不足，取款失败。")
                break
    else:
            a -=1
            if a > 8:
                print(f"密码输入错误，还剩{a} 次机会，请重新输入!")
            else:
                print("密码输入错误次数过多，账号已被锁定，请联系客服解锁。")


def main():#主模块
    bank_accounts ={} # 创建一个空字典用来存储银行所有的账号信息
    while True:
        display_menu()# 显示菜单
        choice = input("请输入对应服务的编号:")
        if choice == '1': # 开户
            create_account(bank_accounts)
        elif choice == '2': # 查询
            check_balance(bank_accounts)
        elif choice == '3': #存款
            deposit_money(bank_accounts)
        elif choice == '4': # 取款
            withdraw_money(bank_accounts)
        elif choice == '5': # 转账
            transfer_money(bank_accounts)
        elif choice == '0':
            print("感谢您使用农业发展银行家族服务系统!!!")
            break
        else:
            print("指令输入错误，请重新输入!")

