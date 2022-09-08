#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Reading file into list
fileobj=open("file.txt")
lines=fileobj.read()
lst1=lines.split()

# Reading list to dataframe
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
         
dict1=Convert(lst1)
print("Original text file:")
for key, value in dict1.items():
    print(key,value)

# Replacing keys
ini_list1 = ['1', '2', '3', '4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
final_dict1 = dict(zip(ini_list1, list(dict1.values())))

# User input data in sequence
lst2 = ['"affine.expedia.com",','"1432",','"affine@123",','"/hadoop/aws-as-mockproject/modules/pyspark/",','"staging_bix",','"email_domain_name",','"s3://mock_project/",','"/import/",','"s3://mock_project/downloads/tracking/file/",','"/affine/temp/",','"["file1.txt","file2.txt","file3.txt","file4.txt","file5.txt"]",','"aws:east-3:12413525345241352352:bix-affine-ai",','"mockprojectlist.txt",','"Extract_Tracking",','"extract_Tracking_(@areopgregpk\\dascscdc\\ds\\wdwdw\\.zip$",','"date_of_presentation",','"false",','".xls"']

a = len(lst2)
b = len(final_dict1)

# Taking values to list of origianl
lst3=list(final_dict1.values())

# Solution
dict2 = {}
for i in range(b):
    for j in range(a):
        if(i==j):
            if((i==1) or (i==2) or (i==3) or (i==4) or (i==5)):
                final_dict1[i]=lst3[j]
                dict2[i]=final_dict1[i]
            else:
                final_dict1[i]=lst2[j]
                dict2[i]=final_dict1[i]

# Again Replacing key of original  
ini_list2 = ['"parameter_1_ftp_server:"', '"parameter_2_username:"', '"parameter_3_password:"', '"parameter_4_create_stg_script:"','"parameter_5_stg_schema:"','"parameter_6_tgt_schema:"','"parameter_7_s3_stg_path:"','"parameter_8_remote_path:"','"parameter_9_s3_download_path:"','"parameter_10_local_path:"','"parameter_11_files_to_merge:"','"parameter_12_sns_topic;"','"parameter_13_processed_filename:"','"parameter_14_filename:"','"parameter_15_filename_regexp:"','"parameter_16_partition_column:"','"parameter_17_header:"','"parameter_18_extension:"']
final_dict2 = dict(zip(ini_list2, list(dict2.values())))

# Final required modification
print("\nFinal modified file:")
for key, value in final_dict2.items():
    print(key,value)

