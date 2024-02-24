def main(src_path, images = [], limit = 10):
    with open(src_path, 'r', errors='ignore') as fp:
        for count, line in enumerate(fp):
            pass
    max_limit = count + 1
    while True:
        row = []
        limit = max_limit if limit > max_limit else limit
        print('Current Limit:', limit, 'Max:', max_limit)
        with open(src_path, encoding='utf8', errors='ignore') as content:
            row = [next(content) for _ in range(limit)]
        print(''.join(row))

        choose = input('Choose [c - close; 0 - all lines; 1-n - limit lines (default: 10)]: ')

        if choose.isnumeric():
            choose_limit = int(choose)
            if choose_limit > 0 and choose_limit <= max_limit:
                limit = choose_limit
            else:
                limit = max_limit
        elif choose in ['c']:
            break
        elif choose in ['x', 'q']:
            exit('close program')
