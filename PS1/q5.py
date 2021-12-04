# no. disks, source, destination, spare

def hanoi(disks, src, dest, spr):
    # base case
    if (disks == 1):
        print("{}->{}".format(src, dest))
   # geberal case
    else:
        # step 1
        # move disks-1 from src to spare
        hanoi(disks-1, src, spr, dest)
        
        # step 2
        # move bottom disk from src to dest
        hanoi(1, src, dest, spr)

        # step 3
        # move disks-1 from spare to dest
        hanoi(disks-1, dest, src, spr)
