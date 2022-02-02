This program sorts the photos based on the time when photo was taken.
Program execution flow is as follows
 - Double click the PhotoSort.py to run it on local system
 - Select the desired folder containing photos. Please select the folder at root level such that it is contains no more subfolders, but only photos.
 - Program will extract 'exif' information from photo contains photo metadata. Date part will be extracted from it.
 - Program will create subfolders in the form of 'YYYY/MMM' under the selected folders
 - Program will create copies of photos by renaming them with the exctrated timecode as follows
   - If 'Date Taken' value is extracted correctly, photo will be renamed with 'DC' code. This the most correct date value with reference to photo.
   - 'Date Modified' value will be exctrated if 'Date Taken' value is not found. This is near to correct date value for photo. For videos it will always be 'Date Modified' as videos are modified as soon as they are created. Photos/vidoes will be renamed with 'DM' code in this case.
 - Program will display the status of photos data extraction. Window will exit after successfull completion
 - Original contents on the selected folder will be kept intact. So the newly sorted contents can be compared with original contents.
    
