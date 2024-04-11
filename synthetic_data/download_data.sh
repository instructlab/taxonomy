export s3_path=https://instruct-lab.s3.us-east.cloud-object-storage.appdomain.cloud
export files=$(find compositional_skills -type f -exec echo {} \;)
export model_filename=mistrial-7b
export data_dir=full_synthetic_data

echo "### Downloading full synthetic data links to directory $data_dir"
export data_path=${files//qna.yaml/}
for i in ${data_path[@]}
do
   mkdir -p $data_dir/$i
   curl -L $s3_path/$i/$model_filename.preview.json -o $data_dir/$i/$model_filename.preview.json
   curl -L $s3_path/$i/$model_filename.parquet -o $data_dir/$i/$model_filename.parquet
done
