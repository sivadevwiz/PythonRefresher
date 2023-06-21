

def func_one():
    def func_two():
        print("Func Two")
    def func_three():
        print("Func Three")
    def func_four():
        print("Func four")

    func_two()
    func_four()


func_one()