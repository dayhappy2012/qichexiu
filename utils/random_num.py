import  random

def main():
    list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    veri_out = random.sample(list_num, 6)
    veri_res = str(veri_out[0]) + str(veri_out[1]) + str(veri_out[2]) + str(veri_out[3]) + str(veri_out[4]) + str(veri_out[5])
    print(veri_res)

if __name__ == '__main__':
    main()