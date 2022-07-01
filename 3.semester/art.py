import time
from tqdm import tqdm, trange
from termcolor import colored
import numpy as np

def creeper(iter=1):
    for _ in range(iter):
        for i in range(8):
            time.sleep(0.05)
            for j in range(13):
                if (i==2 or i==3) and (j>=2 and j<=4 or j>=8 and j<=10):
                    print(' ', end='')
                elif i==4 and (j>=5 and j<=7):
                    print(' ', end='')
                elif (i==5 or i==6) and (j>=3 and j<=9):
                    print(' ', end='')
                elif (i==7) and (j==3 or j==4 or j==8 or j==9):
                    print(' ', end='')
                else:
                    print(colored('█', 'green'), end='')
            print('')

        print('tsssssss..')


def draw(canvas, multicolor=True, fill='green'):
    if multicolor == True:
        for i in range(len(canvas[:,0])):
            for j in range(len(canvas[0])):
                # Blank (black)
                if canvas[i,j] == 0:
                    print(2*' ', end='')
                if canvas[i,j] == 0.1:
                    print(' ', end='')
                    print(colored('█', color='green'), end='')
                if canvas[i,j] == 0.2:
                    print(' ', end='')
                    print(colored('█', color='blue'), end='')
                if canvas[i,j] == 0.3:
                    print(' ', end='')
                    print(colored('█', color='red'), end='')
                if canvas[i,j] == 0.4:
                    print(' ', end='')
                    print(colored('█', color='yellow'), end='')
                if canvas[i,j] == 0.5:
                    print(' ', end='')
                    print(colored('█', color='white'), end='')
                if canvas[i,j] == 0.6:
                    print(' ', end='')
                    print(colored('█', color='cyan'), end='')
                if canvas[i,j] == 0.7:
                    print(' ', end='')
                    print(colored('█', color='magenta'), end='')
                if canvas[i,j] == 0.8:
                    print(' ', end='')
                    print(colored('█', color='grey'), end='')

                # Green
                if canvas[i,j] == 1:
                    print(colored('██', color='green'), end='')
                if canvas[i,j] == 1.01:
                    print(colored('█', color='green'), end='')
                    print(' ', end='')
                if canvas[i,j] == 1.2:
                    print(colored('█', color='green'), end='')
                    print(colored('█', color='blue'), end='')
                if canvas[i,j] == 1.3:
                    print(colored('█', color='green'), end='')
                    print(colored('█', color='red'), end='')
                if canvas[i,j] == 1.4:
                    print(colored('█', color='green'), end='')
                    print(colored('█', color='yellow'), end='')
                if canvas[i,j] == 1.5:
                    print(colored('█', color='green'), end='')
                    print(colored('█', color='white'), end='')
                if canvas[i,j] == 1.6:
                    print(colored('█', color='green'), end='')
                    print(colored('█', color='cyan'), end='')
                if canvas[i,j] == 1.7:
                    print(colored('█', color='green'), end='')
                    print(colored('█', color='magenta'), end='')
                if canvas[i,j] == 1.8:
                    print(colored('█', color='green'), end='')
                    print(colored('█', color='grey'), end='')

                # Blue
                if canvas[i,j] == 2:
                    print(colored('██', color='blue'), end='')
                if canvas[i,j] == 2.01:
                    print(colored('█', color='blue'), end='')
                    print(' ', end='')
                if canvas[i,j] == 2.1:
                    print(colored('█', color='blue'), end='')
                    print(colored('█', color='green'), end='')
                if canvas[i,j] == 2.3:
                    print(colored('█', color='blue'), end='')
                    print(colored('█', color='red'), end='')
                if canvas[i,j] == 2.4:
                    print(colored('█', color='blue'), end='')
                    print(colored('█', color='yellow'), end='')
                if canvas[i,j] == 2.5:
                    print(colored('█', color='blue'), end='')
                    print(colored('█', color='white'), end='')
                if canvas[i,j] == 2.6:
                    print(colored('█', color='blue'), end='')
                    print(colored('█', color='cyan'), end='')
                if canvas[i,j] == 2.7:
                    print(colored('█', color='blue'), end='')
                    print(colored('█', color='magenta'), end='')
                if canvas[i,j] == 2.8:
                    print(colored('█', color='blue'), end='')
                    print(colored('█', color='grey'), end='')

                # Red
                if canvas[i,j] == 3:
                    print(colored('██', color='red'), end='')
                if canvas[i,j] == 3.01:
                    print(colored('█', color='red'), end='')
                    print(' ', end='')
                if canvas[i,j] == 3.1:
                    print(colored('█', color='red'), end='')
                    print(colored('█', color='green'), end='')
                if canvas[i,j] == 3.2:
                    print(colored('█', color='red'), end='')
                    print(colored('█', color='blue'), end='')
                if canvas[i,j] == 3.4:
                    print(colored('█', color='red'), end='')
                    print(colored('█', color='yellow'), end='')
                if canvas[i,j] == 3.5:
                    print(colored('█', color='red'), end='')
                    print(colored('█', color='white'), end='')
                if canvas[i,j] == 3.6:
                    print(colored('█', color='red'), end='')
                    print(colored('█', color='cyan'), end='')
                if canvas[i,j] == 3.7:
                    print(colored('█', color='red'), end='')
                    print(colored('█', color='magenta'), end='')
                if canvas[i,j] == 3.8:
                    print(colored('█', color='red'), end='')
                    print(colored('█', color='grey'), end='')

                # Yellow
                if canvas[i,j] == 4:
                    print(colored('██', color='yellow'), end='')
                if canvas[i,j] == 4.01:
                    print(colored('█', color='yellow'), end='')
                    print(' ', end='')
                if canvas[i,j] == 4.1:
                    print(colored('█', color='yellow'), end='')
                    print(colored('█', color='green'), end='')
                if canvas[i,j] == 4.2:
                    print(colored('█', color='yellow'), end='')
                    print(colored('█', color='blue'), end='')
                if canvas[i,j] == 4.3:
                    print(colored('█', color='yellow'), end='')
                    print(colored('█', color='red'), end='')
                if canvas[i,j] == 4.5:
                    print(colored('█', color='yellow'), end='')
                    print(colored('█', color='white'), end='')
                if canvas[i,j] == 4.6:
                    print(colored('█', color='yellow'), end='')
                    print(colored('█', color='cyan'), end='')
                if canvas[i,j] == 4.7:
                    print(colored('█', color='yellow'), end='')
                    print(colored('█', color='magenta'), end='')
                if canvas[i,j] == 4.8:
                    print(colored('█', color='yellow'), end='')
                    print(colored('█', color='grey'), end='')

                # White
                if canvas[i,j] == 5:
                    print(colored('██', color='white'), end='')
                if canvas[i,j] == 5.01:
                    print(colored('█', color='white'), end='')
                    print(' ', end='')
                if canvas[i,j] == 5.1:
                    print(colored('█', color='white'), end='')
                    print(colored('█', color='green'), end='')
                if canvas[i,j] == 5.2:
                    print(colored('█', color='white'), end='')
                    print(colored('█', color='blue'), end='')
                if canvas[i,j] == 5.3:
                    print(colored('█', color='white'), end='')
                    print(colored('█', color='red'), end='')
                if canvas[i,j] == 5.4:
                    print(colored('█', color='white'), end='')
                    print(colored('█', color='yellow'), end='')
                if canvas[i,j] == 5.6:
                    print(colored('█', color='white'), end='')
                    print(colored('█', color='cyan'), end='')
                if canvas[i,j] == 5.7:
                    print(colored('█', color='white'), end='')
                    print(colored('█', color='magenta'), end='')
                if canvas[i,j] == 5.8:
                    print(colored('█', color='white'), end='')
                    print(colored('█', color='grey'), end='')

                # Cyan
                if canvas[i,j] == 6:
                    print(colored('██', color='cyan'), end='')
                if canvas[i,j] == 6.01:
                    print(colored('█', color='cyan'), end='')
                    print(' ', end='')
                if canvas[i,j] == 6.1:
                    print(colored('█', color='cyan'), end='')
                    print(colored('█', color='green'), end='')
                if canvas[i,j] == 6.2:
                    print(colored('█', color='cyan'), end='')
                    print(colored('█', color='blue'), end='')
                if canvas[i,j] == 6.3:
                    print(colored('█', color='cyan'), end='')
                    print(colored('█', color='red'), end='')
                if canvas[i,j] == 6.4:
                    print(colored('█', color='cyan'), end='')
                    print(colored('█', color='yellow'), end='')
                if canvas[i,j] == 6.5:
                    print(colored('█', color='cyan'), end='')
                    print(colored('█', color='white'), end='')
                if canvas[i,j] == 6.7:
                    print(colored('█', color='cyan'), end='')
                    print(colored('█', color='magenta'), end='')
                if canvas[i,j] == 6.8:
                    print(colored('█', color='cyan'), end='')
                    print(colored('█', color='grey'), end='')

                # Magenta
                if canvas[i,j] == 7:
                    print(colored('██', color='magenta'), end='')
                if canvas[i,j] == 7.01:
                    print(colored('█', color='magenta'), end='')
                    print(' ', end='')
                if canvas[i,j] == 7.1:
                    print(colored('█', color='magenta'), end='')
                    print(colored('█', color='green'), end='')
                if canvas[i,j] == 7.2:
                    print(colored('█', color='magenta'), end='')
                    print(colored('█', color='blue'), end='')
                if canvas[i,j] == 7.3:
                    print(colored('█', color='magenta'), end='')
                    print(colored('█', color='red'), end='')
                if canvas[i,j] == 7.4:
                    print(colored('█', color='magenta'), end='')
                    print(colored('█', color='yellow'), end='')
                if canvas[i,j] == 7.5:
                    print(colored('█', color='magenta'), end='')
                    print(colored('█', color='white'), end='')
                if canvas[i,j] == 7.6:
                    print(colored('█', color='magenta'), end='')
                    print(colored('█', color='cyan'), end='')
                if canvas[i,j] == 7.8:
                    print(colored('█', color='magenta'), end='')
                    print(colored('█', color='grey'), end='')

                # Grey
                if canvas[i,j] == 8:
                    print(colored('██', color='grey'), end='')
                if canvas[i,j] == 8.01:
                    print(colored('█', color='grey'), end='')
                    print(' ', end='')
                if canvas[i,j] == 8.1:
                    print(colored('█', color='grey'), end='')
                    print(colored('█', color='green'), end='')
                if canvas[i,j] == 8.2:
                    print(colored('█', color='grey'), end='')
                    print(colored('█', color='blue'), end='')
                if canvas[i,j] == 8.3:
                    print(colored('█', color='grey'), end='')
                    print(colored('█', color='red'), end='')
                if canvas[i,j] == 8.4:
                    print(colored('█', color='grey'), end='')
                    print(colored('█', color='yellow'), end='')
                if canvas[i,j] == 8.5:
                    print(colored('█', color='grey'), end='')
                    print(colored('█', color='white'), end='')
                if canvas[i,j] == 8.6:
                    print(colored('█', color='grey'), end='')
                    print(colored('█', color='cyan'), end='')
                if canvas[i,j] == 8.7:
                    print(colored('█', color='grey'), end='')
                    print(colored('█', color='magenta'), end='')

            print('')
    else:
        for i in range(len(canvas[:,0])):
            for j in range(len(canvas[0])):
                if canvas[i,j] == 0:
                    print(2*' ', end='')
                else:
                    print(colored('██', fill), end='')
            print('')


creeper_canvas = np.array([[1,1,1,1,1,1,1,1],
                           [1,1,1,1,1,1,1,1],
                           [1,0,0,1,1,0,0,1],
                           [1,0,0,1,1,0,0,1],
                           [1,1,1,0,0,1,1,1],
                           [1,1,0,0,0,0,1,1],
                           [1,1,0,0,0,0,1,1],
                           [1,1,0,1,1,0,1,1]])

smile_canvas = np.array([[1,1,1,1,1,1,1,1],
                         [1,1,1,1,1,1,1,1],
                         [1,0,0,1,1,0,0,1],
                         [1,0,0,1,1,0,0,1],
                         [1,1,1,1,1,1,1,1],
                         [1,0.1,1,1,1,1,1.01,1],
                         [1,1.01,0,0,0,0,0.1,1],
                         [1,1,1,1,1,1,1,1]])

bigsmile_canvas = np.array([[1,1,1,1,1,1,1,1],
                            [1,0,0,1,1,0,0,1],
                            [1,0,0,1,1,0,0,1],
                            [1,1,1,1,1,1,1,1],
                            [1,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,1],
                            [1,1,0,0,0,0,1,1],
                            [1,1,1,1,1,1,1,1]])

bird_canvas = np.array([[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                        [2,2,5,5,2,5,5,2,2,2,2,4,4,4,2,2,2],
                        [2,5,2,2,5,2,2,5,2,2,2,4,4,4,2,2,2],
                        [2,2,2,2,2,2,2,2,2,2,2,4,4,4,2,2,2],
                        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                        [6,6,6,6,6,6,6,6,6,6,6,6,8,8,6,6,6],
                        [6,6,6,6,6,6,6,6,6,6,6,8,8,8,8,6,6],
                        [1,1,1,1,1,1,1,1,1,1,8,8.3,3,3,3.8,8,1],
                        [1,0,0,0,1,1,1,1,1,1,1,3,3,3,3,1,1],
                        [1,0,0,0,1,1,1,1,1,1,1,3,8,3,3,1,1],
                        [1,0,0,0,1,0,1,1,1,1,1,3,8,3,3,1,1],
                        [1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,0,0.1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
                        [1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1]])

five_canvas = np.array([[1,1,1,1],
                        [1,0,0,0],
                        [1,1,1,0],
                        [0,0,0,1],
                        [0,0,0,1],
                        [1,1,1,0]])

flag_canvas = np.array([[3, 3, 3, 5.2, 2.5, 3, 3, 3, 3, 3],
                        [3, 3, 3, 5.2, 2.5, 3, 3, 3, 3, 3],
                        [3, 3, 3, 5.2, 2.5, 3, 3, 3, 3, 3],
                        [5, 5, 5, 5.2, 2.5, 5, 5, 5, 5, 5],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                        [5, 5, 5, 5.2, 2.5, 5, 5, 5, 5, 5],
                        [3, 3, 3, 5.2, 2.5, 3, 3, 3, 3, 3],
                        [3, 3, 3, 5.2, 2.5, 3, 3, 3, 3, 3],
                        [3, 3, 3, 5.2, 2.5, 3, 3, 3, 3, 3]])
