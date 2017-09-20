import pickle
from Good import Good
from GoodsCollection import GoodsCollection
from GoodsTypesCollection import GoodsTypesCollection
from GoodType import GoodType

goodsCollection = GoodsCollection()
typesCollection = GoodsTypesCollection()

def init(goodsCollection, typesCollection):

    with open('Goods.txt', 'rb') as f:
        goodsCollection.goods = pickle.load(f)
        goodsCollection.maxIndex = goodsCollection.goods.__len__()
    with open('Types.txt', 'rb') as f:
        typesCollection.goodTypes = pickle.load(f)
        typesCollection.maxIndex = typesCollection.goodTypes.__len__()

def initDialog(goodsCollection, typesCollection):
    choice = input("Choose the collection: 1 - goods' collection, 2 - goods' types' collection;"
                   "\n\t3 - compose the types of the goods which price is higher than 10;"
                   "\n\t4 - save data to the file;"
                   "\n\t5 - load data from the file (enter any other value to exit): ")
    if (choice == '1'):
        processGC(goodsCollection, typesCollection)
    elif (choice == '2'):
        processTC(goodsCollection, typesCollection)
    elif (choice == '3'):
        print(goodsCollection.composewHigherPriceSearch(typesCollection))
    elif(choice == '4'):
        with open('Goods.txt', 'wb') as f:
            pickle.dump(goodsCollection.goods,f)
        with open('Types.txt', 'wb') as f:
            pickle.dump(typesCollection.goodTypes,f)
        if (str(input("Enter 5 to continue. Enter any other value to exit: ")) == '5'):
            initDialog(goodsCollection, typesCollection)
    elif(choice == '5'):
        with open('Goods.txt', 'rb') as f:
            goodsCollection.goods = pickle.load(f)
        goodsCollection.maxIndex = goodsCollection.goods.__len__()
        with open('Types.txt', 'rb') as f:
            typesCollection.goodTypes = pickle.load(f)
        typesCollection.maxIndex = typesCollection.goodTypes.__len__()
        if (str(input("Enter 5 to continue. Enter any other value to exit: ")) == '5'):
            initDialog(goodsCollection, typesCollection)
    else:
        return

def processGC(goodsCollection, typesCollection):
    choice = str(input("Choose the operation: 1 - add new good, 2 - delete a good by ID, 3 - edit a good by ID, 4 - display. Press 5 to dissmiss. Enter any other value to exit: "))
    if(choice == '1'):
        newGood = Good(input("Enter the good's name: "), int(input("Enter the good's price: ")), int(input("Enter the corresponding good's type's ID: ")))
        flag = 0
        for type in typesCollection.goodTypes:
            if (type.gtID == newGood.gtID):
                flag = 1
                goodsCollection.add(newGood)
        if (flag == 0):
            print("Good's type with the entered ID does not exist.")
        if (str(input("Enter 5 to continue. Enter any other value to exit: ")) == '5'):
            processGC(goodsCollection, typesCollection)
        else:
            return
    elif(choice == '2'):
        flag = 0
        while (flag == 0):
            try:
                choice = int(input("Enter the ID (input 0 to dismiss): "))
                if (choice > goodsCollection.goods.__len__()):
                    print("Wrong ID.")
                elif(choice == '0'):
                    break
                else:
                    goodsCollection.delete(choice)
                    flag = 1
            except ValueError:
                print("Input error: the value must be numeric.")

        if(input("Enter 5 to continue. Enter any other value to exit: ") == '5'):
            processGC(goodsCollection, typesCollection)
        else:
            return
    elif(choice == '3'):
        flag = 0
        editChoice = 0
        idChoice = 0
        while (flag < 2):
            while (flag == 0):
                try:
                    idChoice = eval(input("Enter the good's ID: "))
                    if(idChoice > 0 and idChoice < goodsCollection.goods.__len__()):
                        flag += 1
                    else:
                        print("Wrong ID.")
                except ValueError:
                    print("Input error: the value must be numeric.")
            while(flag == 1):
                try:
                    editChoice = int(input("Choose an editing mode: 1 - edit the name, 2 - edit the price, 3 - edit the good's type's ID, 0 - edit all: "))
                    if(editChoice >= 0 and editChoice < 4):
                        flag += 1
                    else:
                        print("Wrong value.")
                except ValueError:
                    print("Input error: the value must be numeric.")
        if(editChoice == 1):
            goodsCollection.edit(idChoice, editChoice, typesCollection, input("Input new good's name: "))
        elif(editChoice == 2):
            goodsCollection.edit(idChoice, editChoice, typesCollection, "", eval(input("Input new good's price: ")))
        elif(editChoice == 3):
            goodsCollection.edit(idChoice, editChoice, typesCollection, "", 0, eval(input("Input new good's type's ID: ")))
        elif(editChoice == 4):
            goodsCollection.edit(idChoice, editChoice, typesCollection,input("Input new good's name: "), eval(input("Input new good's price: ")), eval(input("Input new good's type's ID: ")))
        if(input("Enter 5 to continue. Enter any other value to exit: ") == '5'):
            processGC(goodsCollection, typesCollection)
    elif(choice == '4'):
        print("\nGoods' collection:")
        print(goodsCollection)
        if(input("Enter 5 to continue. Enter any other value to exit: ") == '5'):
            processGC(goodsCollection, typesCollection)
    elif(choice == '5'):
        initDialog(goodsCollection, typesCollection)
    else:
        return
def processTC(goodsCollection, typesCollection):
    choice = str(input("Choose the operation: 1 - add new good's type, 2 - delete a good's type by ID, 3 - edit a good's type by ID, 4 - display. Press 5 to dissmiss. Enter any other value to exit: "))
    if (choice == '1'):
        newType = GoodType(input("Enter the good's type's name: "), input("Enter the good's type's manufacturer: "))
        typesCollection.add(newType)
        if (str(input("Enter 5 to continue. Enter any other value to exit: ")) == '5'):
            processTC(goodsCollection, typesCollection)
        else:
            return
    elif (choice == '2'):
        flag = 0
        while (flag == 0):
            try:
                choice = int(input("Enter the ID (input 0 to dissmiss): "))
                if(choice > 0 and choice <= typesCollection.goodTypes.__len__()):
                    deletingFlag = 0
                    for good in goodsCollection.goods:
                        if(good.gtID == choice):
                            deletingFlag = 1
                            break
                    if (deletingFlag == 0):
                        typesCollection.delete(choice, goodsCollection)
                        flag = 1
                    else:
                        print(
                            "At first delete all the goods of the chosen type. Then you will be able to delete the type.")
                elif (choice == 0):
                    break
                else:
                    print("Wrong ID.")
            except ValueError:
                print("Input error: the value must be numeric.")
        if (input("Enter 5 to continue. Enter any other value to exit: ") == '5'):
            processTC(goodsCollection, typesCollection)
        else:
            return
    elif (choice == '3'):
        flag = 0
        editChoice = 0
        idChoice = 0
        while (flag < 2):
            while (flag == 0):
                try:
                    idChoice = eval(input("Enter the good's type's ID: "))
                    flag += 1
                except ValueError:
                    print("Input error: the value must be numeric.")
            while (flag == 1):
                try:
                    editChoice = eval(input("Choose an editing mode: 1 - edit the name, 2 - edit the manufacturer, 3 - edit both: "))
                    if (editChoice > 0 and editChoice < 4):
                        flag += 1
                    else:
                        print("Wrong value.")
                except ValueError:
                    print("Input error: the value must be numeric.")
                if(editChoice == 1):
                    typesCollection.edit(idChoice - 1, editChoice, input("Input new good's type's name:"))
                elif(editChoice == 2):
                    typesCollection.edit(idChoice - 1, editChoice, "", input("Input new good's type's Manufacturer: "))
                elif(editChoice == 3):
                    typesCollection.edit(idChoice - 1, editChoice, input("Input new good's type's name:"), input("Input new good's type's Manufacturer: "))
    elif (choice == '4'):
        print("\nGoods' types' collection:")
        print(typesCollection)
        if (input("Enter 5 to continue. Enter any other value to exit: ") == '5'):
            processTC(goodsCollection, typesCollection)
    elif (choice == '5'):
        processTC(goodsCollection, typesCollection)
    else:
        return


init(goodsCollection, typesCollection)
initDialog(goodsCollection, typesCollection)