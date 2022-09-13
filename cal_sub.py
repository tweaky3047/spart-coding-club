
def calculator():
    try:
        input_=list(input().split())
        if input_[1]=='+':
            return int(input_[0])+int(input_[2])
        elif input_[1]=='-':
            return int(input_[0]) - int(input_[2])
        elif input_[1]=='*':
            return int(input_[0]) * int(input_[2])
        elif input_[1]=='/':
            return int(input_[0]) / int(input_[2])
        elif input_[1]=='//':
            return int(input_[0]) // int(input_[2])
        elif input_[1]=='%':
            return int(input_[0]) % int(input_[2])
        else:
            print('형식에 맞춰서 다시 입력해주세요!')
            return calculator()
    except:
        print('형식에 맞춰서 다시 입력해주세요!')
        return calculator()

