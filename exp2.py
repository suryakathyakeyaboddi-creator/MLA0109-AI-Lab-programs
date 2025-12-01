def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary, so they are out of the way
    towers_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Move the n-1 disks from auxiliary to destination
    towers_of_hanoi(n - 1, auxiliary, source, destination)

# Example usage
num_disks = 3
towers_of_hanoi(num_disks, 'A', 'B', 'C')
