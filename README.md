# Data_Deduplication_On_Cloud
Data Deduplication Project: A Linux script connected with an S3 bucket for efficient removal of duplicate files, optimizing storage resources.

Welcome to the Data Deduplication Project! This project focuses on developing a Linux script connected with an S3 bucket for efficient deduplication of data.

## Description

The Data Deduplication Project aims to eliminate duplicate files between a local directory and an S3 bucket, optimizing storage resources and improving data management. The script, built for Linux, utilizes the AWS Command Line Interface (CLI) to connect with the S3 bucket and perform deduplication tasks.

## Features

- Seamlessly connect with an S3 bucket using the AWS CLI.
- List all objects in the S3 bucket and retrieve their MD5 hashes.
- Compare local files with S3 objects using MD5 hashes.
- Remove duplicate files from the S3 bucket, improving storage efficiency.

## Prerequisites

To run the script, make sure you have the following:

- Linux operating system
- AWS CLI installed and configured with appropriate access credentials

## Usage

1. Clone the repository:

```bash
git clone https://github.com/patilchaitanya/Data_Deduplication_On_Cloud.git
```

2. Navigate to the project directory:
```bash
cd data-deduplication-project
```

3. Open the script file and set the following variables:

```bash
bucket_name="your-bucket-name"
directory_to_deduplicate="/path/to/directory"
```

4. Make the script executable:
```bash
chmod +x deduplication_script.sh
```

5. Run the script:
```bash
./deduplication_script.sh
```

## Results :

- EC2 Instances
![EC2_Instances](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/30e323eb-0623-4318-9ea1-e2dcd4bd4e1b)

- S3 Bucket 
![S3_Empty](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/4a94ab5e-c3da-4a0d-b730-a7e6ec43357f)

- VPC 
![VPC](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/990529a1-485f-4864-b822-274f2996f770)

![VPC_Subnets](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/031efd74-1c93-4632-bc25-b753a2ad539d)

![Subnets](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/020f5d68-0461-4c0f-bdc3-b532bd83803e)

![Route_tables](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/7645c5f9-1795-4ebf-b806-8378e2505c77)

![NAT_gateway](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/fb078235-0fb0-41e3-8901-a52fed864adb)

![Gateways](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/3e0d2e5c-b0eb-4510-b240-3a0db879a151)

- Output on server

![Output_on_System](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/3b7a75fe-c499-4cd1-b981-38e7c72c7c2d)

![Output_2](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/8270aaf0-a8db-48ab-8d1d-4835a16223fe)

- S3 Bucket

![S3_Bucket](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/f6d1d241-25b9-40dd-97cc-056c5855750c)

![Hash_Folder](https://github.com/patilchaitanya/Data_Deduplication_On_Cloud/assets/73357241/952149d3-5e22-4309-99aa-95dd82e537f0)



## Contribution
Contributions are welcome! If you want to contribute to this project, follow these steps:

## Fork the repository.
Create a new branch: git checkout -b my-feature-branch.
Make your changes and commit them: git commit -m "Add some feature".
Push to the branch: git push origin my-feature-branch.
Open a pull request on GitHub.

## License
This project is licensed under the MIT License.

## Contact
If you have any questions or suggestions, feel free to reach out to the project maintainer:

Email: chaitanyathepatil1603@gmail.com, adityavpawar07@gmail.com, tulshiram1408@gmail.com
Twitter: https://twitter.com/ChaitanyaPatill

## Happy deduplicating!
