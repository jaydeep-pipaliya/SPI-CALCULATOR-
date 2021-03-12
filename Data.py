import Niram_data as data
DATA=data.DATA



def Get_Branch_List():
    return list(DATA.keys())



def Get_Branch_Semester_Data(Branch):
    if Branch in DATA:
        return DATA[Branch]
    else:
        raise RuntimeError('Branch not found')


def Get_Branch_Semester_List(Branch='Chemical Engineering-BCH'):
    return list(DATA[Branch].keys())


def Get_Branch_Semester_Sub_List(Branch,Semester):
    list=Get_Branch_Semester_Data(Branch)

    # print(list)
    if Semester in list:
        return list[Semester]
    else:
        raise RuntimeError('Semester not found')

if __name__=="__main__":
    print(Get_Branch_List())

