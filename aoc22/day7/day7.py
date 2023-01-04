class Dir:

    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.files = [] #a list of other File objects
        self.child_dirs = []
        self.parent = parent
    
    #locates a child dir by name
    def find_child_dir(self, n):
        
        index = -1
        for i in range(len(self.child_dirs)):
            if (self.child_dirs[i].name == n):
                index = i
                break

        return index

class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size

def get_dir_size(d, small_dirs):


    child_dir_sizes = [x.size for x in d.child_dirs]
    file_sizes = [x.size for x in d.files]
    #print(f"child_dir_sizes for dir {d.name}: {child_dir_sizes} ")
    #print(f"file sizes for dir {d.name}: {file_sizes} ")


    if (len(d.child_dirs)==0):
        d.size = sum(file_sizes)
        #print(f"dir {d.name} has size {d.size}")
        if (d.size < 100000):
            small_dirs.append(d)

        return d.size
    
    d.size = sum(file_sizes) + sum([get_dir_size(x, small_dirs) for x in d.child_dirs])
    #print(f"dir {d.name} has size {d.size}")

    if (d.size < 100000):
        small_dirs.append(d)

    if (d.name == '/'):
        print(f"Part 1 answer: {sum([x.size for x in small_dirs])}\n\n")

    return d.size

def get_del_dir(d, unused_space, needed_space, smallest_viable):

    #print(f"checking dir {d.name} ")
    #print(f"curr smallest_viable: {smallest_viable} ")
    if (unused_space + d.size > needed_space and d.size < smallest_viable):
        smallest_viable = d.size

    print(f"smallest_viable: {smallest_viable}\n")
    return [get_del_dir(x, unused_space, needed_space, smallest_viable) for x in d.child_dirs]




if __name__== "__main__":


    root_dir = Dir('/', -1, None)
    curr_dir = root_dir

    with open("input.txt", "r") as f:

        for line in f:

            split_line = line.strip().split(' ') 

            if ('/' in line or line.strip() == '$ ls'):
                continue

            if ('$ cd' in line):

                if (split_line[2] == '..'):
                    curr_dir = curr_dir.parent
                else:
                    curr_dir = curr_dir.child_dirs[curr_dir.find_child_dir(split_line[2])]
                
                continue


            if ('dir' in line):
                new_dir = Dir(split_line[1], -1, curr_dir)

                if (new_dir not in curr_dir.child_dirs):
                    curr_dir.child_dirs.append(new_dir)
            else:
                new_f = File(split_line[1], int(split_line[0]))

                if (new_f not in curr_dir.files):
                    curr_dir.files.append(new_f)

    f.close()
    
    print("\n\nGetting sizes \n\n")
    used_mem = get_dir_size(root_dir, [])
    total_mem = 70000000
    needed_mem = 30000000
    unused_mem = total_mem - used_mem

    get_del_dir(root_dir, unused_mem, needed_mem, root_dir.size)

    #if used_mem + d.size > needed_mem and < curr d.size
    #print(f"root_dir.size: : {ans} ")
    print(f"total space - used space = 70000000 - {used_mem} = {70000000 - used_mem}")
    #print(f"smallest dir space: {smallest_viable_dir} ")
