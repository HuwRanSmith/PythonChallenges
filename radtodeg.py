import math

def rad_to_deg(rad):
    conversion = 180 / math.pi
    deg = rad * conversion
    return deg

def main():
    rad = math.pi * 7 / 4 # 7/4 pi radians
    deg = rad_to_deg(rad)
    print(deg) # 315 degreesx

if __name__ == "__main__":
    main()