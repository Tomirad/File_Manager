import re, json, codecs
import totalcommander_ftp_password_recovery as tc

def hexdec(hex_string):
    return int(hex_string, 16)

def replace(content, character = ''):
    pass

def main(src_path, images = []):
    with open(src_path, 'r', errors='ignore') as fp:
        for count, line in enumerate(fp):
            pass
    max_limit = count + 1
    modeWorking = 'r'

    ftp = {}
    ftp_head = ''
    while True:
        row = []
        print('Current Limit:', 'Limit:', max_limit, 'Mode:', modeWorking)
        with open(src_path, 'r', errors='ignore', encoding='utf8') as fp:
            for count, line in enumerate(fp):
                line = line.replace("\n", '')
                line_head = re.findall(r"\[(.*)\]", line)
                if len(line_head) > 0:
                    line_head = line_head[0]
                else:
                    line_head = ''
                find = re.findall(r"([A-Za-z0-9]{1,})=(.*)", line)
                if ftp_head != line_head and len(line_head) > 0:
                    ftp_head = line_head
                    ftp[ftp_head] = {}
                elif len(find) > 0:
                    line_cmp = find[0]
                    if line_cmp[0] == 'password':
                        ftp[ftp_head][line_cmp[0]] = tc.tc_decrypt(line_cmp[1])
                    else:
                        ftp[ftp_head][line_cmp[0]] = line_cmp[1]

        print(json.dumps(ftp, indent=4))
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
        
       