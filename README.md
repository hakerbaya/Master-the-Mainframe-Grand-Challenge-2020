# HandyZ
![Banner Image](https://raw.githubusercontent.com/hakerbaya/Master-the-Mainframe-Grand-Challenge-2020/master/Screenshots/SC1.png)

## About
HandZ | Tool for Master the Mainframe 2020 Grand Challenge.
  Python Tool to submit, cancel or get relevant Job Information using ZOAU Util.
  This Tool is very handy for Beginners, specifically new mainframers.
  Enjoy Hacking 2021.

## Prerequisites
You will require an account to login to IBM's USS. Next, you will need this folder.

You may copy this folder from /z/z00162/MTM_GRAND_2021 to your local home directory.

Also, you require Python 3.7 and above.

## Setup
```
# You may clone this repo to your local home directory if git is installed.
git clone https://github.com/hakerbaya/Master-the-Mainframe-Grand-Challenge-2020.git

# If you do not have git and is on MtM2020, you may copy the folder from my home directory:
cp -R /z/z00162/MTM_GRAND_2021/ ~

cd MTM_GRAND_2021/
chmod +x *

# Run the setup script to install all modules
./build.sh
```


## Examples Usage
```
  handyz.py : Return List Of Jobs
  handyz.py <USERID> : Return List Of Jobs
  handyz.py <USERID> -d "<DATASET_NAME>" : Submits Job, it must be JCL  <DATASET_NAME> : "MTM2020.PUBLIC.JCL(CHK)"
  handyz.py <USERID> <JOBID> -o <OPTION_NAME> : Choose Option Name in a list:
                                                 list-dds, cancel, submit, cc-status
```

## Acknowledgements
I would like to thank IBM for their wonderful [Master the Mainframe 2020](https://www.ibm.com/it-infrastructure/z/education/master-the-mainframe) challenge.

The crash course on USS, REXX, COBOL, Bash and Python scripting as well as LXSS, Zowe CLI and Ansible are eye-opening and truly fun to tinkle with.


## Licence
This project is licenced under the [MIT](LICENSE) license.

## Screenshots
![SC1](https://raw.githubusercontent.com/hakerbaya/Master-the-Mainframe-Grand-Challenge-2020/master/Screenshots/SC2.png)
![SC2](https://raw.githubusercontent.com/hakerbaya/Master-the-Mainframe-Grand-Challenge-2020/master/Screenshots/SC3.png)

## Submission Poster
![MtM 2020 Grand Challenge Submission Poster](https://raw.githubusercontent.com/hakerbaya/Master-the-Mainframe-Grand-Challenge-2020/master/Screenshots/POSTER.png)
