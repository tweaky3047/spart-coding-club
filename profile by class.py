class Profile:
    def __init__(self):
        self.profile = {
            "name": "-",
            "gender": "-",
            "birthday": "-",
            "age": "-",
            "phone": "-",
            "email": "-",
        }

    def set_profile(self):
        self.profile ={
            "name": input('name:'),
            "gender": input("gender:"),
            "birthday": input("birthday:"),
            "age": input("age:"),
            "phone": input("phone:"),
            "email": input("email:")
        }
    def get_name(self):
        return self.profile['name']
    def get_gender(self):
        return self.profile['gender']
    def get_birthday(self):
        return self.profile['birthday']
    def get_age(self):
        return self.profile['age']+'세'
    def get_phone(self):
        return self.profile['phone']
    def get_email(self):
        return self.profile['email']
profile = Profile()
profile.set_profile()
print(profile.get_name()) # 이름 출력
print(profile.get_gender()) # 성별 출력
print(profile.get_birthday()) # 생일 출력
print(profile.get_age()) # 나이 출력
print(profile.get_phone()) # 핸드폰번호 출력
print(profile.get_email())