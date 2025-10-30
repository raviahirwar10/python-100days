#readline()
f = open('day37relate.txt','r')
i = 0
while True:
  i = i+1
  line = f.readline()
  if not line:
      break
  m1 = line.split(",")[0]
  m2 = line.split(",")[1]
  m3 = line.split(",")[2]
  print(f"mark of student{i} in the math: {m1}")
  print(f"mark of student{i} in the English: {m2}")
  print(f"mark of student{i} in the Scienc: {m3}")
  print(line)
  
#writeline()
f = open('day37relate2.txt','w')
lines = ['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close
  
