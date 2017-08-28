# See https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md

for (( i=1; i<=$#; i++ )); do
    wget -c "https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.${!i}.zip"
done

# For example:
# ./download.sh bg el ka hy ru fa es fr de it pt ar tr pl ko

# If stopped it will not re-start automatically, but if re-started it will continue from where it stopped.

# Remember to check if there is enough disk space - they are about 4GB each.

