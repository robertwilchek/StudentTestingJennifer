def remove_short(names, min_len):
    for n in names:       
        print(len(n))      
        print(n) 
        if len(n) < min_len:
            names.remove(n)     
    return names


if __name__ == "__main__":
    data = ["A", "B", "Cat", "Do"]
    print(remove_short(data, 2))

#I believe the bug is coming from the code skipping over B, but I haven't figured out why yet
