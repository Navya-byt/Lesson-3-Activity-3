incrt_num_1 = int(input("Enter a number 1-3: " ))
incrt_num_2 = int(input("Enter a number 1-3: " ))
incrt_num_3 = int(input("Enter a number 1-3: " ))
print("The expected correct Answer is: -4")
sub_calc = incrt_num_1 - incrt_num_2 - incrt_num_3
print("Calculation", incrt_num_1, "-", incrt_num_2, "-", incrt_num_3, "=", sub_calc)

if sub_calc == -4:
    print("The calculation is correct")

elif sub_calc != -4:
    print("The calculation is incorrect")
    print("Let's swap the numbers and see if the calculation matches")

    print("Swapping first and second numbers...")
    incrt_num_1, incrt_num_2 = incrt_num_2, incrt_num_1
    sub_calc = incrt_num_1 - incrt_num_2 - incrt_num_3
    print("Swapped numbers are , incrt_num_1, incrt_num_2, incrt_num_3")
    print("Calculation", incrt_num_1, "-", incrt_num_2, "-", incrt_num_3, "=", sub_calc)


    if sub_calc == -4:
        print("Now the calculation is correct after first-second swap")

    elif sub_calc != -4:
        print("Still incorrect. Swapping first and third numbers...")
        incrt_num_1, incrt_num_3 = incrt_num_3, incrt_num_1
        sub_calc = incrt_num_1 - incrt_num_2 - incrt_num_3
        print("Swapped numbers are , incrt_num_1, incrt_num_2, incrt_num_3")
        print("Calculation", incrt_num_1, "-", incrt_num_2, "-", incrt_num_3, "=", sub_calc)


        if sub_calc == -4:
            print("Now the calculation is correct after first-third swap")

        else:
            print("Still incorrect. Swapping second and third numbers...")
            incrt_num_2, incrt_num_3 = incrt_num_3, incrt_num_2
            sub_calc = incrt_num_1 - incrt_num_2 - incrt_num_3
            print("Swapped numbers are , incrt_num_1, incrt_num_2, incrt_num_3")
            print("Now the calculation is correct after second-third swap")
            print("Calculation", incrt_num_1, "-", incrt_num_2, "-", incrt_num_3, "=", sub_calc)

            

print("Final and Correct Values and Calculation: ",incrt_num_1, "-",incrt_num_2,"-",incrt_num_3,"=",sub_calc)

