import numpy as np
import pandas as pd
import os

dir = 'cones/'

allCones = pd.DataFrame(columns=['colour', 'data'])

available_folders = os.listdir(dir)

for colour in ['Blue', 'Large Orange', 'Orange', 'Yellow']:
    if colour in available_folders:
        available_files = os.listdir(str(dir+colour))
        for file in available_files:
            try:
                with open('cones/{0}/{1}'.format(colour, file)) as f:
                    current_image = []
                    rows = f.readlines()[11:]
                    for row in rows:
                        col = row[:-1].split(' ')
                        for index in range(0, len(col)):
                            col[index] = float(col[index])
                        current_row = [[col[0],col[1],col[2],col[3],col[4]]]
                        current_image = current_image + current_row

                allCones = allCones.append({'colour' : colour, 'data' : current_image}, ignore_index=True)

            except Exception as e:
                print(colour)
                print(e)

allCones.to_csv(path_or_buf = 'allCones.csv')
print('Saved')
