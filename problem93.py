# to get change in velocity
# get time in s
# find acc

vi = float(input("Enter vi in m/s"))
vf = float(input("Enter vf in m/s"))
t = float(input("Enter time in s"))
change_velocity = vf-vi
acc = change_velocity / t
print("Acceleration of an obejct = "+str(acc)+"m/s2")