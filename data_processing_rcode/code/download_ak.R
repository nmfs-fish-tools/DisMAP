# This function can be used to download the most recent survey data files for the AK regions and 
# put them in the data_raw folder.
# The ai_strata.csv, ebs_strata.csv, and goa_strata.csv do not change year to year, and should be retained 
# between updates (do not delete these files)

## New Data download function for getting data from the Fisheries one-stop-shop (FOSS): 
#the API is broken so instead will need to go to FOSS() and manually download the data for each survey and save to local folder. 

# install.packages(c("httr", "jsonlite"))
library(httr)
library(jsonlite)
library(dplyr)

# link to the API
api_link <- "https://apps-st.fisheries.noaa.gov/ods/foss/afsc_groundfish_survey/"


#EBS
res <- httr::GET(
  url = paste0(api_link, '?q={"srvy":"EBS"}'))
data <- jsonlite::fromJSON(base::rawToChar(res$content))

as_tibble(data$items) %>% 
  mutate_if(is.character, type.convert, as.is = TRUE) %>%
  head(3) %>%
  dplyr::mutate(across(where(is.numeric), round, 3)) %>%
  dplyr::select(year, srvy, stratum, species_code, cpue_kgkm2) %>%
  flextable::flextable() %>%
  flextable::fit_to_width(max_width = 6) %>% 
  flextable::theme_zebra() %>%
  flextable::colformat_num(x = ., j = c("year", "species_code"), big.mark = "") 


################## OLD SCRIPT ##########################################

## old script to download from AFSC website. Those data files are outdated and no longer being updated. Instead use the above code/process to get the correct AK survey data
 # from FOSS.... 

# # Check [Alaskan website](https://www.fisheries.noaa.gov/alaska/commercial-fishing/alaska-groundfish-bottom-trawl-survey-data) for any new data and add it to the list, files to watch are ai2014-2018, ebs2017-2018, and goa2015-2017.  Did the names changes?  Are there more recent files?.  
# # This is the old website: https://archive.fisheries.noaa.gov/afsc/RACE/groundfish/survey_data/data.htm and it is not being updated with new data.
# library(tibble)
# download_ak <- function(){
#   # define the destination folder
#   for (i in seq(file_list)){
#     # define the destination file path
#     file <- paste("data_raw", ak_files$survey[i], sep = "/")
#     # define the source url
#     url <- paste("https://apps-afsc.fisheries.noaa.gov/RACE/groundfish/survey_data/downloads", ak_files$survey[i], sep = "/")
#     # download the file from the url to the destination file path
#     download.file(url,file)
#     # unzip the new file - this will overwrite an existing file of the same name
#     unzip(file, exdir = "data_raw")
#     # delete the downloaded zip file
#     file.remove(file)
#   }
# }
# 
# ## Check names on website and make sure to update which files to download based on any name changes with the addition
#   # of a new year of data
# 
# ak_files <- tibble(survey = c("ai1983_2000.zip", 
#                               "ai2002_2012.zip", 
#                               "ai2014_2018.zip", 
#                               
#                               "ebs1982_1984.zip", 
#                               "ebs1985_1989.zip", 
#                               "ebs1990_1994.zip", 
#                               "ebs1995_1999.zip", 
#                               "ebs2000_2004.zip", 
#                               "ebs2005_2008.zip", 
#                               "ebs2009_2012.zip", 
#                               "ebs2013_2016.zip", 
#                               "ebs2017_2019.zip", 
#                               
#                               "goa1984_1987.zip", 
#                               "goa1990_1999.zip", 
#                               "goa2001_2005.zip", 
#                               "goa2007_2013.zip", 
#                               "goa2015_2019.zip"))
# 
# file_list <- ak_files$survey
# download_ak()