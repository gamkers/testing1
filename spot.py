import streamlit as st
import subprocess

import os

# Set the file permissions to allow execution
os.chmod('./spotinfo', 0o755)

# Now you can try to execute the file
try:
    subprocess.run('./spotinfo', shell=True)
except Exception as e:
    print(f"Error: {e}")


def run_spotinfo(args):
    # Call the shell script and capture the output
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

st.title("AWS EC2 Instance Filter")

# Get user input
st.write("Choose EC2 instance type:")
instance_choice = st.selectbox("Choose EC2 instance type:", ["t2.micro", "t2.small", "t2.medium", "t2.large", "t2.xlarge", "t2.2xlarge",
    "t3.nano", "t3.micro", "t3.small", "t3.medium", "t3.large", "t3.xlarge", "t3.2xlarge",
    "m3.medium", "m3.large", "m3.xlarge", "m3.2xlarge",
    "m4.large", "m4.xlarge", "m4.2xlarge", "m4.4xlarge", "m4.10xlarge",
    "m5.large", "m5.xlarge", "m5.2xlarge", "m5.4xlarge", "m5.12xlarge", "m5.24xlarge",
    "c3.large", "c3.xlarge", "c3.2xlarge", "c3.4xlarge", "c3.8xlarge",
    "c4.large", "c4.xlarge", "c4.2xlarge", "c4.4xlarge", "c4.8xlarge",
    "c5.large", "c5.xlarge", "c5.2xlarge", "c5.4xlarge", "c5.9xlarge", "c5.12xlarge", "c5.18xlarge",
    "r3.large", "r3.xlarge", "r3.2xlarge", "r3.4xlarge", "r3.8xlarge",
    "r4.large", "r4.xlarge", "r4.2xlarge", "r4.4xlarge", "r4.8xlarge", "r4.16xlarge",
    "x1.16xlarge", "x1.32xlarge",
    "x1e.xlarge", "x1e.2xlarge", "x1e.4xlarge", "x1e.8xlarge", "x1e.16xlarge", "x1e.32xlarge",
    "i2.xlarge", "i2.2xlarge", "i2.4xlarge", "i2.8xlarge",
    "i3.large", "i3.xlarge", "i3.2xlarge", "i3.4xlarge", "i3.8xlarge", "i3.16xlarge",
    "d2.xlarge", "d2.2xlarge", "d2.4xlarge", "d2.8xlarge",
    "h1.2xlarge", "h1.4xlarge", "h1.8xlarge", "h1.16xlarge",
    "f1.2xlarge", "f1.4xlarge", "f1.16xlarge",
    "p2.xlarge", "p2.8xlarge", "p2.16xlarge",
    "p3.2xlarge", "p3.8xlarge", "p3.16xlarge",
    "g2.2xlarge", "g2.8xlarge",
    "g3.4xlarge", "g3.8xlarge", "g3.16xlarge",
    "g4dn.xlarge", "g4dn.2xlarge", "g4dn.4xlarge", "g4dn.8xlarge", "g4dn.12xlarge", "g4dn.16xlarge",
    "m6g.medium", "m6g.large", "m6g.xlarge", "m6g.2xlarge", "m6g.4xlarge", "m6g.8xlarge", "m6g.12xlarge", "m6g.16xlarge",
    "m6gd.medium", "m6gd.large", "m6gd.xlarge", "m6gd.2xlarge", "m6gd.4xlarge", "m6gd.8xlarge", "m6gd.12xlarge", "m6gd.16xlarge",
    "c6g.medium", "c6g.large"
], index=0)

os_choice = st.selectbox("Choose instance operating system:", ["Windows", "Linux", "macOS"])
region = st.text_input("Enter AWS region (use 'all' for all regions)", "us-east-1")
output = st.selectbox("Enter output format", ["number", "text", "json", "table", "csv"], index=3)
cpu = st.slider("Enter minimal vCPU cores", min_value=0, max_value=64, value=0)
memory = st.slider("Enter minimal memory GiB", min_value=0, max_value=256, value=0)
price = st.slider("Enter maximum price per hour", min_value=0.0, max_value=10.0, value=0.0)
sort = st.selectbox("Enter sort order", ["interruption", "type", "savings", "price", "region"], index=0)
order = st.selectbox("Enter sort order", ["asc", "desc"], index=0)

if st.button("Run spotinfo"):
    # Prepare the arguments for the shell script
    args = [
        "./spotinfo","--type", instance_choice, "--os", os_choice, "--region", region,
        "--output", output, "--cpu", str(cpu), "--memory", str(memory),
        "--price", str(price), "--sort", sort, "--order", order
    ]
    
    # Run the shell script and get output
    output, error = run_spotinfo(args)
    
    # Display the output and error
    st.text("Output:")
    st.code(output)
    if error:
        st.text("Error:")
        st.code(error)

