# MergeCocoJson
You can merge COCO .json files for segmentation, code will automatically delete duplicate categories, 
images and annotations and if they have the same names diffrent ids or same ids diffrent names it will asign new ids to them according to the 
max id of the first document and will reset annotation ids in the end and combine the files with extend.
