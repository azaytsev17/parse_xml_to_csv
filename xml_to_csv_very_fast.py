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
        writer = csv.writer(output_file)
        writer.writerow(header)
        cur_string = []
        important_check = True # for useless tags without SET tag
        for _, elem in tqdm(iterparse(file_path, events=("start",))):
            if important_check and elem.tag != 'SET':
                continue
            elif important_check and elem.tag == 'SET':
                important_check = False
                continue
            if elem.tag == 'SET':
                writer.writerow(cur_string)
                cur_string = []
            else:
                cur_string.append(elem.text)
