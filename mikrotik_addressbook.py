def replace(content, character = ''):
    ordList = [10, 11]
    for char in ordList:
        content = content.replace(chr(char), character)
    return content

def main(src_path, images = [], limit = 10):
    with open(src_path, 'r', errors='ignore') as fp:
        for count, line in enumerate(fp):
            pass
    max_limit = count + 1
    modeWorking = 'r'
    while True:
        row = []
        limit = max_limit if limit > max_limit else limit
        print('Current Limit:', limit, 'Max:', max_limit, 'Mode:', modeWorking)
        with open(src_path, encoding='utf8', errors='ignore', mode=modeWorking) as content:
            row = [next(content) for _ in range(limit)]
        row3 = []       
        for line in row:
            row3.append(replace(line))

        longline = ''.join(row3)
        splitlist = longline.split('!')

        for e in splitlist:
            hexList = ['\x00', '\x08', '\x04', '\x03', '\x02', '\x01', '\x00', '\x07', '\x06', '\x09','\x05' ]
            for c in range(0,10):
                e.replace(chr(c), '')
            print(e)

        choose = input('Choose [c - close; 0 - all lines; 1-n - limit lines (default: 10)]: ')

        if choose.isnumeric():
            choose_limit = int(choose)
            if choose_limit > 0 and choose_limit <= max_limit:
                limit = choose_limit
            else:
                limit = max_limit
        elif choose in ['c']:
            break
        elif choose in ['b']:
            modeWorking = 'rt'
        elif choose in ['x', 'q']:
            exit('close program')
        
       
