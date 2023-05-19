from LSC_gen import LSC



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    percentages = [0.1, 0.5]
    generator = LSC(10)

    for i in range(len(percentages)):
        print("Percentage of the removed cells is ", percentages[i])
        print("Generated Latin square: \n",generator.puzzle_mode(i), "\n")

