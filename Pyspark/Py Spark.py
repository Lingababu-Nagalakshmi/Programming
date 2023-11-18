# PySpark – Create an empty DataFrameprint("#Create empty RDD Using Pyspark")
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
emptyRDD = spark.sparkContext.emptyRDD()
print(emptyRDD)


#print("#create empty RDD using parallelize")
rdd2= spark.sparkContext.parallelize([])
print(rdd2)


#print("#create DataFrame with Schema()(Struct Type)")
from pyspark.sql.types import StructType,StructField
schema = StructType([StructField('fristname',StringType(),True),StructField('middlename',StringType(),True),StructField('lastname',StringType(),True)])
df =spark.createDataFrame(emptyRDD,schema)
df.printSchema()




#print("#Create empty RDD to Schema")
df =emptyRDD.toDF(schema)
print(df)


#print("#create DataFrame directly")
df = spark.createDataFrame([],schema)
df.printSchema()


#print("#create DataFrame without Schema(no columns")
df = spark.createDataFrame([],StructType([]))
df.printSchema()


# PySpark – Convert RDD to DataFrame
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
dept = [("Finace",20),("Markteing",30),("Sales",40),("IT",50)]
deptColumns = ["Department","rank"]
rdd =spark.sparkContext.parallelize(dept)
#rdd to Dataframes 
df = rdd.toDF(deptColumns)
df.printSchema()
df.show(truncate=False)




#print("#Using create DataFrame using pyspark")
df = spark.createDataFrame(rdd,schema=deptColumns)
df.printSchema()
df.show(truncate=False)
        
        
#print("#Create DataFrame using StructType Schema")
from pyspark.sql.types import StructType,StructField,StringType
schema = StructType([StructField('Department',StringType(),True),StructField('Rank',StringType(),True)]) 
df = spark.createDataFrame(rdd,schema=schema)
df.printSchema()
df.show(truncate=False)



# PySpark – Convert DataFrame to Pandas
#Note --- for RDD creation #rdd =spark.sparkContext.parallelize(dept)
#Note ---for DataFrame creation:pysparkDF =spark.createDataFrame(data=data,schema =columns)
#Note without Schema : pysparkDF =spark.createDataFrame(data=data,schema =columns) By default we get it
#Note with Schema we can get it by Struct Type,StructFeild,StringType we can customise what we want
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [("James","","Smith","36636","M",60000),("Michael","Rose","","40288","M",70000),
        ("Robert","","Williams","42114","",400000),("Maria","Anne","Jones","39192","F",500000),
        ("Jen","Mary","Brown","","F",0)]

columns = ["first_name","middle_name","last_name","dob","gender","salary"]
pysparkDF =spark.createDataFrame(data=data,schema =columns)
pysparkDF.show(truncate=False)

#Converting DataFrame to pandas 
DFpandasDF =pysparkDF.toPandas()
print(DFpandasDF)

#converting Pyspark DF to pandas 
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType,StructType,IntegerType
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

data = [("James","","Smith","36636","M",60000),("Michael","Rose","","40288","M",70000),
        ("Robert","","Williams","42114","",400000),("Maria","Anne","Jones","39192","F",500000),
        ("Jen","Mary","Brown","","F",0)]

pysparkColumns = StructType([StructField("frist_name",StringType(),True),StructField("middle_name",StringType(),True),StructField("last_name",StringType(),True),StructField("dob",StringType(),True),StructField("gender",StringType(),True),StructField("salary",StringType(),True)])
columns = ["first_name","middle_name","last_name","dob","gender","salary"]
pysparkDF =spark.createDataFrame(data=data,schema = pysparkColumns)
pysparkDF.show(truncate=False)


#converting Pyspark DF to pandas 
DFpandasDF =pysparkDF.toPandas()
print(DFpandasDF)


# Default - displays 20 rows and # 20 charactes from column value pysparkDF.show()
# #Display full column contentspysparkDF.show(truncate=False)
# # Display 2 rows and full column contentspysparkDF.show(2,truncate=False) 
# # Display 2 rows & column values 25 characterspysparkDF.show(2,truncate=25)
#  # Display DataFrame rows & columns verticallypysparkDF.show(n=3,truncate=25,vertical=True)
# PySpark – StructType & StructField
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType,StructType,IntegerType
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [("James","","Smith","36636","M",60000),("Michael","Rose","","40288","M",70000),("Robert","","Williams","42114","",400000),("Maria","Anne","Jones","39192","F",500000),("Jen","Mary","Brown","","F",0)]
pysparkColumns = StructType([StructField("frist_name",StringType(),True),StructField("middle_name",StringType(),True),StructField("last_name",StringType(),True),StructField("dob",StringType(),True),StructField("gender",StringType(),True),StructField("salary",StringType(),True)])
columns = ["first_name","middle_name","last_name","dob","gender","salary"]
pysparkDF =spark.createDataFrame(data=data,schema = pysparkColumns)
pysparkDF.printSchema()
pysparkDF.show(truncate=False)


#Adding the Dataframe and with the schema
from pyspark.sql.types import StringType,StructType,IntegerType,StructField
structureData = [(("James","","Smith"),"36636","M",3100),(("Michael","Rose",""),"40288","M",4300),(("Robert","","Williams"),"42114","M",1400),(("Maria","Anne","Jones"),"39192","F",5500),(("Jen","Mary","Brown"),"","F",-1)]
structureSchema = StructType([StructField('name', StructType([StructField('firstname', StringType(), True),StructField('middlename', StringType(), True),StructField('lastname', StringType(), True)])),StructField('id', StringType(), True),StructField('gender', StringType(), True),StructField('salary', IntegerType(), True)])
df2 = spark.createDataFrame(data=structureData,schema=structureSchema)
df2.printSchema()
df2.show(truncate=False)


#5. Adding & Changing struct of the DataFrame
from pyspark.sql.functions import col, when, struct
updatedDF = df2.withColumn("Otherinfo",struct(col("id").alias("identifier"),col("gender").alias("gender"),col("salary").alias("salary"),when(col("salary").cast(IntegerType()) > 2000 , "Low")
                                              .when(col("salary").cast(IntegerType()) > 4000 , "High").otherwise("High").alias("Salary_Grade"))).drop("id","gender","salary")
updatedDF.printSchema()
updatedDF.show(truncate = False)


# PySpark – Column Class
# PySpark Column Class | Operators & Functions
from pyspark.sql.functions import lit
colobj =lit('sparkbyexamples.com')
data = [("James",23),("Ann",40)]
df = spark.createDataFrame(data).toDF("name","gender")
df.printSchema()



#with df.select(df.gender).show()
#with bracketsdf.select(df["gender"]).show()
#with col
from pyspark.sql.functions import col
df.select(col("gender")).show()
df.select(col("name")).show()



#Create DataFrame with struct using Row class
from pyspark.sql import Row
data = [Row(name="James",prop=Row(hair="black",eyes="blue")),
        Row(name="Ann",prop=Row(hair="grey",eyes="black"))]
df = spark.createDataFrame(data)
df.printSchema()

df.select(df.prop.hair).show()
df.select(df["prop.hair"]).show()
df.select(col("prop.hair")).show()
df.select(col("prop.*")).show()



#PySpark Column Operatorsdata=[(100,2,1),(200,3,4),(300,4,4)]
df=spark.createDataFrame(data).toDF("col1","col2","col3")
df.show()
df.select(df.col1 + df.col2).show()
df.select(df.col1 - df.col2).show() 
df.select(df.col1 * df.col2).show()
df.select(df.col1 / df.col2).show()
df.select(df.col1 % df.col2).show()
df.select(df.col2 > df.col3).show()
df.select(df.col2 < df.col3).show()
df.select(df.col2 == df.col3).show()

#working with alias 
data=[("James","Bond","100",None),("Ann","Varsa","200",'F'),("Tom Cruise","XXX","400",''),("Tom Brand",None,"400",'M')]
columns=["fname","lname","id","gender"]
df=spark.createDataFrame(data,columns)
df.show(truncate=False)
df.select(df.fname.alias("fristname")).show()
df.select(df.lname.alias("lastname")).show()
df.select(df.id.alias("Information Details")).show()




#expr condition is used to merge the two columns in single columns
from pyspark.sql.functions import expr
df.select(expr("fname ||',' || lname").alias("fullname")).show()
data=[("James","Bond","100",None),("Ann","Varsa","200",'F'),("Tom Cruise","XXX","400",''),("Tom Brand",None,"400",'M')]
columns=["fname","lname","id","gender"]
df=spark.createDataFrame(data,columns)
df.show()
df.printSchema()
df.sort(df.fname.asc()).show()



# for sorting the selected columns df.sort(df.fname.desc()).show()
#for selecting the individual columns df.select(df.fname.alias("fristname")).show()
#cast conversion for selected columnsdf.select(df.fname,df.lname,df.gender,df.id.cast("int")).printSchema()
#between() -returns Boolean expression when a column value in between upper and lower bound.
df.filter(df.id.between(100,300)).show()



#contains checks if Dataframe columns value contains a specified in the function
df.filter(df.fname.contains("Cruise")).show()


#startswith() & endswith() – Checks if the value of the DataFrame Column starts and ends with a String
df.filter(df.fname.startswith("T")).show()
df.filter(df.fname.endswith("Cruise")).show()



#isNull & isNotNull() – Checks if the DataFrame column has NULL or non NULL values.
df.filter(df.lname.isNull()).show()
df.filter(df.lname.isNotNull()).show()



#like() & rlike() – Similar to SQL LIKE expression
#like , rlikedf.select(df.fname,df.lname,df.id).filter(df.fname.like("%om")).show()
#substr() - Returns from the columns 
df.select(df.fname.substr(1,2).alias("substr")).show()





#4.11 when() & otherwise() – It is similar to SQL Case When, executes sequence of expressions until it matches the condition and returns a value when match.
from pyspark.sql.functions import when
df.select(df.fname,df.id,df.lname,when(df.gender=='M',"Male")
          .when(df.gender=="F","Female")
          .when(df.gender==None,"")
          .otherwise(df.gender).alias("new_gender")).show()



#isin() – Check if value presents in a List.
li=["100","200"]
df.select(df.fname,df.lname,df.id).filter(df.id.isin(li)).show()


#ArrayType -- for list#Map Type  -- for dictionary#String Type -- for string 
#getField() – To get the value by key from MapType column and by stuct child name from StructType column
from pyspark.sql.types import StringType,StructType,StructField,ArrayType,MapType
data=[(("James","Bond"),["Java","C#"],{'hair':'black','eye':'brown'}),(("Ann","Varsa"),[".NET","Python"],{'hair':'brown','eye':'black'}),(("Tom Cruise",""),["Python","Scala"],{'hair':'red','eye':'grey'}),(("Tom Brand",None),["Perl","Ruby"],{'hair':'black','eye':'blue'})]
schema = StructType([StructField('name',StructType([StructField('fname',StringType(),True),StructField('lname',StringType(),True)])),StructField('languages',ArrayType(StringType()),True),StructField('properties',MapType(StringType(),StringType()),True)])
df =spark.createDataFrame(data,schema)
df.printSchema()




#getField from MapType
df.select(df.properties.getField("hair")).show()
#getItem() used with MapType
df.select(df.properties.getItem("hair")).show()
#get Field from array Type
df.select(df.languages.getItem(1)).show()
#get Field from Struct
df.select(df.name.getField("fname")).show()




# PySpark – select()
# #pyspark select columns from Dataframe
import pyspark 
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [("James","Smith","USA","CA"),("Michael","Rose","USA","NY"),("Robert","Williams","USA","CA"),("Maria","Jones","USA","FL")]
columns = ["firstname","lastname","country","state"]
df = spark.createDataFrame(data = data, schema = columns)
df.show(truncate=False)



#select single and Multiple columns from DataFrame
# #m-1
df.select("firstname","lastname").show()
#M-2
df.select(df.firstname,df.lastname).show()
#M-3
df.select(df["firstname"],df["lastname"]).show()
#M-4
 

from pyspark.sql.functions import col
df.select(col("firstname"),col("lastname")).show()






#ALL columns from the list
df.select(*columns).show()
df.select('*').show()
df.select([col for col in df.columns]).show()


#select columns from the list
# #columns 0 to 3
# #rows-3
df.select(df.columns[:3]).show(3)




#for nested columns 
from pyspark.sql.types import StructType,StructField, StringType
data = [(("James",None,"Smith"),"OH","M"),(("Anna","Rose",""),"NY","F"),(("Julia","","Williams"),"OH","F"),(("Maria","Anne","Jones"),"NY","M"),(("Jen","Mary","Brown"),"NY","M"),(("Mike","Mary","Williams"),"OH","M")]
schema = StructType([StructField('name', StructType([StructField('firstname', StringType(), True),StructField('middlename', StringType(), True),StructField('lastname', StringType(), True)])),StructField('state', StringType(), True),StructField('gender', StringType(), True)])
df2 = spark.createDataFrame(data = data, schema = schema)
df2.printSchema()
df2.show(truncate=False)





#for nested columns
df2.select("name.firstname","name.lastname").show(truncate=False)


# PySpark – collect()# Select vs Collect both  are used for the retriving data from the data sets 
#Collect - Disadvanages not used for larger datasets we need to avoid 
# # select we need to use all the time  
# PySpark – collect()
data=[("James","Bond","100",None),("Ann","Varsa","200",'F'),("Tom Cruise","XXX","400",''),("Tom Brand",None,"400",'M')]
columns=["fname","lname","id","gender"]
df=spark.createDataFrame(data,columns)
df.show(truncate=False)
dataCollect = df.collect()
print(dataCollect)


#Returns value of First Row, First Column which is "Finance"
#[0]--indicate Row#[1]--columndf.collect()[0][1]df.collect()
#returns Array of Row type.df.collect()[0] 
#returns the first element in an array (1st row).





# PySpark – withColumn()
#DataFrame which is used to change the value, convert the datatype of an existing column, create a new column
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [('James','','Smith','1991-04-01','M',3000),('Michael','Rose','','2000-05-19','M',4000),('Robert','','Williams','1978-09-05','M',4000),('Maria','Anne','Jones','1967-12-01','F',4000),('Jen','Mary','Brown','1980-02-17','F',-1)]
columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.show()
df.printSchema()



# PySpark – withColumn()#1)Change DataType using PySpark withColumn()
# #Note - we can do cast conversion using select and withcolumn
from pyspark.sql.functions import col,lit
df.withColumn("salary",col("salary").cast("Integer")).printSchema() 


##--- total column printed along with wanted column
df.select(df.firstname,df.middlename,df.salary.cast("int")).printSchema() 

##---required columns only printed
#cast conversion for selected columns --- Using Select
df.select(df.fname,df.lname,df.gender,df.id.cast("int")).printSchema()

#2. Update The Value of an Existing Column
df.withColumn("salary",col("salary")*100).show()

#3. Create a Column from an Existing
df.withColumn("Copiedcolumn",col("salary")-200).show()

#4. Add a New Column using withColumn()
#Note - PySpark lit() function is used to add a constant value to a DataFrame column.
df.withColumn("added new column",lit("USA")).show()


#5. Rename Column Name usng ---withColumn
df.withColumnRenamed("gender","sex").show() 

#6--- total column printed along with wanted column
df.select(df.gender.alias("sex")).show()

#7 --- only selected column printed
#Note -- for renaming the columns --- Using Select# 
df.select(df.fname.alias("fristname")).show()
df.select(df.lname.alias("lastname")).show()
df.select(df.id.alias("Information Details")).show()

#8Drop Column From PySpark DataFrame
df.drop("salary").show()



# PySpark – withColumnRenamed()
#1. Rename Column Name usng ---withColumn
df.withColumnRenamed("gender","sex").show() 



#--- total column printed along with wanted column
df.select(df.gender.alias("sex")).show()



# --- only selected column printed
#2)2. PySpark withColumnRenamed – To rename multiple columns
df.withColumnRenamed("firstname","FRIST_NAME").withColumnRenamed("lastname","LAST_NAME").show()




# PySpark – where() & filter()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [('James','','Smith','1991-04-01','M',3000),('Michael','Rose','','2000-05-19','M',4000),('Robert','','Williams','1978-09-05','M',4000),('Maria','Anne','Jones','1967-12-01','F',4000),('Jen','Mary','Brown','1980-02-17','F',-1)]
columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.show()
df.printSchema()



#2. DataFrame filter() with Column Condition
df.filter(df.gender == 'M').show()




#3. DataFrame filter() with SQL Expression
from pyspark.sql.functions import col
df.filter(col("gender")== 'M').show()
# Not equals condition
df.filter(df.gender != "M").show(truncate=False)
df.filter(~(df.gender == "M")).show(truncate=False)


#4. PySpark Filter with Multiple Conditions
df.filter((df.gender=='M') & (df.salary == 4000)).show()



#5. Filter Based on List Values
li=[4000,1000]
df.filter(df.salary.isin(li)).show()




# PySpark – drop() & dropDuplicates()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [('James','','Smith','1991-04-01','M',3000),('Michael','Rose','','2000-05-19','M',4000),('Robert','','Williams','1978-09-05','M',4000),('Maria','Anne','Jones','1967-12-01','F',4000),('Jen','Mary','Brown','1980-02-17','F',-1)]
columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.show()
df.printSchema()


disntict_df = df.distinct()
print("Distinct count: " +str(disntict_df.count()))
disntict_df.show()

#apply on rows for droping duplicate records
df2 = df.dropDuplicates()
print("Distinct count: "+str(df2.count()))
df2.show(truncate=False)



#applying on multiple columns for dropping duplicate records
dropDisDF = df.dropDuplicates(["gender","salary"])
dropDisDF.show(truncate=False)



# PySpark – orderBy() and sort()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data =[('James','','Smith','1991-04-01','M',3000),('Michael','Rose','','2000-05-19','M',4000),('Robert','','Williams','1978-09-05','M',4000),('Maria','Anne','Jones','1967-12-01','F',4000),('Jen','Mary','Brown','1980-02-17','F',-1)]
columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.show()
df.printSchema()



#1)DataFrame sorting using the sort() function
#Note -- by default it will sort ascending order
#sort    --df.firstname
#        --col("firstname")
#Orderby --col("firstname")
df.sort("firstname","lastname").show(truncate=False)
df.sort(col("firstname"),col("lastname")).show(truncate=False)

df.sort(df.firstname.asc(),df.lastname.asc()).show(truncate=False)
df.sort(col("firstname").asc(),col("lastname").asc()).show(truncate=False)

df.sort(df.firstname.asc(),df.lastname.desc()).show(truncate=False)
df.sort(col("firstname").asc(),col("lastname").desc()).show(truncate=False)

# orderBy() function to sort on one or more columns. By default, it orders by ascending.
df.orderBy("firstname","lastname").show(truncate=False)
df.orderBy(col("firstname"),col("lastname")).show(truncate=False)





#PySpark – groupBy()
#PySpark groupBy() function is used to collect the identical data into groups on DataFrame and perform count, sum, avg, min, max functions on the grouped data
#sum() – Returns the total for values for each group.
#avg() – Returns the average for values for each group.
#mean() – Returns the mean of values for each group.
#max() – Returns the maximum of values for each group.
#min() – Returns the minimum of values for each group.
#agg() – Using groupBy() agg() function, we can calculate more than one aggregate at a time


simpleData = [("James","Sales","NY",90000,34,10000),("Michael","Sales","NY",86000,56,20000),("Robert","Sales","CA",81000,30,23000),("Maria","Finance","CA",90000,24,23000),("Raman","Finance","CA",99000,40,24000),("Scott","Finance","NY",83000,36,19000),("Jen","Finance","NY",79000,53,15000),("Jeff","Marketing","CA",80000,25,18000),("Kumar","Marketing","NY",91000,50,21000)]
schema = ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data=simpleData, schema = schema)
df.printSchema()
df.show(truncate=False)
df.groupBy("department").sum("salary").show(truncate=False)
df.groupBy("department").count().show()
df.groupBy("department").min("salary").show()
df.groupBy("department").max("salary").show()


#applying groupby on multiple columns 
df.groupBy("department","state").sum("salary","bonus").show()
#4. Running more aggregates at a time
from pyspark.sql.functions import sum,avg,max
df.groupBy("department").agg(sum("salary").alias("sum_salary"),avg("salary").alias("avg_salary"),sum("bonus").alias("sum_bonus"),max("bonus").alias("max_bonus")).show(truncate=False)
#5. Using filter on aggregate data
from pyspark.sql.functions import sum,avg

df.groupBy("department").agg(sum("salary").alias("sum_salary"),
                                avg("salary").alias("avg_salary"),
                                sum("bonus").alias("sum_bonus"),
                                max("bonus").alias("max_bonus")).where(col("sum_bonus") >= 50000).show(truncate=False)

# PySpark – join()
emp = [(1,"Smith",-1,"2018","10","M",3000),(2,"Rose",1,"2010","20","M",4000),(3,"Williams",1,"2010","10","M",1000),(4,"Jones",2,"2005","10","F",2000),(5,"Brown",2,"2010","40","",-1),(6,"Brown",2,"2010","50","",-1)]
empColumns = ["emp_id","name","superior_emp_id","year_joined","emp_dept_id","gender","salary"]
empDF = spark.createDataFrame(data=emp, schema = empColumns)
empDF.printSchema()
empDF.show(truncate=False)


dept = [("Finance",10),("Marketing",20),("Sales",30),("IT",40)]
deptColumns = ["dept_name","dept_id"]
deptDF = spark.createDataFrame(data=dept, schema = deptColumns)
deptDF.printSchema()
deptDF.show(truncate=False)


print("#3. PySpark Inner Join DataFrame")# This joins two datasets on key columns, where keys don’t match the rows get dropped from both datasets (emp & #dept)

empDF.join(deptDF,empDF.emp_dept_id == deptDF.dept_id,"inner").show(truncate=False)
print("#4. PySpark Full Outer Join")
# Outer a.k.a full, fullouter join returns all rows from both datasets, where join expression doesn’t match it #returns null on respective record columns# 

empDF.join(deptDF,empDF.emp_dept_id == deptDF.dept_id,"Outer").show(truncate=False)
empDF.join(deptDF,empDF.emp_dept_id == deptDF.dept_id,"full").show(truncate=False)
empDF.join(deptDF,empDF.emp_dept_id == deptDF.dept_id,"fullouter").show(truncate=False)

print("#5. PySpark Left Outer Join")

empDF.join(deptDF,empDF.emp_dept_id == deptDF.dept_id,"left").show(truncate=False)
empDF.join(deptDF,empDF.emp_dept_id == deptDF.dept_id,"leftouter").show(truncate=False)

print("#6. Right Outer Join") 
empDF.join(deptDF,empDF.emp_dept_id == deptDF.dept_id,"right").show(truncate=False)
empDF.join(deptDF,empDF.emp_dept_id == deptDF.dept_id,"rightouter").show(truncate=False)

print('''#7. Left Semi Join--leftsemi join returns all columns from the left dataset and ignores all columns from the right dataset''')
empDF.join(deptDF,empDF.emp_dept_id == deptDF.dept_id,"leftsemi").show(truncate=False)

print("#8. Left Anti Join--leftanti join returns only columns from the left dataset for non-matched records.")
empDF.join(deptDF,empDF.emp_dept_id == deptDF.dept_id,"leftanti").show(truncate=False)

# PySpark – union() & unionAll()print('''Dataframe union() – union() method of the DataFrame is used to merge two DataFrame’s of the same structure/schema. If schemas are not the same it returns an error.''')
# DataFrame unionAll() – unionAll() is deprecated since Spark “2.0.0” version and replaced with union().
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
simpleData = [("James","Sales","NY",90000,34,10000),("Michael","Sales","NY",86000,56,20000),("Robert","Sales","CA",81000,30,23000),("Maria","Finance","CA",90000,24,23000)]
columns= ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data = simpleData, schema = columns)
df.printSchema()
df.show(truncate=False)


simpleData2 =[("James","Sales","NY",90000,34,10000),("Maria","Finance","CA",90000,24,23000),("Jen","Finance","NY",79000,53,15000),("Jeff","Marketing","CA",80000,25,18000),("Kumar","Marketing","NY",91000,50,21000)]
columns2= ["employee_name","department","state","salary","age","bonus"]
df2 = spark.createDataFrame(data = simpleData2, schema = columns2)
df2.printSchema()
df2.show(truncate=False)
df3=df.union(df2)
df3.show(truncate=False)


# PySpark – unionByName()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()



# Create DataFrame df1 with columns name, and id
data = [("James",34),("Michael",56),("Robert",30),("Maria",24)]
df1 = spark.createDataFrame(data = data,schema=["name","id"])
df1.printSchema()


# Create DataFrame df2 with columns name and id
data2=[(34,"James"),(45,"Maria"),(45,"Jen"),(34,"Jeff")]
df2 = spark.createDataFrame(data = data2, schema = ["id","name"])
df2.printSchema()
df3=df2.unionByName(df1)
df3.show(truncate=False)


#if schema having different number of columns then add mention #allowMissingColumns=True

# Create DataFrames with different column names

data1=[[5, 2, 6]]
schema1=["col0", "col1", "col2"]
data2=[[6, 7, 3]]
schema2=["col1", "col2", "col3"]
df1 = spark.createDataFrame(data=data1,schema =schema1 )
df2 = spark.createDataFrame(data=data2,schema =schema2)


# Using allowMissingColumns
df3 = df1.unionByName(df2,allowMissingColumns=True)
df3.printSchemadf3.show()

# PySpark – UDF (User Defined Function)# select(), withColumn() 
# PySpark – UDF (User Defined Function)# select(), withColumn()
from pyspark.sql.functions import col,udf
from pyspark.sql.types import StringType
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
columns = ["Seqno","Name"]
data = [("1", "john jones"),("2", "tracey smith"),("3", "amy sanders")]
df = spark.createDataFrame(data=data,schema=columns)
df.show(truncate=False)


#2.2 Create a Python Function
def convertCase(str):
    resStr=""
    arr = str.split(" ")
    for x in arr:
        resStr= resStr + x[0:1].upper() + x[1:len(x)] + " "
        return resStr 
    

#Convert the above python code to UDF
convertUDF = udf(lambda z: convertCase(z),StringType())
df.select(col("Seqno"),convertUDF(col("Name")).alias("Name")).show(truncate=False)

#Now using withColumn we can convert the UDF form 
#Note: With column no need to provide the col # Note: Select we should provide the col and should provide the alias 
def UpperCase(str):
    return str.upper()

convertUDF = udf(lambda z: UpperCase(z),StringType())
df.withColumn("Cureated Name", convertUDF(col("Name"))).show(truncate=False)


#Creating UDF using Annotation 
@udf(returnType=StringType())
def UpperCase(str):
    return str.upper()
df.withColumn("Created name",UpperCase(col("Name"))).show(truncate=False)


# PySpark – transform()
# Imports
from pyspark.sql import SparkSession
from pyspark.sql.functions import upper
from pyspark.sql.functions import transform
SparkSessionspark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
DatasimpleData = (("Java",4000,5),("Python",4600,10),("Scala",4100,15),("Scala",4500,15),("PHP", 3000,20))
columns= ["CourseName", "fee", "discount"]
DataFramedf = spark.createDataFrame(data = simpleData, schema = columns)
df.printSchema()
df.show(truncate=False)


#. PySpark DataFrame.transform()
from pyspark.sql.functions import upper
def to_upper_str_columns(df):
    return df.withColumn("CourseName",upper(df.CourseName))

#reduce prize
def reduce_price(df,reduceBy):
    return df.withColumn("new_fee",df.fee-reduceBy)
#apply discount 

def apply_discount(df):
    return df.withColumn("Discount_fee",(df.new_fee-df.discount)/100)
# custom function
 
def select_columns(df):
    return df.select("CourseName","discounted_fee")


df2 = df.transform(to_upper_str_columns).transform(reduce_price,1000).transform(apply_discount).transform(select_columns)

# PySpark – apply()# PySpark – apply()

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
columns = ["Seqno","Name"]
data = [("1", "john jones"),("2", "tracey smith"),("3", "amy sanders")]
df = spark.createDataFrame(data=data,schema=columns)
df.show(truncate=False)

#1)PySpark apply Function using withColumn()
from pyspark.sql.functions import upper
df.withColumn("Uppername",upper(df.Name)).show(truncate=False)

#2)Apply Function using select()
df.select(col("Seqno"),upper(df.Name).alias("Name")).show()

#3)Create Custom Function
def UpperCase(str):
    return str.upper()

# Convert function to udf
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
#4)Register UDF
convertUDF = udf(lambda x: UpperCase(x),StringType())

#5)Apply Custom UDF to Column
df.select(col("Seqno"),convertUDF(col("Name").alias("Name")))
df.show()

#withColumn
df.withColumn("Created_with_column",convertUDF(col("Name"))).show()

#6)PySpark Pandas apply()# Imports
 
import pyspark.pandas as ps 
import numpy as np
technologies = ({'Fee' :[20000,25000,30000,22000,np.NaN],'Discount':[1000,2500,1500,1200,3000]})
# Create a DataFrameps
df = ps.DataFrame(technologies)
print(df)

def add(data):
    return data[0] + data[1]
addDF = df.apply(add,axis=1)
print(addDF)


# PySpark – map()# PySpark – map()
data = [('James','Smith','M',30),('Anna','Rose','F',41),('Robert','Williams','M',62)]
columns = ["firstname","lastname","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.show()

# Refering columns by index.
rdd2=df.rdd.map(lambda x: (x[0]+","+x[1],x[2],x[3]*2))
df2=rdd2.toDF(["name","gender","new_salary"])
df2.show()

# Referring Column Names
rdd2=df.rdd.map(lambda x:(x["firstname"]+","+x["lastname"],x["gender"],x["salary"]*2))

# Referring Column Names
rdd2=df.rdd.map(lambda x:(x.firstname+","+x.lastname,x.gender,x.salary*2)) 

#By calling function 
def func1(x):
    firstName = x.firstname
    lastName = x.lastname
    name = firstName+","+lastName
    gender = x.gender.lower()
    salary = x.salary*2
    return (name,gender,salary)

rdd2 = df.rdd.map(lambda x: func1(x))


# PySpark – flatMap()
# PySpark – flatMap()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = ["Project Gutenbergs","Alices Adventures in Wonderland","Project Gutenbergs","Adventures in Wonderland","Project Gutenbergs"]
rdd=spark.sparkContext.parallelize(data)
for element in rdd.collect():
    print(element)


# Flatmap    
rdd2=rdd.flatMap(lambda x: x.split(" "))
for element in rdd2.collect():
    print(element)

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('pyspark-by-examples').getOrCreate()
arrayData = [('James',['Java','Scala'],{'hair':'black','eye':'brown'}),('Michael',['Spark','Java',None],{'hair':'brown','eye':None}),('Robert',['CSharp',''],{'hair':'red','eye':''}),('Washington',None,None),('Jefferson',['1','2'],{})]
df = spark.createDataFrame(data=arrayData, schema = ['name','knownLanguages','properties'])
df.show(truncate=False)



from pyspark.sql.functions import explode
df2 = df.select(df.name,explode(df.knownLanguages))
df2.printSchema()
df2.show()

# PySpark – foreach()# Import
from pyspark.sql import SparkSession
# Create SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
# Prepare Datacolumns
Datacolumns = ["Seqno","Name"]
data = [("1", "john jones"),("2", "tracey smith"),("3", "amy sanders")]
# Create DataFrame
df = spark.createDataFrame(data=data,schema=columns)
df.show()
# foreach()
#  Example
def f(df):
    print(df.Seqno)
df.foreach(f)




# PySpark – sample() vs sampleBy()
# PySpark – sample() vs sampleBy()#fraction – Fraction of rows to generate, range [0.0, 1.0]. 
# Note that it doesn’t guarantee to provide the exact number of the fraction of records.

#1.1 Using fraction to get a random sample in PySpark
from pyspark.sql import SparkSessionspark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
df=spark.range(100)
print(df.sample(0.06).collect())

#seed – Seed for sampling (default a random seed). Used to reproduce the same random sampling.#1.2 Using seed to reproduce the same Samples in PySpark
print(df.sample(0.1,123).collect())
print(df.sample(0.1,123).collect())
print(df.sample(0.1,456).collect())

#withReplacement – Sample with replacement or not (default False)
#1.3 Sample withReplacement (May contain duplicates)

print(df.sample(True,0.3,123).collect()) 
print(df.sample(0.3,123).collect()) 
# PySpark – fillna() & fill()
# # PySpark – pivot() (Row to Column)# PySpark – partitionBy()
# # PySpark – MapType (Map/Dict)