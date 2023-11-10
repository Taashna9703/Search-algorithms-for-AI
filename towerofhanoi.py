def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    tower_of_hanoi(n - 1, auxiliary, destination, source)
def main():
    n = int(input("Enter the number of disks: "))
    tower_of_hanoi(n, 'A', 'B', 'C')
if __name__ == '__main__':
    main()
    
