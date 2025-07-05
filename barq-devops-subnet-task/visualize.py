import matplotlib.pyplot as plt

# Creates a bar chart which shows the number of hosts per subnet.
# Takes as input a dictionary with networks as keys and IPv4 addresses as values.
def create_subnet_plot(subnet_grouping):   
    all_subnets = []
    host_counts = []
    for subnet in subnet_grouping:
        all_subnets.append(str(subnet))
        host_counts.append(len(subnet_grouping[subnet]))

    plt.figure(figsize=(19.2, 12))
    plt.bar(all_subnets, host_counts)
    plt.xlabel('Subnets')
    plt.xticks(rotation=35, ha='right') # Rotates the labels so they don't overlap
    plt.ylabel('Host Counts')
    plt.title('Hosts Grouped by Subnet')
    plt.savefig('network_plot.png')