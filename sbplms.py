from sys import stdin

stacks = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": [],
    "F": []
}
n = 0
Neg = False
A = False


def N(v):
    global n
    n = v


def pop(s):
    N(stacks[s].pop(-1))


def push(s):
    stacks[s].append(n)
    N(0)


def add(a, b):
    pop(a)
    N(int(n) + int(stacks[b].pop(-1)))


def mult(a, b):
    pop(a)
    N(int(n) * int(stacks[b].pop(-1)))


def rem(a):
    stacks[a].pop(-1)


mode = int(input("1: Run commands from STDIN\n" +
                 "2: Run commands from file\n" +
                 "3: Compile commands from file to python"))
CmdList = []

for std in stdin:
    try:
        if mode == 1:
            for line in std:
                A = False
                for i in ['A', 'B', 'C', 'D', 'E', 'F']:
                    for j in ['A', 'B', 'C', 'D', 'E', 'F']:
                        if line.rstrip() == f'{i}+{j}' and not A:
                            add(i, j)
                            A = True
                        elif line.rstrip() == f'{i}*{j}' and not A:
                            mult(i, j)
                            A = True
                        elif line.rstrip() == f'{i}={j}' and not A:
                            N(stacks[i].pop(-1) == stacks[j].pop(-1))
                            A = True
                        elif line.rstrip() == f'{i}<{j}' and not A:
                            N(stacks[i].pop(-1) < stacks[j].pop(-1))
                            A = True
                    if line.rstrip() == f'{i}' and not A:
                        push(i)
                        A = True
                    elif line.rstrip() == f'{i.lower()}' and not A:
                        pop(i)
                        A = True
                    elif line.rstrip() == f"~{i}" and not A:
                        rem(i)
                        A = True
                    # Arithmetic with N
                    elif line.rstrip() == f'{i}+' and not A:
                        N(int(stacks[i].pop(-1)) + int(n))
                        A = True
                    elif line.rstrip() == f'{i}*' and not A:
                        N(int(stacks[i].pop(-1)) * int(n))
                        A = True
                    # Boolops with N
                    elif line.rstrip() == f'{i}=' and not A:
                        N(stacks[i].pop(-1) == n)
                        A = True
                    elif line.rstrip() == f'{i}<' and not A:
                        N(stacks[i].pop(-1) < n)
                        A = True
                if line.rstrip().isdigit() and not A:
                    N(int(line))
                    A = True
                elif line.rstrip()[0] == "I" and not A:
                    N(int(input(line.rstrip()[1:])))
                    A = True
                elif line.rstrip() == "N" and not A:
                    print(n)
                    A = True
                elif line.rstrip() == ".N" and not A:
                    print(chr(n))
                    A = True
                elif line.rstrip() == "~N" and not A:
                    n = -n
                    A = True
                elif line.rstrip() == 'Q' and not A:
                    print("Program end")
                    break
        elif mode == 2:
            with open(f"{std.rstrip()}", 'r') as F:
                for line in F:
                    A = False
                    if line.rstrip()[0] == "#":
                        A = True
                    for i in ['A', 'B', 'C', 'D', 'E', 'F']:
                        for j in ['A', 'B', 'C', 'D', 'E', 'F']:
                            if line.rstrip() == f'{i}+{j}' and not A:
                                add(i, j)
                                A = True
                            elif line.rstrip() == f'{i}*{j}' and not A:
                                mult(i, j)
                                A = True
                            elif line.rstrip() == f'{i}={j}' and not A:
                                N(stacks[i].pop(-1) == stacks[j].pop(-1))
                                A = True
                            elif line.rstrip() == f'{i}<{j}' and not A:
                                N(stacks[i].pop(-1) < stacks[j].pop(-1))
                                A = True
                        if line.rstrip() == f'{i}' and not A:
                            push(i)
                            A = True
                        elif line.rstrip() == f'{i.lower()}' and not A:
                            pop(i)
                            A = True
                        elif line.rstrip() == f"~{i}" and not A:
                            rem(i)
                            A = True
                        # Arithmetic with N
                        elif line.rstrip() == f'{i}+' and not A:
                            N(int(stacks[i].pop(-1)) + int(n))
                            A = True
                        elif line.rstrip() == f'{i}*' and not A:
                            N(int(stacks[i].pop(-1)) * int(n))
                            A = True
                        # Boolops with N
                        elif line.rstrip() == f'{i}=' and not A:
                            N(stacks[i].pop(-1) == n)
                            A = True
                        elif line.rstrip() == f'{i}<' and not A:
                            N(stacks[i].pop(-1) < n)
                            A = True
                    if line.rstrip().isdigit() and not A:
                        N(int(line))
                        A = True
                    elif line.rstrip()[0] == "I" and not A:
                        N(int(input(line.rstrip()[1:])))
                        A = True
                    elif line.rstrip() == "N" and not A:
                        print(n)
                        A = True
                    elif line.rstrip() == ".N" and not A:
                        print(chr(n))
                        A = True
                    elif line.rstrip() == "~N" and not A:
                        n = -n
                        A = True
                    elif line.rstrip() == 'Q' and not A:
                        print("Program end")
                        break
        elif mode == 3:
            with open("output.py", 'w') as out:
                out.write("""stacks = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}\n""")
            with open(f"{std.rstrip()}", 'r') as F:
                with open("output.py", 'a') as out:
                    for line in F:
                        A = False
                        if line.rstrip()[0] == "#":
                            out.write(line.rstrip() + "\n")
                            A = True
                        for i in ['A', 'B', 'C', 'D', 'E', 'F']:
                            for j in ['A', 'B', 'C', 'D', 'E', 'F']:
                                if line.rstrip() == f'{i}+{j}' and not A:
                                    out.write(f"n = stacks['{i}'].pop() + stacks['{j}'].pop()\n")
                                    A = True
                                elif line.rstrip() == f'{i}*{j}' and not A:
                                    out.write(f"n = stacks['{i}'].pop() * stacks['{j}'].pop()\n")
                                    A = True
                                elif line.rstrip() == f'{i}={j}' and not A:
                                    out.write(f"n = (stacks['{i}'].pop() == stacks['{j}'].pop())\n")
                                    A = True
                                elif line.rstrip() == f'{i}<{j}' and not A:
                                    out.write(f"n = (stacks['{i}'].pop() < stacks['{j}'].pop())\n")
                                    A = True
                            if line.rstrip() == f'{i}' and not A:
                                out.write(f"stacks['{i}'].append(n)\n")
                                A = True
                            elif line.rstrip() == f'{i.lower()}' and not A:
                                out.write(f"n = stacks['{i}'].pop()\n")
                                A = True
                            elif line.rstrip() == f"~{i}" and not A:
                                out.write(f"stacks['{i}'].pop()\n")
                                A = True
                            # Arithmetic with N
                            elif line.rstrip() == f'{i}+' and not A:
                                out.write(f"n += stacks['{i}'].pop()\n")
                                A = True
                            elif line.rstrip() == f'{i}*' and not A:
                                out.write(f"n *= stacks['{i}'].pop()\n")
                                A = True
                            # Boolops with N
                            elif line.rstrip() == f'{i}=' and not A:
                                out.write(f"n = (stacks['{i}'].pop() == n)\n")
                                A = True
                            elif line.rstrip() == f'{i}<' and not A:
                                out.write(f"n = (stacks['{i}'].pop() < n)\n")
                                A = True
                        if line.rstrip().isdigit() and not A:
                            out.write(f"n = {line.rstrip()}\n")
                            A = True
                        elif line.rstrip()[0] == "I" and not A:
                            out.write(f"n = int(input('{line.rstrip()[2:]}'))\n")
                            A = True
                        elif line.rstrip() == "N" and not A:
                            out.write("print(n)\n")
                            A = True
                        elif line.rstrip() == ".N" and not A:
                            out.write("print(chr(int(n)))\n")
                            A = True
                        elif line.rstrip() == "~N" and not A:
                            out.write("n = -n\n")
                            A = True
                        elif line.rstrip() == 'Q' and not A:
                            out.write("exit()\n")
                            break

    except Exception as e:
        print(e)
