anno_files = './Annotations_Part/*.mat';
anno_path =  './Annotations_Part/';

anno_imgs = dir(anno_files);
fil = fopen('instances.txt', 'wt');

for ii = 1:numel(anno_imgs)    
    anno_name = anno_imgs(ii).name;  
    load([anno_path, anno_name]);
    for oo = 1:numel(anno.objects)
        obj = anno.objects(oo);
        class_ind = obj.class_ind;
        fprintf(fil,'%d*', class_ind);    
    end
    fprintf(fil, '\n');  
end
fclose(fil);