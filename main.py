import webbrowser

all_of_price = 0
webbrowser. open('https://sites.google.com/view/hellowelcometomysoftwareworld/%E0%B8%AB%E0%B8%99%E0%B8%B2%E0%B9%81%E0%B8%A3%E0%B8%81')
while True:
    a=input()
    if a=="red":
        all_of_price = all_of_price + 20
    elif a == "gray":
        all_of_price = all_of_price + 40
    elif a == "gold":
        all_of_price = all_of_price + 60
    elif a == "black":
        all_of_price = all_of_price + 80
    elif a == "0":
        break
    else:
        print("สีจานไม่ถูกต้อง")
    print(all_of_price)

print("ราคารวม : ", all_of_price)

webbrowser.open("https://sites.google.com/view/thecredit/%E0%B8%AB%E0%B8%99%E0%B8%B2%E0%B9%81%E0%B8%A3%E0%B8%81")