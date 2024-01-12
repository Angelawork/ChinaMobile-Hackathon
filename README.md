# ChinaMobile-Hackathon
In the course of conducting business operations, to ensure data security, it is necessary to regularly carry out security audits. Participants are required to effectively identify accounts exhibiting high-frequency access, account reuse, access from uncommon IP addresses, access during non-working hours, login anomalies, and other abnormal behaviours from the provided data access logs. Finally, submit these identified accounts along with their associated types of anomalies and the times these anomalies occurred. 

**Each submitted version can be executed by the `name = main` function, accepting two parameters:**
~~~
if __name__ == "__main__":
    to_pred_path  = sys.argv[1] # Data path
    result_save_path = sys.argv[2] # Output path
    main(to_pred_path, result_save_path) # Run the main function
~~~ 
## Run the program
Run the file in the Python console and then enter `test()`

## Switch between using trainA.csv and testdata.csv
In the tools.py file, modify the get_fcsv_path() function:
```
  #file_path = os.path.join(parent_directory, 'input', '数据安全赛道', 'trainA.csv')
  file_path = os.path.join(parent_directory, 'input', '数据安全赛道', 'testdata.csv')
```

