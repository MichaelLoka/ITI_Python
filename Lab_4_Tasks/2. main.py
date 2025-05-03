import counting_vowles as v_count
import finding_i_index as i_index
import mult_table as mult
import mario_pyramid as pyr
import array_sort as sort
import user_info as user
import user_login as valid


print("Finding the count of vowles:")
v_count.counting_vowles("This is my first python code")
print("-----------------------------------------\nFinding i index in a sentence:")
i_index.finding_i_index("This is my second python script")
print("-----------------------------------------\nGenerating multiplication table:")
mult.mult_table(5)
print("-----------------------------------------\nMario Pyramid Generation:")
pyr.mario_pyramid(4)
print("-----------------------------------------\nSorting Array Asc & Des:")
sort.sort_array([4,2,7,5,1])
print("-----------------------------------------\nGenerating multiplicaiton table in lists:")
mult.mult__table_list(6)
print("-----------------------------------------\nEntering User Information:")
user.user_info("Michael", "michael@gmail.com")
print("-----------------------------------------\nMario Pyramid Generation with Lists:")
pyr.mario_pyramid_lsit(6)
print("-----------------------------------------\nLogging with username & password:")
valid.user_login("michael", "pass123")
print("-----------------------------------------\nEntering User Information With Exception Hadeling:")
user.user_info_error_handel("Michael", "michael@gmail.com")