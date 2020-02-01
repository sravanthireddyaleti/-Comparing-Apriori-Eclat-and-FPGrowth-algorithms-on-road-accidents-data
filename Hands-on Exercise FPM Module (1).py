
# coding: utf-8

# # Hands-on Exercise for  FPM Module

# ### 1. Exploring properties of the dataset accidents_10k.dat. Read more about it here:  http://fimi.uantwerpen.be/data/accidents.pdf

# In[1]:


get_ipython().system('head accidents_10k.dat')


# <span style="color:red">**Question 1a:** </span>. How many items are there in the data?

# In[1]:


get_ipython().system("awk -- '{for (i = 1; i <= NF; i++) wc[$i] += 1}; END {print length(wc)}' accidents_10k.dat")


# <span style="color:green">**Answer:** </span>310

# <span style="color:red">**Question 1b:** </span> How many transactions are present in the data?

# In[2]:


get_ipython().system('wc -l accidents_10k.dat')


# <span style="color:green">**Answer:** </span> 10000

# <span style="color:red">**Question 1c:** </span>.  What is the length of the smallest transaction?

# In[48]:


get_ipython().system("awk -- '{print NF} ' accidents_10k.dat|sort -n|uniq -c")


# <span style="color:green">**Answer:** </span> The length of the smallest transaction is 23

# <span style="color:red">**Question 1d:** </span>  What is the length of the longest transaction?

# In[49]:


get_ipython().system("awk -- '{print NF} ' accidents_10k.dat|sort -n|uniq -c")


# <span style="color:green">**Answer:** </span> The length of the largest transaction is 45

# <span style="color:red">**Question 1e:** </span>  What is the size of the search space of frequent itemsets in this data?

# <span style="color:green">**Answer:** </span> 

# <span style="color:red">**Question 1f:** </span> 
# Assume that you work for the deparment of transportation that collected this data. What benefit do you see in using itemset mining approaches on this data?

# <span style="color:green">**Answer:** </span> 
# We will be able to find the different circumstances that led to the accidents. Also we might be able to get some common conditions which have caused these accidents.

# <span style="color:red">**Question 1g:** </span>  What type of itemsets (frequent, maximial or closed) would you be interested in discovering this dataset? State your reason.

# <span style="color:green">**Answer:** </span> 
# I would be interested in Frequent itemset as frequent itemset gives the circumstances which led to majority of accidents.

# <span style="color:red">**Question 1h:** </span>  What minsup threshold would you use and why?

# <span style="color:green">**Answer:** </span> 
# I would use minsup as 5000 so that I will be able to get the cause or the circumstances that led to the majority of the accidents.

# ### 2. Generating frequent, maximal and closed itemsets using $\color{red}{\text{Apriori}}$, $\color{red}{\text{ECLAT}}$, and $\color{red}{\text{FPGrowth}}$ algorihtms from the dataset accidents_10k.dat 

# <span style="color:red">**Question 2a:** </span> Generate frequent itemsets using Apriori, for minsup = 2000, 3000, and 4000. Which of these minsup thresholds results in a maximum number of frequent itemsets? Which of these minsup thresholds results in a least number of frequent itemsets? Provide a rationale for these observations.

# In[3]:


get_ipython().system('chmod u+x apriori')
get_ipython().system('./apriori')


# In[4]:


get_ipython().system('./apriori -ts -s-2000 accidents_10k.dat accident_minsup_2000.txt')


# In[5]:


get_ipython().system('./apriori -ts -s-3000 accidents_10k.dat accident_minsup_3000.txt')


# In[6]:


get_ipython().system('./apriori -ts -s-4000 accidents_10k.dat accident_minsup_4000.txt')


# In[7]:


get_ipython().system('wc -l accident_minsup_2000.txt')


# In[8]:


get_ipython().system('wc -l accident_minsup_3000.txt')


# In[9]:


get_ipython().system('wc -l accident_minsup_4000.txt')


# <span style="color:green">**Answer:** </span> 
# For minsup=2000, we have 851034 frequent itemsets and has high frequent itemset whereas for minsup=4000, we have 29501 frequent itemsets and has low frequent itemsets. With lower minsup, we have high number of frequent subsets and as minsup increases, the number of itemsets which are frequent gradually decreases.

# <span style="color:red">**Question 2b:** </span>   Using Apriori, compare the execution time for finding frequent itemsets for minsup = 2000, 3000, and 4000. Which of these minsup thresholds takes the least amount of time? Provide a rationale for this observation.

# In[15]:


import datetime 
start_time = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-2000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# In[16]:


import datetime 
start_time = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-3000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# In[17]:


import datetime 
start_time = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-4000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# <span style="color:green">**Answer:** </span>
# For minsup= 4000, it took only a little over 1 second and has the least computation time because it has only fewer frequent itemsets to be computed.

# <span style="color:red">**Question 2c:** </span> Using Apriori, find the frequent itemsets for minsup = 2000, 3000, and 4000. Determine the number of itemsets for each size (1 to max length of an itemset). What trends do you see that are common for all three minsup thresholds? What trends do you see that are different? Provide a rationale for these observations.

# In[22]:


get_ipython().system("awk '{print NF-1}' accident_minsup_2000.txt|sort -n|uniq -c")


# In[23]:


get_ipython().system("awk '{print NF-1}' accident_minsup_3000.txt|sort -n|uniq -c")


# In[24]:


get_ipython().system("awk '{print NF-1}' accident_minsup_4000.txt|sort -n|uniq -c")


# <span style="color:green">**Answer:** </span> 
# Common for all the three minsup is as the size of itemset increases, the number of itemset having that size first increases and then decreases.
# The difference is that for the same size of itemset, the number of itemsets having that size will be different for different minsups because the higher the minsup,the frequency of the itemset should be higher which results in decrease in the number of frequent itemsets.

# <span style="color:red">**Question 2d:** </span>  Using Apriori with minsup=2000, compare the number of frequent, maximal, and closed itemsets. Which is the largest set and which is the smallest set? Provide a rationale for these observations.

# In[29]:


get_ipython().system('./apriori -ts -s-2000 accidents_10k.dat accident_Frequent_minsup_2000.txt')


# In[25]:


get_ipython().system('./apriori -tm -s-2000 accidents_10k.dat accident_Maximal_minsup_2000.txt')


# In[28]:


get_ipython().system('./apriori -tc -s-2000 accidents_10k.dat accident_Closed_minsup_2000.txt')


# <span style="color:green">**Answer:** </span> 
# Largest set is frequent itemset and smallest set is maximal itemset. Since closed and maximal are subsets of frequent itemsets, frequent itemsets have largest sets.

# <span style="color:red">**Question 2e:** </span> For a minsup = 2000, compare the execution time for Apriori, ECLAT and FPGrowth. Which of these algorithms took the least amount of time. Provide a rationale for this observation.

# In[22]:


import datetime 
start_time = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-2000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print("apriori  ",elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# In[2]:


get_ipython().system('chmod u+x eclat')
start_time = datetime.datetime.now()
get_ipython().system('./eclat -ts -s-2000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print("eclat  ",elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# In[3]:


get_ipython().system('chmod u+x fpgrowth')
start_time = datetime.datetime.now()
get_ipython().system('./fpgrowth -ts -s-2000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print("fpgrowth  ",elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# <span style="color:green">**Answer:** </span> 
# Fpgrowth algorithm took the least amount of time. As Apriori algorithm reads the database for each and every itemset frequency computation, it takes a long time. But in eclat, by using transaction id sets, we are eliminating the itemsets which dont have the minsupport as we are moving forward, so the number of itemsets for frequency computation decreases so the computational time decreases.In Fpgrowth, the number of datbase computation gets for decreased while projecting the itemset,so it will have further less computational time

# <span style="color:red">**Question 2f:** </span> For a minsup = 4000, compare the execution time for Apriori, ECLAT and FPGrowth. Which of these algorithms took the least amount of time. Provide a rationale for this observation.

# In[4]:


start_time = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-4000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print("apriori  ",elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# In[20]:


start_time = datetime.datetime.now()
get_ipython().system('./eclat -ts -s-4000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print("eclat  ",elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# In[21]:


start_time = datetime.datetime.now()
get_ipython().system('./fpgrowth -ts -s-4000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print("fpgrowth  ",elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# <span style="color:green">**Answer:** </span>
# Fpgrowth algorithm took the least amount of time. As Apriori algorithm reads the database for each and every itemset frequency computation, it takes a long time. But in eclat, by using transaction id sets, we are eliminating the itemsets which dont have the minsupport as we are moving forward, so the number of itemsets for frequency computation decreases so the computational time decreases.In Fpgrowth, the number of datbase computation gets for decreased while projecting the itemset,so it will have further less computational time

# <span style="color:red">**Question 2g:** </span>  For a minsup = 6000, compare the execution time for Apriori, ECLAT and FPGrowth. Which of these algorithms took the least amount of time. Provide a rationale for this observation.

# In[7]:


start_time = datetime.datetime.now()
get_ipython().system('./apriori -ts -s-6000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print("apriori  ",elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# In[19]:


start_time = datetime.datetime.now()
get_ipython().system('./eclat -ts -s-6000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print("eclat  ",elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# In[18]:


start_time = datetime.datetime.now()
get_ipython().system('./fpgrowth -ts -s-6000 accidents_10k.dat ')
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print("fpgrowth  ",elapsed_time.seconds,"Seconds ",elapsed_time.microseconds,"Microsecs");


# <span style="color:green">**Answer:** </span> 
# Fpgrowth algorithm took the least amount of time.

# <span style="color:red">**Question 2h:** </span> Fill the following table based on execution times computed in __2e__, __2f__, and __2g__. State your observations on the relative computational efficiency at different support thresholds. Based on your knowledge of these algorithms, provide the reasons behind your observations.

# |   Algorithm                |minsup=2000         |minsup=4000         |minsup=6000         |
# |----------------------------|--------------------|--------------------|--------------------|    
# |Apriori                     |      20.1          |      1.65          |      0.32          |
# |Eclat                       |      0.59          |      0.31          |      0.26          |
# |FPGrowth                    |      0.41          |      0.28          |      0.25          |

# <span style="color:green">**Answer:** </span> 
# Fpgrowth algorithm took the least amount of time to compute frequent itemsets. Although as the minsup is increased, we can find that apriori computational time decreased drastically as the number of frequent itemset decreases.

# ### 3. Discovering frequent subsequences and substrings

# Assume that roads in a Cincinnati are assigned numbers. Participants are enrolled in a transportation study and for every trip they make using their car, the sequence of roads taken are recorded. Trips that involves freeways are excluded. This data is in the file <span style="color:blue">road_seq_data.dat</span>.

# <span style="color:red">**Question 3a:** </span>  What 'type' of sequence mining will you perform to determine frequently taken 'paths'? Paths are sequences of roads traveresed consecutively in the same order.

# <span style="color:green">**Answer:** </span> 
# Substring  

# <span style="color:red">**Question 3b:** </span> How many sequences are there in this sequence database?

# In[23]:


get_ipython().system('wc -l road_seq_data.dat')


# <span style="color:green">**Answer:** </span> 1000

# <span style="color:red">**Question 3c:** </span> What is the size of the alphabet in this sequence database?

# In[24]:


get_ipython().system("awk -- '{for (i = 1; i <= NF; i++) wc[$i] += 1}; END {print length(wc)}' road_seq_data.dat")


# <span style="color:green">**Answer:** </span> 1283

# <span style="color:red">**Question 3d:** </span> What are the total number of possible subsequences of length 2 in this dataset?

# In[46]:


get_ipython().system('awk -- \'{for (i = 1; i <= NF-1; i++) for (j=i+1; j<= NF; j++) wc[$i","$j] += 1}; END {print length(wc)}\' road_seq_data.dat')


# <span style="color:red">**Question 3e:** </span> What are the total number of possible substrings of length 2 in this dataset?

# In[45]:


get_ipython().system('awk -- \'{for (i = 1; i <= NF-1; i++) wc[$i","$(i+1)] += 1}; END {print length(wc)}\' road_seq_data.dat')


# <span style="color:red">**Question 3f:** </span> Discover frequent __subsequences__ with minsup = 10 and report the number of subsequences discovered.

# In[21]:


get_ipython().system('chmod u+x prefixspan')
get_ipython().system("./prefixspan -min_sup 10 road_seq_data.dat| sed -n 'p;n' > road_subseq.txt")


# In[22]:


get_ipython().system('wc -l road_subseq.txt')


# <span style="color:green">**Answer:** </span> 
# 4589

# <span style="color:red">**Question 3g:** </span>  Discover frequent __substrings__ with minsup = 10 and report the number of substrings discovered.

# In[26]:


get_ipython().system('chmod u+x seqwog')
get_ipython().system('./seqwog -ts -s-10 road_seq_data.dat road_substring.txt')


# In[27]:


get_ipython().system('wc -l road_substring.txt')


# <span style="color:green">**Answer:** </span> 
# 613

# <span style="color:red">**Question 3h:** </span> Explain the difference in the number of frequent subsequences and substrings found in __3f__ and __3g__ above.

# <span style="color:green">**Answer:** </span> 
# For subsequences, it computes support for all the subsequences present in the sequence whereas for substring, it computes support for all those subsequences which are present consecutively only. So there will be fewer number of frequent substrings.
