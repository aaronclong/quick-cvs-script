import os

def summarize(func):
    def wrapper(file_name):
        sum_dict = {}
        for item in func(file_name):
            if item in sum_dict:
                sum_dict[item] = sum_dict[item]  + 1
            else:
                sum_dict[item] = 1
        print(str(sum_dict))
        return sum_dict
    return wrapper

@summarize
def load_file(file_name):
    """
    Take cvs file name as param, Load CSV, and return as a Dictionary
    Args:
        file_name (str)
    """
    try:
        with open(file_name, "r") as lines:
            elements = [] 
            for line in lines:
                data = line.split(",")
                elements.append(data[len(data)-1].rstrip())
            return elements

    except Exception as e:
        print("Problem loading File\n %s", str(e))

def save(dictionary):
    with open("output.csv", "w") as file:
        index = 0
        file.write("id,trace_id,count\n")
        for k, v in dictionary.items():
            if k == 'name_in':
                continue

            file.write("{},{},{}\n".format(index,k,v))
            index += 1
        
    
if __name__ == "__main__":
    save(
        load_file("input.csv") 
    )
