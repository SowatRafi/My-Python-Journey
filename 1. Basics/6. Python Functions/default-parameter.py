def loveMachine(n='no name'):
    if n == "no name":
        return f"Don't you have any name? or You have {n}?"

    return f"\nI love you, {n}\n"


name = "Sowat Hossain Rafi"
value = loveMachine(name)
print(value)

value = loveMachine()
print(value)

def loveMachine2(n='no name', t='Mr.'):
    if n == "no name":
        return f"Don't you have any name? or You have {n}?"

    return f"\nI love you, {t} {n}\n"


name = "Sowat Hossain Rafi"
value = loveMachine2(name)
print(value)