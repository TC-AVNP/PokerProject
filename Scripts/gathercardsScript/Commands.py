#moves for each table coordinadest for each move
# table1_moves={"fold":c,"check":c,"raise":c}
# table2_moves={"fold":c,"check":c,"raise":c}
# table3_moves={"fold":c,"check":c,"raise":c}
# table4_moves={"fold":c,"check":c,"raise":c}
# import time

# for i in range(0,4):
# 	print(i+1)
# 	time.sleep(1)
import pyautogui

table1_moves={"fold":(466,340),"check":(545,340)}
table2_moves={"fold":(957,340),"check":(1038,340)}
table3_moves={"fold":(462,701),"check":(545,700)}
table4_moves={"fold":(956,701),"check":(1038,700)}

table= {"table1_moves":table1_moves,"table2_moves":table2_moves,
"table3_moves":table3_moves,"table4_moves":table4_moves}

def clika(tableName):
	print("foldar a mesa"+tableName)
	pyautogui.click(table[tableName+"_moves"]["fold"])
	pyautogui.click(table[tableName+"_moves"]["check"])
