def replace(content, character = ''):
    ordList = [10, 11]
    for char in ordList:
        content = content.replace(chr(char), character)
    return content

def main(src_path, images = []):
    with open(src_path, 'r', errors='ignore') as fp:
        for count, line in enumerate(fp):
            pass
    max_limit = count + 1
    modeWorking = 'r'
    while True:
        row = []
        print('Current Limit:', 'Limit:', max_limit, 'Mode:', modeWorking)
        with open(src_path, encoding='utf8', errors='ignore', mode=modeWorking) as content:
            row = [next(content) for _ in range(max_limit)]

        newrows = []      
        for line in row:
            newrows.append(replace(line))

        longline = ''.join(newrows)
        splitlist = longline.split('!')
        m2 = []
        for e in splitlist:
            for c in range(0, 10):
                e = e.replace(chr(c), ' ')
            m2.append(e)

        longline = ''.join(m2)
        splitlist = longline.split('M2')
        for m in splitlist:
            print(m)

        choose = input('Choose [c - close]: ')

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
        
       