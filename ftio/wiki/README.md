Many researchers and developers use [the models that the fastText team has pre-trained on Wikipedia for hundreds of languages](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md).

### Downloading the models
To download** pre-trained models for many languages:

    ./wiki.download.sh bg el ka hy ru

This downloads the zipped models into the current directory.  To unzip them all:

    unzip \*.zip

The zipped models are on the order of 1GB to 10GB in size.  If stopped it will not re-start automatically, but if re-started it will continue from where it stopped.  If you run out of disk space when unzipping, remove .zip files that are already unzipped.

### Using the models

To use the models with a Python library like salestock/fasttext or Gensim that wraps or implements fastText:

    import ftio.wiki.preproc

    line = "This isn't a test!"
    preprocessed_line = preproc.preproc(line)
    ...

### About the models

Each text corpus was pre-processed with [get-wikimedia.sh](https://github.com/facebookresearch/fastText/blob/master/get-wikimedia.sh) before a model was trained with it.

In order to see the pre-trained trained models effectively, strings must be processed at runtime in the same way as the training data were pre-processed.

For example, there is no vector for `"Djibouti"`, only for `"djibouti"`.  Somewhat surprisingly, there are no vectors for `"1st"`, `"3d"`, `"don't"` or `"youtube.com"`.

The following pre-processing steps were taken on each line:
0. Lowercase
1. Remove wiki markup
2. Replace some punctuation with a space
3. Add a space around some other punctuation
4. Replace digits (0-9) with a space
5. Replace multiple spaces with a single space

`preproc.py` implements steps 0 and 2-5.
