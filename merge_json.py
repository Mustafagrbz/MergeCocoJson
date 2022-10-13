import json
import sys

from numpy import append

document1 = "Document1.json"
with open(document1) as f:
    data_document1 = json.load(f)
document2 = "Document2.json"
with open(document2) as f:
    data_document2 = json.load(f)


##Control if the format checks

#Document 1
try:
        if data_document1["images"]:
                if data_document1["categories"]:
                        if data_document1["annotations"]:
                                print("Document 1 titles are correct")
                        else: print("annotations is missing")
                else: print("Categories is missing")
        else: print("images is missing")
except:
        print("Unable to process the document please check the titles in document 1")
        sys.exit(0)
try:        
        for i in data_document1["images"]:
                if i["id"]:
                        pass
                elif i["id"] == 0:
                        pass
                else: print("ids are missing in images, in document1")
                if i["file_name"]:
                        pass
                else: print("file names are missing in images, in document1")
except:
        print("Unable to process the document please check the images tab in document 1")  
        sys.exit(0)         
try:
        for i in data_document1["categories"]:
                if i["name"]:
                        pass
                else: print("names are missing in categories, in document1")
                if i["id"]:
                        pass
                else: print("ids are missing in categories, document1")
except:
        print("Unable to process the document please check the categories tab in document 1") 
        sys.exit(0)          
try:
        for i in data_document1["annotations"]:
                if i["image_id"]:
                        pass
                else: print("image ids are missing in annotations, in document1")
                if i["iscrowd"]:
                        if i["iscrowd"] == 1:
                                if i["segmentation"] and i["bbox"]:
                                        if i["counts"] and i["size"]:
                                                pass
                                        else: print("size or counts or both are missing from annotations/segmentation")
                                else: print("segmentation or bbox or both are missing in annonations")
                        elif i["iscrowd"]==0:
                                if i["segmentation"] and i["bbox"]:
                                        pass
                                else: print("size or counts or both are missing from annotations/segmentation")
                        else: print("iscrowd has a value it should not have")
                else:("iscrowd is missing from annotations")        

                if i["category_id"]:
                        pass
                else: print("category ids are missing in annotations, document1")
except:
        print("Unable to process the document please check the annotations tab in document 1")
        sys.exit(0)           

#Document 2
try:
        if data_document2["images"]:
                if data_document2["categories"]:
                        if data_document2["annotations"]:
                                print("Document 2 titles are correct")
                        else: print("annotations is missing")
                else: print("Categories is missing")
        else: print("images is missing")
except:
        print("Unable to process the document please check the titles in document 2")
        sys.exit(0)
try:
        for i in data_document2["images"]:
                if i["id"]:
                        print(i)
                elif i["id"] == 0:
                        pass        
                else: print("ids are missing in images, in document2",i)
                        
                if i["file_name"]:
                        pass
                else: print("file names are missing in images, in document2")
except:
        print("Unable to process the document please check the images in document 2")
        sys.exit(0)   
try:
        for i in data_document2["categories"]:
                if i["name"]:
                        pass
                else: print("names are missing in categories, in document2")
                if i["id"]:
                        pass
                else: print("ids are missing in categories, document2")
except:
        print("Unable to process the document please check the categories in document 2")
        sys.exit(0)

try:
        for i in data_document1["annotations"]:
                if i["image_id"]:
                        pass
                else: print("image ids are missing in annotations, in document2")
                if i["iscrowd"]:
                        if i["iscrowd"] == 1:
                                if i["segmentation"] and i["bbox"]:
                                        if i["counts"] and i["size"]:
                                                pass
                                        else: print("size or counts or both are missing from annotations/segmentation")
                                else: print("segmentation or bbox or both are missing in annonations")
                        elif i["iscrowd"]==0:
                                if i["segmentation"] and i["bbox"]:
                                        pass
                                else: print("size or counts or both are missing from annotations/segmentation")
                        else: print("iscrowd has a value it should not have")
                else:("iscrowd is missing from annotations")        


                if i["category_id"]:
                        pass
                else: print("category ids are missing in annotations, document2")        
except:
        print("Unable to process the document please check the annotations in document 2")
        sys.exit(0)
####

### Key asigments

image_data1 = data_document1["images"]
image_data2 = data_document2["images"]

annotations_data1 = data_document1["annotations"]
annotations_data2 = data_document2["annotations"]


category_data1 = data_document1["categories"]
category_data2 = data_document2["categories"]



#Detecting and deleting the duplicate images
image_name1 = []
image_name2 = []

for i in image_data1:        
        image_name1.append(i["file_name"])

for i in image_data2:
        image_name2.append(i["file_name"])       

duplications = set(image_name1).intersection(set(image_name2))
rm_img = []
rm_img_id = []
for i in duplications: 
        for j in range(len(image_data2)):
                if  image_data2[j]["file_name"] == i:
                        rm_img.append(j)
                        rm_img_id.append(image_data2[j]["id"])
rm_img.reverse()
for index, i in enumerate(rm_img):
        del image_data2[i-index]

#Deleting annotations with the image id that were deleted before from 2. document

rm_annotations = []

for i in rm_img_id:
        for j in range(len(annotations_data2)):
                if annotations_data2[j]["image_id"] == i:
                        rm_annotations.append(j)
                        
                     
for index, i in enumerate(rm_annotations):
        del annotations_data2[i-index]          



cat_name1 = []
cat_name2 = []

for i in category_data1:
        cat_name1.append(i["name"])
for i in category_data2:
        cat_name2.append(i["name"]) 

duplicate_cat_names = set(cat_name1).intersection(set(cat_name2))   

rm_cat_name = []
rm_cat_id = []

for i in duplicate_cat_names:
        for j,name in enumerate(category_data2):
                if name['name'] == i:
                        rm_cat_name.append(name)   

cat1_info = {"name":[],"id":[]}
for i in category_data1:
        cat1_info["name"].append(i["name"])
        cat1_info["id"].append(i["id"])


cat2_info = {"name":[],"id":[]}

for i in rm_cat_name:
        cat2_info["name"].append(i["name"])
        cat2_info["id"].append(i["id"])


#Control the category names and ids if they are same delete category2

control_names = []
verifiy_names = cat1_info["name"]
control_ids = []
verify_ids = cat1_info["id"]


for i in cat1_info["name"]:
        for j in cat2_info["name"]:
              if i == j:
                control_names.append(i)

control_category_names = set(control_names).intersection(set(verifiy_names))

l1 = set(verifiy_names)
l2 = set(control_category_names)

if l1 == l2:
        category_data2 = []
   


#################################

cat_ids = [cat1["id"] for cat1 in category_data1]
cat2_ids = [cat2["id"] for cat2 in category_data2]
for id_ in cat2_ids:
    cat_ids.append(id_)

change_ids = []
cat_new_ids = []
rm_cat = []
for cat1 in category_data1:
    for j, cat2 in enumerate(category_data2):
        condition_1 = (cat1["id"] == cat2["id"])
        condition_2 = (cat1["name"] == cat2["name"])
        # if condition_1 and condition_2:
        #     rm_cat.append(cat2)
        if condition_2:
            change_ids.append([cat2["id"], cat1["id"]])
            rm_cat.append(cat2)
        elif condition_1:
            new_id = max(cat_ids) + 1
            cat_ids.append(new_id)
            new_data = [j, new_id]
            cat_new_ids.append(new_data)
            change_ids.append([cat2["id"], new_id])

new_category_data2 = []
for new_id in cat_new_ids:
    category_data2[new_id[0]]["id"] = new_id[1]

for r in rm_cat:
    category_data2.remove(r)


#################################

# Deleting duplicate Annotations
annotations_data1 = data_document1["annotations"]
annotations_data2 = data_document2["annotations"]

for chng_id in change_ids:
    for i, j in enumerate(annotations_data2):
        if annotations_data2[i]["category_id"] == chng_id[0]:
            annotations_data2[i]["category_id"] = chng_id[1]



#################################


#Resetting annonation ids
b3={}
for i,j in enumerate(data_document1['annotations']):
        b3[j['id']]=i
lastkey3 = list(b3)[-1]   
b4={}
for i,j in enumerate(data_document2['annotations']):
        b4[j['id']]=b3[lastkey3]+i+1

for i,j in enumerate(data_document1['annotations']):
        data_document1['annotations'][i]['id']= b3[data_document1['annotations'][i]['id']]
for i,j in enumerate(data_document2['annotations']):
        data_document2['annotations'][i]['id']= b4[data_document2['annotations'][i]['id']]

image_data1.extend(image_data2)

category_data1.extend(category_data2)

annotations_data1.extend(annotations_data2)

data = {"images":image_data1,"categories":category_data1,"annotations":annotations_data1}


with open("output.json", 'w') as outfile:
     json.dump(data, outfile, separators=(',', ':'))
