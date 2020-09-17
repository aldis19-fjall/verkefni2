# verkefni2

def func()
position = 1.1 
ir_str = input('Direction: ') 
if ir_str == 'n': 
    position += 1 
elif ir_str == 's': 
    position += -1 
elif ir_str == 'a': 
    position += 0.1 
elif ir_str == 'v': 
    position += -0.1 
print('You can travel:', ir_str) 