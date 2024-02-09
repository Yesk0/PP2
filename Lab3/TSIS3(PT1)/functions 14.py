def some_function() -> None:
    from functions_1 import convert_gramm_to_ounces
    loop_flag_dict = {"Y" : 1,
                      "N" : 0}
    loop_recursion = 1
    while(loop_recursion):
        ounces = int(input("Amount of ounces you want to convert: "))
        print(f"Ounces in grams: {convert_gramm_to_ounces(ounces)}.\n")
        loop_recursion = loop_flag_dict[input("Do you want to convert again?(Y/N)\n").upper()]

    print("See you again!")
    return None

some_function()