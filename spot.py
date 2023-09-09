import streamlit as st
import subprocess

def run_spotinfo(args):
    # Call the shell script and capture the output
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

st.title("AWS EC2 Instance Filter")

# Get user input
st.write("Choose EC2 instance type:")
instance_choice = st.selectbox("Choose EC2 instance type:", [
    "t2.micro", "t2.small", "t2.medium", "t3.nano",  # Add all choices
    "t3.micro", "t3.small", "t3.medium", "c5.large",
    # ... add more choices ...
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
        "./spotinfotool.sh",--type", instance_choice, "--os", os_choice, "--region", region,
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

