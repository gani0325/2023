phone_book = ["119", "97674223", "1195524421"]


for i in range(len(phone_book)) :
    for j in range(1, len(phone_book[i])) :
        if phone_book[i] == phone_book[j][:len(phone_book[i])] :
            print(phone_book[j][:len(phone_book[i])])
            print(phone_book[i])
            print("====================")
            answer = False
            break
        else :
            answer = True