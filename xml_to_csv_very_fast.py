from xml.etree.ElementTree import iterparse
from tqdm import tqdm
import csv

if __name__ == '__main__':
    file_path = r'524.xml'
    header = ['TNR', 'BEG', 'BEE', 'BEF', 'BES', 'BEI', 'BED', 'VTN', 'NTN', 'WTN', 'CP1', 'CP2', 'EKZ', 'MEN', 'GEW',
              'VP1', 'VP2', 'VP3', 'KKZ', 'WKB', 'LAZ', 'WNR', 'HLW', 'MEC', 'PSY', 'PLM', 'DRT', 'ITS', 'IPA', 'DAA',
              'RGA', 'PLA', 'RLA', 'MAC', 'DAZ', 'RGZ', 'PLZ', 'RLZ', 'MCF', 'SKL', 'IVO', 'VPZ', 'DGI', 'LAE', 'BRE',
              'HOE', 'COO', 'LLP', 'SNP', 'LAG', 'KLK', 'LTY', 'QBL', 'EAS', 'PRS', 'DVC', 'ETB']

    with open('new.csv', 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter=';')
        writer.writerow(header)
        edited_tags = ['TNR', 'VTN', 'NTN', 'WTN']
        cur_string = []
        important_check = True  # for useless tags without SET tag
        for _, elem in tqdm(iterparse(file_path, events=("end",)), total=50804760): # _ for event
            if important_check and elem.tag != 'SET':
                continue
            elif important_check and elem.tag == 'SET':
                important_check = False
                continue
            if elem.tag == 'SET':
                writer.writerow(cur_string)
                cur_string = []
            elif elem.tag in edited_tags:
                cur_text = elem.text
                if cur_text and (cur_text.startswith('A') or cur_text.startswith('W')):
                    new_text = cur_text[0] + cur_text[6:9] + cur_text[1:4] + cur_text[11:13] + cur_text[4:6] + cur_text[9:11] + cur_text[13:15] + cur_text[15:]
                    cur_string.append(new_text.strip())
                elif cur_text and cur_text.startswith('H'):
                    new_text = cur_text[0] + cur_text[9:11] + cur_text[6:9] + cur_text[1:4] + cur_text[11:13] + cur_text[4:6] + cur_text[13:15] + cur_text[15:]
                    cur_string.append(new_text.strip())
                elif not cur_text:
                    cur_string.append('NULL')
                else:
                    cur_string.append(elem.text)
            else:
                cur_string.append(elem.text)
