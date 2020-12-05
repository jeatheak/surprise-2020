class Utils():

    def leftRotation(my_list):
        output_list = []

        for item in range(1, len(my_list)):
            output_list.append(my_list[item])

        output_list.append(my_list[0])

        return output_list

    def rightRotation(my_list):
        output_list = [my_list[len(my_list)-1]]

        for item in range(0, len(my_list) - 1):
            output_list.append(my_list[item])

        return output_list
