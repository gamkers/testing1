#!/bin/bash

echo "AWS EC2 Instance Filter Script"
echo "------------------------------"

# Get user input for each option
echo "Choose EC2 instance type:"
echo "1. t2.micro      2. t2.small      3. t2.medium"
echo "4. t3.nano       5. t3.micro      6. t3.small"
echo "7. t3.medium     8. c5.large      9. c5.xlarge"
echo "10. c5.2xlarge   11. c6g.medium   12. c6g.large"
echo "13. c6g.xlarge   14. r5.large     15. r5.xlarge"
echo "16. r5.2xlarge   17. x1.16xlarge   18. x1e.32xlarge"
echo "19. i3.large     20. i3.xlarge    21. i3.2xlarge"
echo "22. d2.xlarge    23. d2.2xlarge   24. d2.4xlarge"
echo "25. p3.2xlarge   26. p3.8xlarge   27. p3.16xlarge"
echo "28. g4dn.xlarge  29. g4dn.12xlarge 30. g4dn.16xlarge"
echo "31. h1.2xlarge   32. h1.4xlarge   33. h1.8xlarge"
echo "34. z1d.large    35. z1d.xlarge   36. z1d.2xlarge"
echo "37. a1.medium    38. a1.large     39. a1.xlarge"
echo "40. m6g.medium   41. m6g.large    42. m6g.xlarge"
echo "40. m6g.medium   41. m6g.large    42. m6g.xlarge"
echo -n "Enter your choice [default: 1]: "
read instance_choice
case $instance_choice in
    2) type="t2.small" ;;
    3) type="t2.medium" ;;
    # ... (same as before, mapping choices to instance types)
    41) type="m6g.large" ;;
    42) type="m6g.xlarge" ;;
    *) type="t2.micro" ;;
esac

echo "Choose instance operating system:"
echo "1. Windows"
echo "2. Linux"
echo "3. macOS"
echo -n "Enter your choice [default: 2]: "
read os_choice
case $os_choice in
    1) os="windows" ;;
    3) os="mac" ;;
    *) os="linux" ;;
esac

echo -n "Enter AWS region (use 'all' for all regions) [default: us-east-1]: "
read region
region=${region:-us-east-1}  # Set default value if user input is empty

echo -n "Enter output format (number|text|json|table|csv) [default: table]: "
read output
output=${output:-table}  # Set default value if user input is empty

echo -n "Enter minimal vCPU cores [default: 0]: "
read cpu
cpu=${cpu:-0}  # Set default value if user input is empty

echo -n "Enter minimal memory GiB [default: 0]: "
read memory
memory=${memory:-0}  # Set default value if user input is empty

echo -n "Enter maximum price per hour [default: 0]: "
read price
price=${price:-0}  # Set default value if user input is empty

echo -n "Enter sort order (interruption|type|savings|price|region) [default: interruption]: "
read sort
sort=${sort:-interruption}  # Set default value if user input is empty

echo -n "Enter sort order (asc|desc) [default: asc]: "
read order
order=${order:-asc}  # Set default value if user input is empty

# Call the hypothetical spotinfo command with gathered arguments
./spotinfo --type "$type" --os "$os" --region "$region" --output "$output" --cpu "$cpu" --memory "$memory" --price "$price" --sort "$sort" --order "$order"

