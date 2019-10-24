import time
import os

frameList = ['''
   _  
  / \\\
  |-|
  |-|
  |-|
  |-|
  |-|

''',
'''
   _  
  / \
  |-|
  |-|
  |-|
  |-|
  |-|
  /|\\
 /|||\\
''',
'''
   _ 
  / \
  |-|
  |-|
  |-|
  |-|
  |-|
  /|\\
 /|||\\
/|||||\\
'''
]         

while True:
	os.system("cls")
	for frame in frameList:
		print(frame)
		time.sleep(.2)
		os.system("cls")       