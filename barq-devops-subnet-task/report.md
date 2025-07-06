# Analysis Questions

**1. Which subnet has the most hosts?**  
 Each subnet has only one host on it.

---

**2. Are there any overlapping subnets? If yes, which ones?**  
There are no overlapping subnets. I double-checked by iterating over all subnets and used the overlaps function from the ipaddress library to compare every pair of subnets.

---

**3. What is the smallest and largest subnet in terms of address space?**  
The subnets 192.168.100.0, 10.2.0.0, 172.16.48.0, 10.20.4.0, 192.168.20.0, 10.3.0.0, 172.16.60.0 and 10.15.4.0 all have an address space of 1024, making them the largest subnets. On the other hand, the subnets 192.168.1.0, 172.16.20.0, 10.0.3.0, 192.168.2.0, 192.168.3.0, 10.4.3.0, 172.16.40.0, 192.168.10.0, 192.168.4.0, 10.50.2.0 all have an address space of 256, making them the smallest subnets.

---

**4. Suggest a subnetting strategy that could reduce wasted IPs in this network.**  
In order to waste fewer IP addresses, dedicating the appropriate number of bits for the host portion of the IP address is a good strategy. In general, you should not have an address space that's far too large in comparison to the number of hosts that will actually be connected to the network.