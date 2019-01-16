# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:54:11 2019
@author: wmin_

1.删除多列、
2.更改数据类型、
3.将分类变量转换为数字变量、
4.检查缺失数据、
5.删除列中的字符串、
6.删除列中的空格、
7.用字符串连接两列（带条件）、
8.转换时间戳（从字符串到日期时间格式）
"""

# =============================================================================
#                            1.   删除多列
# =============================================================================
def drop_multiple_col(col_names_list, df): 
    '''
    AIM    -> Drop multiple columns based on their column names 
    INPUT  -> List of column names, df
    OUTPUT -> updated df with dropped columns 
    ------
    '''
    df.drop(col_names_list, axis=1, inplace=True)
    return df


# =============================================================================
#                          2.  转换数据类型
# =============================================================================
# 当数据集变大时，需要转换数据类型来节省内存。
def change_dtypes(col_int, col_float, df): 
    '''
    AIM    -> Changing dtypes to save memory
    INPUT  -> List of column names (int, float), df
    OUTPUT -> updated df with smaller memory  
    ------
    '''
    df[col_int] = df[col_int].astype('int32')
    df[col_float] = df[col_float].astype('float32')


# =============================================================================
#                   3. 将分类变量转换为数值变量
# =============================================================================
#一些机器学习模型要求变量采用数值格式。
#这需要先将分类变量转换为数值变量。同时，
#你也可以保留分类变量，以便进行数据可视化。
def convert_cat2num(df):
    # Convert categorical variable to numerical variable
    num_encode = {'col_1' : {'YES':1, 'NO':0},
                  'col_2'  : {'WON':1, 'LOSE':0, 'DRAW':0}}  
    df.replace(num_encode, inplace=True)  

# =============================================================================
#                       4. 检查缺失数据
# =============================================================================
#如果你要检查每列缺失数据的数量，
#使用下列代码是最快的方法。可以让你更好地了解哪些列缺失的数据更多，
#从而确定怎么进行下一步的数据清洗和分析操作。
def check_missing_data(df):
    # check for any missing data in the df (display in descending order)
    return df.isnull().sum().sort_values(ascending=False)


# =============================================================================
#                   5.  删除列中的字符串
# =============================================================================
#有时候，会有新的字符或者其他奇怪的符号出现在字符串列中，
#这可以使用df[‘col_1’].replace很简单地把它们处理掉。
def remove_col_str(df):
    # remove a portion of string in a dataframe column - col_1
    df['col_1'].replace('\n', '', regex=True, inplace=True) 
    # remove all the characters after &# (including &#) for column - col_1
    df['col_1'].replace(' &#.*', '', regex=True, inplace=True)


# =============================================================================
#                   6.  删除列中的空格
# =============================================================================
#数据混乱的时候，什么情况都有可能发生。字符串开头经常会有一些空格。
#在删除列中字符串开头的空格时，下面的代码非常有用。
def remove_col_white_space(df):
    # remove white space at the beginning of string 
    df[col] = df[col].str.lstrip()



# =============================================================================
#                 7.  用字符串连接两列（带条件）
# =============================================================================
#当你想要有条件地用字符串将两列连接在一起时，这段代码很有帮助。
#比如，你可以在第一列结尾处设定某些字母，然后用它们与第二列连接在一起。
#根据需要，结尾处的字母也可以在连接完成后删除。
def concat_col_str_condition(df):
    # concat 2 columns with strings if the last 3 letters of the first column are 'pil'
    mask = df['col_1'].str.endswith('pil', na=False)
    col_new = df[mask]['col_1'] + df[mask]['col_2']
    col_new.replace('pil', ' ', regex=True, inplace=True)  # replace the 'pil' with emtpy space

# =============================================================================
#                8.  转换时间戳（从字符串到日期时间格式）
# =============================================================================
#在处理时间序列数据时，我们很可能会遇到字符串格式的时间戳列。
#这意味着要将字符串格式转换为日期时间格式(或者其他根据我们的需求指定的格式) ，
#以便对数据进行有意义的分析。
def convert_str_datetime(df): 
    '''
    AIM    -> Convert datetime(String) to datetime(format we want)
  
    INPUT  -> df
    
    OUTPUT -> updated df with new datetime format 
    ------
    '''
    df.insert(loc=2, column='timestamp', value=pd.to_datetime(df.transdate, format='%Y-%m-%d %H:%M:%S.%f')) 
