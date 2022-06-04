from cProfile import run
from AC import *
from board import board
from coordinate import Coordinate
from constraint import Arithmetic_Constraint
from boardgeneration import *
from backtrack import Back_Track
from backtrackFC import Back_Track_FC
from gui import *
import time

#### ANALYSIS SECTION ###

#1. 100 3X3 BOARD FOR EACH ALGORITHM 
total_time=0
for i in range (100):
    b = createBoard(3)
    start = time.time()
    bt=Back_Track(b)
    bt.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking algorithm on 100 3x3 board is: ",total_time, " seconds.") 

total_time=0
for i in range (100):
    b = createBoard(3)
    start = time.time()
    bt_fc=Back_Track_FC(b)
    bt_fc.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking with forward checking algorithm on 100 3x3 board is: ",total_time, " seconds.") 

total_time=0
for i in range (100):
    b = createBoard(3)
    start = time.time()
    bt_ac=AC(b)
    bt_ac.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking with AC algorithm on 100 3x3 board is: ",total_time, " seconds.") 


############################################################################################################################
#2. 100 4X4 BOARD FOR EACH ALGORITHM 
total_time=0
for i in range (100):
    b = createBoard(4)
    start = time.time()
    bt=Back_Track(b)
    bt.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking algorithm on 100 4x4 board is: ",total_time, " seconds.") 

total_time=0
for i in range (100):
    b = createBoard(4)
    start = time.time()
    bt_fc=Back_Track_FC(b)
    bt_fc.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking with forward checking algorithm on 100 4x4 board is: ",total_time, " seconds.") 

total_time=0
for i in range (100):
    b = createBoard(4)
    start = time.time()
    bt_ac=AC(b)
    bt_ac.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking with AC algorithm on 100 4x4 board is: ",total_time, " seconds.") 

##########################################################################################################################
#3. 100 5X5 BOARD FOR EACH ALGORITHM 
total_time=0
for i in range (100):
    b = createBoard(5)
    start = time.time()
    bt=Back_Track(b)
    bt.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking algorithm on one 5x5 board is: ",total_time, " seconds.") 

total_time=0
for i in range (100):
    b = createBoard(5)
    start = time.time()
    bt_fc=Back_Track_FC(b)
    bt_fc.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking with forward checking algorithm on one 5x5 board is: ",total_time, " seconds.") 

total_time=0
for i in range (100):
    b = createBoard(5)
    start = time.time()
    bt_ac=AC(b)
    bt_ac.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking with AC algorithm on one 5x5 board is: ",total_time, " seconds.") 

###################################################################################################################
#4. one 6X6 BOARD FOR EACH ALGORITHM 
total_time=0
for i in range (1):
    b = createBoard(6)
    start = time.time()
    bt=Back_Track(b)
    bt.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking algorithm on one 6x6 board is: ",total_time, " seconds.") 

total_time=0
for i in range (1):
    b = createBoard(6)
    start = time.time()
    bt_fc=Back_Track_FC(b)
    bt_fc.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking with forward checking algorithm on one 6x6 board is: ",total_time, " seconds.") 

total_time=0
for i in range (1):
    b = createBoard(6)
    start = time.time()
    bt_ac=AC(b)
    bt_ac.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking with AC algorithm on one 6x6 board is: ",total_time, " seconds.") 

##############################################################################################################
#5. one 7X7 BOARD FOR EACH ALGORITHM 
total_time=0
for i in range (1):
    b = createBoard(7)
    start = time.time()
    bt=Back_Track(b)
    bt.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking algorithm on one 7x7 board is: ",total_time, " seconds.") 

total_time=0
for i in range (1):
    b = createBoard(7)
    start = time.time()
    bt_fc=Back_Track_FC(b)
    bt_fc.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking with forward checking algorithm on one 7x7 board is: ",total_time, " seconds.") 

total_time=0
for i in range (1):
    b = createBoard(7)
    start = time.time()
    bt_ac=AC(b)
    bt_ac.solve()
    end = time.time()
    total_time=total_time+(end-start)
print("Total time for BackTracking with AC algorithm on one 7x7 board is: ",total_time, " seconds.") 