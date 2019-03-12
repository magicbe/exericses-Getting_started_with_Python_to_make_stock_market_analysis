number = 10

if number == 10:
    print('歡迎來到投資小判斷')

saving = int(input('請輸入你的存款：'))

if 10000 <= saving <= 50000:
    print('你可以做零股投資')
elif 50000 < saving < 100000:
    print('你可以考慮繼續存並買股票')
elif 100000 <= saving:
    print('你可以直接買股票')
else:
    print('對不起，請確認你的存款')