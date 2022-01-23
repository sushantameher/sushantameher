import pikepdf
import os

input_path = '/Users/smeher/code/sushantameher/pdfdecrypt/input'
output_path = '/Users/smeher/code/sushantameher/pdfdecrypt/output'
archive_path = '/Users/smeher/code/sushantameher/pdfdecrypt/input/archive'

password = 'sush0503'

for f in os.listdir(input_path):
    if '.pdf' in f:
        print(f)
        pikepdf.open(input_path + '/' + f,password=password)
        print('PDF decrypted.')
        pikepdf.save(output_path + '/' + f)



