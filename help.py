import os

for file in os.listdir("F"):
    if len(file) < 20:
        continue
    ivals = eval(file[4:-8]);
    ps = [];
    for i in range(len(ivals)):
        ps.append(sum(ivals[:i])) 
    if "1.5" not in file and "2.0" not in file:
        print(file)
        os.rename("F/" + file, "F/a/" + file);
       

