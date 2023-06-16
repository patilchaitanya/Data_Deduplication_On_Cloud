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

## Contribution
Contributions are welcome! If you want to contribute to this project, follow these steps:

##Fork the repository.
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
