import pandas as pd
import matplotlib.pyplot as plt
import ipaddress
from visualize import create_subnet_plot

def main():
    ip_df = pd.read_excel('ip_data.xlsx', 'Sheet1')

    # Dictionary that groups IPs together by subnet/CIDR.
    subnet_grouping = {}

    # Dictionary that contains the necessary information that will be written into the CSV file.
    summary_report = {
        'IP Address' : [],
        'Subnet Mask' : [],
        'CIDR Notation' : [],
        'Network Address' : [],
        'Broadcast Address' : [],
        'Number of Host Addresses' : []
    }

    for ip, mask in zip(ip_df['IP Address'], ip_df['Subnet Mask']):
        ip_data = ipaddress.IPv4Interface((ip, mask))
        add_to_report(summary_report, ip_data)

        subnet = ip_data.network
        if subnet not in subnet_grouping:
            subnet_grouping[subnet] = []

        subnet_grouping[subnet].append(ip_data.ip)

    csv_df = pd.DataFrame(summary_report)
    csv_df.to_csv('subnet_report.csv', index=False)

    create_subnet_plot(subnet_grouping)


# Used to add the information from the IPv4Interface to the report dictionary.
def add_to_report(summary_report, ip_data):
    summary_report['IP Address'].append(str(ip_data.ip))
    summary_report['Subnet Mask'].append(str(ip_data.netmask))
    summary_report['CIDR Notation'].append(str(ip_data))
    summary_report['Network Address'].append(str(ip_data.network.network_address))
    summary_report['Broadcast Address'].append(str(ip_data.network.broadcast_address))
    summary_report['Number of Host Addresses'].append(ip_data.network.num_addresses - 2)


if __name__ == '__main__':
    main()